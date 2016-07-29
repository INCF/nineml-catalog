#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages

SUB_CATALOG_NAME = 'catalog'
XML_NAME = 'xml'
PACKAGE_NAME = 'ninemlcatalog'

src_dir = os.path.abspath(os.path.dirname(__file__))
xml_dir = os.path.join(src_dir, XML_NAME)
catalog_dir = os.path.join(src_dir, PACKAGE_NAME, SUB_CATALOG_NAME)

# Build package data paths to model description files
package_data = []
prefix_len = len(xml_dir) + 1
for path, dirs, files in os.walk(xml_dir):
    package_data.extend(
        (os.path.join(SUB_CATALOG_NAME, path[prefix_len:], f) for f in files
         if os.path.splitext(f)[1] == '.xml'))

try:
    # Create a symlink to the catalog path inside the package directory so it
    # gets installed within the python package
    os.symlink(xml_dir, catalog_dir)
    setup(
        name="ninemlcatalog",
        version="1.0",
        packages=find_packages(),
        package_data={PACKAGE_NAME: package_data},
        author=("Thomas G. Close"),
        author_email="nineml-users@incf.org",
        description=(
            "A collection of 9ML models and basic Python functions for "
            "accessing them"),
        long_description=open("README.rst").read(),
        license="MIT Licence",
        keywords="computational neuroscience modeling interoperability XML",
        url="http://nineml.incf.org",
        classifiers=['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT Licence',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Topic :: Scientific/Engineering'],
        install_requires=[],  # ['nineml'],
        tests_require=['nose']
    )
finally:
    os.unlink(catalog_dir)
