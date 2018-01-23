# dataArchiveReport
Returns information about NetCDF files in a data archive.

## Installation

### pip

```
pip install git+git://github.com/scrim-network/dataArchiveReport.git#egg=dataArchiveReport
```

### Manual Installation

Just download and unpack the repository. Make sure the module folder is in your path. Then, install the dependencies:

```
pip install -r requirements.txt
```

## Usage

The simplest way to use this module is to call it with netCDF file names as arguments:

```
python dataArchiveReport file1 [file2 ... fileN]
```

The same output can be created by loading the module in a python script:

```python
from dataArchiveReport import *
file_list = ["file1.nc", "file2.nc", "file3.nc"]
my_report = create(file_list)
my_report.printReport(statistics=True)
```

### Add New Files

```python
new_files = ["new_file1.nc", "new_file2.nc"]
my_report.addReports(new_files)
```

### Remove a File from Report

```python
remove_files = ["new_file1.nc", "file2.nc"]
my_report.removeReports(remove_files)
```
