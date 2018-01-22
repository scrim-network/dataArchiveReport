import unittest
import os
import shutil
from dataArchiveReport import *

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.report = create("tests/air.sig995.2012.nc")

    def tearDown(self):
        if os.path.isdir("data_report"):
            shutil.rmtree("data_report")

    def test_create(self):
        self.assertIsNotNone(self.report)
        self.assertEqual(self.report.files[0],"tests/air.sig995.2012.nc")

    def test_removeReports(self):
        self.report.removeReports("tests/air.sig995.2012.nc")
        self.assertEqual(len(self.report.files),0)

    def test_addReports(self):
        self.report.removeReports("tests/air.sig995.2012.nc")
        self.assertFalse(self.report.addReports(""))
        self.assertTrue(self.report.addReports("tests/air.sig995.2012.nc"))
        self.assertEqual(self.report.files[0],"tests/air.sig995.2012.nc")
        self.assertTrue("tests/air.sig995.2012.nc" in self.report.reports)
        self.assertTrue(self.report.addReports("tests/air.sig995.2012.nc"))
        self.assertEqual(len(self.report.files),1)
        self.assertTrue(self.report.addReports("not-a-file"))
        self.assertEqual(len(self.report.files),1)
        self.assertTrue("not-a-file" in self.report.errors)
        self.assertEqual(len(self.report.reports),1)

    def test_reportarize(self):
        new_report = self.report.reportarize("tests/air.sig995.2012.nc")
        self.assertIsNotNone(new_report)
        self.assertIsInstance(new_report,dict)

    def test_printReport(self):
        self.report.printReport(statistics=True)
        self.report.printReport(save_to_file=True)
        self.assertTrue(os.path.isfile("data_report/report.csv"))
