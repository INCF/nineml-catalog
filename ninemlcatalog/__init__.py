import os.path
import nineml

root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'catalog'))
# Check to see if package has been installed via pip (not actually recommended)
# and catalog has been linked inside the package directory, else use the one
# in the repo root.
if not os.path.exists(root):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                        'xml'))


def load(path, name=None):
    """
    Retrieves a model from the catalog from the given path
    """
    doc = nineml.read(get_full_path(path))
    if name is not None:
        elem = doc[name]
    else:
        elem = doc
    return elem


def get_full_path(path):
    if isinstance(path, basestring):
        if path.endswith('.xml'):
            path = path[:-4]
        path = path.strip('/').split('/')
    return os.path.join(root, *path) + '.xml'
