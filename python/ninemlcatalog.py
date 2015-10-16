from os import path
import nineml

xml_path = path.normpath(path.join(path.dirname(__file__), '..', 'xml'))


def lookup(path_to_model):
    """
    Retrieves a model from the catalog from the given path
    """
    if isinstance(path_to_model, basestring):
        path_to_model = path_to_model.split('/')
    file_path = path.join(xml_path, *path_to_model[:-1]) + '.xml'
    doc = nineml.read(file_path)
    return doc[path_to_model[-1]]
