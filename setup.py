#!/usr/bin/env python

import sys
import os.path
from setuptools import find_packages, setup


SUB_CATALOG_NAME = 'catalog'
XML_NAME = 'xml'
PACKAGE_NAME = 'ninemlcatalog'

src_dir = os.path.abspath(os.path.dirname(__file__))
catalog_dir = os.path.join(src_dir, PACKAGE_NAME, SUB_CATALOG_NAME)

# Get version number
sys.path.insert(0, os.path.join(src_dir, PACKAGE_NAME))
from version import __version__  # @IgnorePep8
sys.path.pop(0)

# Build package data paths to model description files
package_data = []
prefix_len = len(catalog_dir) + 1
for path, dirs, files in os.walk(catalog_dir):
    package_data.extend(
        (os.path.join(SUB_CATALOG_NAME, path[prefix_len:], f) for f in files
         if os.path.splitext(f)[1] == '.xml'))


setup(
    name=PACKAGE_NAME,
    version=__version__,
    packages=find_packages(),
    package_data={PACKAGE_NAME: package_data},
    author=("The NineML Committee"),
    author_email="tom.g.close@gmail.com",
    description=(
        "A collection of 9ML models and basic Python functions for "
        "accessing them"),
    long_description=open("README.rst").read(),
    license="MIT Licence",
    keywords=("computational neuroscience modeling interoperability XML "
              "YAML JSON HDF5"),
    url="http://nineml.net",
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Scientific/Engineering'],
    install_requires=['nineml>=1.0',
                      'future>=0.16'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    tests_require=['nose'])
