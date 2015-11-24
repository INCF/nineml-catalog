NineML Catalog
========

The NineML Catalog is a collection of NineML models (see http://nineml.net)
written in XML. See http://nineml.net/software/ for a list of software that
have support for NineML.

Also included is a simple Python module 'ninemlcatalog'
for convenient access to the models stored in the catalog using the lib9ML
Python library (see http://github.com/INCF/lib9ML).


Editors
---

The NineML Calalog is maintained by the NineML committee
(http://nineml.net/committee).


Installation
---

To "install" the XML models in the NineML Catalog simply clone the repository
to somewhere sensible on your local computer (e.g. $HOME/git/ninemlcatalog),
and then you can reference the models from other NineML documents using either
relative or absolute URLs.

To install the python module you will need to install the lib9ML python package
(see http://github.com/INCF/lib9ML). Then simply add the 'python' directory in
the catalog repository to your PYTHONPATH. Once lib9ML is installed you will
then be able to run the unit-tests by the command
 
  python -m unittest <ninemlcatlog-home>/test/unittests/test_validation.py
  
and it will attempt to load and validate every model in the catalog.


Contributing
---

Contributions to the catalog are most welcome. To add a model or amend an 
existing one simply make the changes to your local model, push them to your
GitHub fork and open a pull request to the master branch of the INCF fork with
a brief explanation of what your model models or amendment fixes
(see https://help.github.com/articles/using-pull-requests/).

Before opening a pull request, please add the author information and relevant 
scientific citations to comments within the annotations block of the document.
It is also encouraged to create or link your model with an existing entry on
Open Source Brain
(see http://www.opensourcebrain.org/docs#Creating_Your_Own_Project).
