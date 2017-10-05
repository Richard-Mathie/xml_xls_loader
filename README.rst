xml\_xls\_loader
================

Python module to load a MS xml xls into a pandas DataFrame

|PyPI version| |Travis CI| |Code Climate| |Test Coverage|

Usage
-----

.. code:: python

    from xml_xls_loader import xmlxls_to_pd

    dat = xmlxls_to_pd(attachment, header=3, skip_footer=4)

.. |PyPI version| image:: https://img.shields.io/pypi/v/xml_xls_loader.svg
   :target: https://pypi.python.org/pypi/xml_xls_loader
.. |Travis CI| image:: https://travis-ci.org/Richard-Mathie/xml_xls_loader.svg?branch=master
   :target: https://travis-ci.org/Richard-Mathie/xml_xls_loader
.. |Code Climate| image:: https://codeclimate.com/github/Richard-Mathie/xml_xls_loader/badges/gpa.svg
   :target: https://codeclimate.com/github/Richard-Mathie/xml_xls_loader
.. |Test Coverage| image:: https://codeclimate.com/github/Richard-Mathie/xml_xls_loader/badges/coverage.svg
   :target: https://codeclimate.com/github/Richard-Mathie/xml_xls_loader/coverage
