# xml_xls_loader
Python module to load a MS xml xls into a pandas DataFrame

[![PyPI version](https://img.shields.io/pypi/v/xml_xls_loader.svg)](https://pypi.python.org/pypi/xml_xls_loader)
[![Travis CI](https://travis-ci.org/Richard-Mathie/xml_xls_loader.svg?branch=master)](https://travis-ci.org/Richard-Mathie/xml_xls_loader)
[![Code Climate](https://codeclimate.com/github/Richard-Mathie/xml_xls_loader/badges/gpa.svg)](https://codeclimate.com/github/Richard-Mathie/xml_xls_loader)
[![Test Coverage](https://codeclimate.com/github/Richard-Mathie/xml_xls_loader/badges/coverage.svg)](https://codeclimate.com/github/Richard-Mathie/xml_xls_loader/coverage)


## Usage

```python
from xml_xls_loader import xmlxls_to_pd

dat = xmlxls_to_pd(attachment, header=3, skip_footer=4)
```
