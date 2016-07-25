#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages

SUB_CATALOG_NAME = 'catalog'
XML_NAME = 'xml'

src_dir = os.path.abspath(os.path.dirname(__file__))
xml_dir = os.path.join(src_dir, XML_NAME)
catalog_dir = os.path.join(src_dir, 'ninemlcatalog', SUB_CATALOG_NAME)

# Build package data paths, i.e. all paths in xml directory that are not in
# gitignore
with open(os.path.join(src_dir, '.gitignore')) as f:
    gitignore = [i for i in f.read().split() if not i.startswith('/')]
package_data = []
for path, dirs, files in os.walk(xml_dir, topdown=True):
    dirs[:] = [d for d in dirs if d not in gitignore]
    if path != xml_dir:
        package_data.append(os.path.join(SUB_CATALOG_NAME,
                                         path[(len(xml_dir) + 1):], '*'))

try:
    # Create a symlink to the catalog path inside the package directory so it
    # gets installed along side the package
    os.symlink(xml_dir, catalog_dir)
    setup(
        name="ninemlcatalog",
        version="1.0",
        packages=find_packages(),
        package_data={'ninemlcatalog': package_data},
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
        install_requires=[], # ['nineml'],
        tests_require=['nose']
    )
finally:
    os.unlink(catalog_dir)
