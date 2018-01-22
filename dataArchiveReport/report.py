#!/usr/bin/env python
# -*- coding: utf-8 -*-

from netCDF4 import Dataset, num2date
import os
import numpy

class report:
    def __init__(self):
        self.files = []
        self.reports = {}
        self.errors = {}
        self.metas = ["filename", "dim", "var", "units", "start_date", "end_date", "max_lat", "min_lat", "max_lon", "min_lon"]
        self.stats = ["var_max", "var_min", "var_mean"]
        return None

    def addReports(self,files):
        if len(files) == 0:
            return False
        if not isinstance(files,list):
            files = [files]
        self.files = list(set(self.files + files))
        for f in files:
            if os.path.isfile(f):
                self.reports[f] = self.reportarize(f)
            else:
                self.files.pop(self.files.index(f))
                self.errors[f] = f+' is not a file or is a directory.'
        return True

    def reportarize(self,f):
        new_report = {}
        fid = Dataset(f)
        new_report["filename"] = f
        new_report["dim"] = [x for x in fid.dimensions]
        new_report["var"] = [x for x in fid.variables if x not in new_report["dim"]]
        new_report["units"] = [fid.variables[x].units for x in new_report["var"]]
        if "time" in new_report["dim"]:
            new_report["start_date"] = fid.variables["time"][0]
            new_report["end_date"] = fid.variables["time"][-1]
            if "since" in fid.variables["time"].units:
                new_report["start_date"] = str(num2date(new_report["start_date"],fid.variables["time"].units,calendar="standard"))
                new_report["end_date"] = str(num2date(new_report["end_date"],fid.variables["time"].units,calendar="standard"))
        if "lat" in new_report["dim"]:
            new_report["max_lat"] = str(max(fid.variables["lat"]))
            new_report["min_lat"] = str(min(fid.variables["lat"]))
        if "lon" in new_report["dim"]:
            new_report["max_lon"] = str(max(fid.variables["lon"]))
            new_report["min_lon"] = str(min(fid.variables["lon"]))
        # Statistics Section
        var_max = []
        var_min = []
        var_mean = []
        for v in new_report["var"]:
            data = fid.variables[v][:]
            var_max.append(numpy.amax(data))
            var_min.append(numpy.amin(data))
            var_mean.append(numpy.nanmean(data))
        new_report["var_max"] = var_max
        new_report["var_min"] = var_min
        new_report["var_mean"] = var_mean
        fid.close()
        return new_report

    def removeReports(self,files):
        if not isinstance(files,list):
            files = [files]
        for f in files:
            if f in self.files:
                self.files.pop(self.files.index(f))
                del self.reports[f]
        return None

    def csv(self,keys):
        report_str = ''
        report_str += ",".join(keys) + "\n"
        for filename in self.reports:
            line = []
            for key in keys:
                if key in self.reports[filename]:
                    if isinstance(self.reports[filename][key],list):
                        if len(self.reports[filename][key]) == 1:
                            line.append(str(self.reports[filename][key][0]))
                        else:
                            line.append('"['+','.join(str(x) for x in self.reports[filename][key])+']"')
                    else:
                        line.append(str(self.reports[filename][key]))
            report_str += ",".join(line) + "\n"
        return report_str

    def printReport(self, statistics=False, fmt="csv", save_to_file=False):
        keys = self.metas
        if statistics:
            keys = keys + self.stats
        ff = eval('self.'+fmt)
        report_str = ff(keys)
        if save_to_file:
            if not os.path.isdir("data_report"):
                os.makedirs("data_report")
                fid = open("data_report/report.csv","w")
                fid.write(report_str)
                fid.close()
        else:
            print(report_str)
        return None
