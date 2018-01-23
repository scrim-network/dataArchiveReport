#!/usr/bin/env python
# -*- coding: utf-8 -*-

from report import report
from sys import argv

new_report = report()
new_report.addReports(argv[1:])
new_report.printReport(statistics=True)
