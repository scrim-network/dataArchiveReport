# dataArchiveReport
Returns information about NetCDF files in a data archive.

## Installation

### pip

```
pip install git+git://github.com/scrim-network/dataArchiveReport.git#egg=dataArchiveReport
```

### Manual

Just download and unpack the repository. Make sure the module folder is in your path. Then, install the dependencies:

```
pip install -r requirements.txt
```

## Usage

```
from dataArchiveReport import *
my_report = create(<file name or list of file names>)
```
