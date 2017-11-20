NineML Catalog
==============

.. image:: https://travis-ci.org/INCF/nineml-catalog.svg
   :target: https://travis-ci.org/INCF/nineml-catalog
.. image:: https://coveralls.io/repos/github/INCF/nineml-catalog/badge.svg
   :target: https://coveralls.io/github/INCF/nineml-catalog
.. image:: https://img.shields.io/pypi/pyversions/ninemlcatalog.svg
    :target: https://pypi.python.org/pypi/ninemlcatalog/
    :alt: Supported Python versions
.. image:: https://img.shields.io/pypi/v/ninemlcatalog.svg
    :target: https://pypi.python.org/pypi/ninemlcatalog/
    :alt: Latest Version       

The `NineML Catalog`_ is a collection of NineML_ models written in XML. See
http://nineml.net/software/ for a list of software that support NineML_.

Also included is a simple Python module 'ninemlcatalog'
for convenient access to the models stored in the catalog using the
`NineML Python library`_.


Editors
-------

The `NineML Catalog`_ is maintained by the NineML committee
(http://nineml.net/committee).


Installation
------------

To "install" the XML models in the NineML Catalog simply clone the repository
to somewhere sensible on your local computer (e.g. $HOME/git/nineml-catalog),
and then you can reference the models from other NineML documents using either
relative or absolute URLs. Before cloning, it is best to create a fork of the
central repo (https://github.com/INCF/nineml-catalog) so you can backup any
modifications to your own GitHub repo, and then open merge requests with the
central repo (see Contributing_).

To install the python module you will need to install the `NineML Python library`_.
Then simply add the 'python' directory in the catalog repository to your
PYTHONPATH. Once `NineML Python library`_ is installed you will then be able
to run the unit-tests by the command
 
  $ python -m unittest test
  
from the git repository directory and it will attempt to load and validate
every model in the catalog.

.. note: The Python ninemlcatalog package can also be installed from the
         Python Package Index (PyPI). However, this approach is not recommended
         for general use (it is designed for installations in testing
         environments), as it is better to have a separate catalog per user.


Contributing
------------

Contributions to the catalog are most welcome. To add a model or amend an 
existing one simply make the changes to your local model, push them to your
GitHub fork and open a pull request to the master branch of the INCF fork with
a brief explanation of what your model models or amendment fixes
(see https://help.github.com/articles/using-pull-requests/).


To make merging with the central repository feasible it is strongly recommeded
that you make any distinct sets of changes in separate feature branches from
the central repo's master branch and then merge them together to create your
"develop" branch of the catalog with all your customisations.

Before opening a pull request, please add the author information and relevant 
scientific citations to comments within the annotations block of the document.
It is also encouraged to create or link your model with an entry on
Open Source Brain
(see http://www.opensourcebrain.org/docs#Creating_Your_Own_Project).

.. _NineML: http://nineml.net
.. _`NineML Catalog`: http://github.com/INCF/nineml-catalog
.. _`NineML Python Library`: http://nineml-python.readthedocs.io
