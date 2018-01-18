import unittest
import os
import shutil
from dataArchiveReport import *

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.report = create("tests/air.sig995.2012.nc")

    def tearDown(self):
        #os.remove(os.getcwd()+'/tests/scrim_publications.md')
        #os.remove(os.getcwd()+'/tests/clima_publications.md')
        #shutil.rmtree(os.getcwd()+'/tests/scrim_publications')
        #shutil.rmtree(os.getcwd()+'/tests/clima_publications')
        pass

    def test_create(self):
        self.assertIsNotNone(self.report)
        self.assertEqual(self.report.files[0],"tests/air.sig995.2012.nc")

    def test_removeReport(self):
        self.report.removeReport("tests/air.sig995.2012.nc")
        self.assertEqual(len(self.report.files),0)

    def test_addReports(self):
        self.report.removeReport("tests/air.sig995.2012.nc")
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
        self.assertIsNotNone(self.report.reportarize("tests/air.sig995.2012.nc"))
        self.assertIsInstance(self.report.reportarize("tests/air.sig995.2012.nc"),dict)
