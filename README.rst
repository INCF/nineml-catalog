NineML Catalog
==============

The NineML Catalog (http://github.com/INCF/NineMLCatalog) is a collection of
NineML models (see http://nineml.net) written in XML. See
http://nineml.net/software/ for a list of software that have support for
NineML.

Also included is a simple Python module 'ninemlcatalog'
for convenient access to the models stored in the catalog using the lib9ML
Python library (see http://github.com/INCF/lib9ML).


Editors
-------

The NineML Calalog is maintained by the NineML committee
(http://nineml.net/committee).


Installation
------------

To "install" the XML models in the NineML Catalog simply clone the repository
to somewhere sensible on your local computer (e.g. $HOME/git/ninemlcatalog),
and then you can reference the models from other NineML documents using either
relative or absolute URLs. Before cloning, it is best to create a fork of the
central repo (https://github.com/INCF/NineMLCatalog) so you can backup any
modifications to your own GitHub repo, and then open merge requests with the
central repo (see Contributing).

To install the python module you will need to install the lib9ML python package
(see http://github.com/INCF/lib9ML). Then simply add the 'python' directory in
the catalog repository to your PYTHONPATH. Once lib9ML is installed you will
then be able to run the unit-tests by the command
 
  python -m unittest test.test_load_all
  
from the git repository directory and it will attempt to load and validate
every model in the catalog.

NB: The Python ninemlcatalog package can also be installed using setuptools
(e.g. pip or easy_install) via the setup.py script in the python directory.
However, this approach is not recommended for general use (it is designed for
installations in testing environments), as it is better to have a separate
catalog per user.


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
It is also encouraged to create or link your model with an existing entry on
Open Source Brain
(see http://www.opensourcebrain.org/docs#Creating_Your_Own_Project).
