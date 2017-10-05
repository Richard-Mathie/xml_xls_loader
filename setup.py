#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip.req import parse_requirements
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('Version', 'r') as f:
    version = next(f).strip().decode('utf-8')

with open('README.rst') as f:
    readme = f.read()

requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in requirements]

__NAME__ = 'xml_xls_loader'
__doc__ = readme
__author__ = 'Richard-Mathie'
__license__ = 'GPLv3'

setup(
    name=__NAME__,
    version=version,
    license=__license__,
    description='Module to load a MS xml xls into a pandas DataFrame',
    long_description=__doc__,
    author=__author__,
    author_email='richard.mathie@cantab.net',
    url='/'.join(['https://github.com', __author__, __NAME__]),
    py_modules=['xml_xls_loader'],
    platforms='any',
    install_requires=requirements,
    test_suite='tests',
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ]
)
