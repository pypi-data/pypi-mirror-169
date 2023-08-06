# ngdataqualitycheck

**[ngdataqualitycheck](https://pypi.org/project/ngdataqualitycheck)** a Python package for checking data quality and generating the data quality report.


[![Current Release Version](https://shields.io/badge/release-v0.1.0-purple?&logo=github)](https://github.com/ngenux/ngdataqualitycheck/releases)
[![Current Release Version](https://shields.io/badge/pypi-v0.1.0-blue?&logo=pypi)](https://pypi.org/project/ngdataqualitycheck/)
![](https://img.shields.io/badge/python-3.8-blue?&logo=Python)
![](https://img.shields.io/badge/license-Creative%20Commons%20Attribution%20NonCommercial%20NoDerivatives%204.0%20International%20Public%20License-green.svg)

## Table of contents:
- **[Installation](#installation)**
- **[Usage](#usage)**

## Installation:

To install the package in your local environment, open a terminal inside your project directory and type:
```python
pip install ngdataqualitycheck
```  

To upgrade the already existing installation, run
```python
  pip install -U ngdataqualitycheck
```

## Usage:

Here is how you can use the package in your working environment.

```python
# import the package
from ngdataqualitycheck import generate_report

# define the filename
filename = 'sample.csv'

# call the method
generate_report(filename)
```
This will generate a consolidated word document along with three
csv files that contains the global statistics, profile schema and the
profile summary.
