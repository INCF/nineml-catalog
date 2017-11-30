from past.builtins import basestring
import os.path
import nineml


root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'catalog'))


class NineMLCatalogSpecifiedMultipleNamesError(Exception):
    pass


def load(path, name=None):
    """
    Retrieves a model from the catalog from the given path
    """
    path, name = get_full_path(path, name)
    doc = nineml.read(path)
    if name is not None:
        elem = doc[name]
    else:
        elem = doc
    return elem


def get_full_path(path, name=None):
    if isinstance(path, basestring):
        if '#' in path:
            parts = path.split('#')
            if name is not None:
                raise NineMLCatalogSpecifiedMultipleNamesError(
                    "Name specified both in kwarg ('{}') and in path string "
                    "'{}' (i.e. section following #)".format(name, parts[1]))
            path, name = parts
        if path.endswith('.xml'):
            path = path[:-4]
        path = path.strip('/').split('/')
    return os.path.join(root, *path) + '.xml', name
