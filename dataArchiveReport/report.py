#!/usr/bin/env python
# -*- coding: utf-8 -*-

from netCDF4 import Dataset
import os.path

class report:
    def __init__(self):
        self.files = []
        self.reports = {}
        self.errors = {}
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
        return new_report

    def removeReport(self,filename):
        self.files.pop(self.files.index(filename))
        del self.reports[filename]
        return None

    def testPrint(self):
        for f in self.files:
            nc_fid = Dataset(f)
            print(nc_fid.ncattrs())
            nc_dims = [dim for dim in nc_fid.dimensions]
            print(nc_dims)
            nc_vars = [var for var in nc_fid.variables]
            print(nc_vars)
            lats = nc_fid.variables['lat'][:]
            print(lats)
            air = nc_fid.variables['air'][:]
            print(air)
            nc_fid.close()
        return None
