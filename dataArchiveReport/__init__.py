__all__ = ["create"]

from .report import report

def create(files):
    new_report = report()
    new_report.addReports(files)
    return new_report
