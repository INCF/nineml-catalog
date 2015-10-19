import os.path
import nineml

xml_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..',
                                         'xml'))


def lookup(path, name=None):
    """
    Retrieves a model from the catalog from the given path
    """
    doc = nineml.read(os.path.join(xml_path, *(path.split('/'))) + '.xml')
    if name is not None:
        elem = doc[name]
    else:
        elem = doc
    return elem
