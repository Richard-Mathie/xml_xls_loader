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

__NAME__ = 'Flask-Cache-Redis-Cluster'
__doc__ = readme
__author__ = 'Richard-Mathie'
__license__ = 'BSD'

setup(
    name=__NAME__,
    version=version,
    license=__license__,
    description='Adds redis cluster caching support to the Flask Cache(ing) extension',
    long_description=__doc__,
    author=__author__,
    author_email='richard.mathie@cantab.net',
    url='/'.join(['https://github.com', __author__, __NAME__]),
    packages=['flask_cache_redis_cluster'],
    platforms='any',
    install_requires=requirements,
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
