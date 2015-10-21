import os.path
import nineml
from copy import deepcopy

xml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                        'xml'))


class NineMLCatalogError(Exception):
    pass


def lookup(path, name=None):
    """
    Retrieves a model from the catalog from the given path
    """
    if isinstance(path, basestring):
        if path.startswith('/'):
            path = path[1:]
        path = path.split('/')
    doc = nineml.read(os.path.join(xml_path, *path) + '.xml')
    if name is not None:
        elem = doc[name]
    else:
        elem = doc
    return elem


def save(document, path):
    if not isinstance(document, nineml.Document):
        raise NineMLCatalogError(
            "Can only save nineml.Document objects")
    if isinstance(path, basestring):
        if path.startswith('/'):
            path = path[1:]
        path = path.split('/')
    # Deepcopy document so we can change the catalog urls to relative paths
    document = deepcopy(document)
    # Get the relative url prefix to the root of the catalog
    prefix = '/'.join(['..'] * (len(path) - 1))
    _convert_to_relative_urls(document, prefix)
    nineml.write(document, os.path.join(xml_path, *path) + '.xml')


def _convert_to_relative_urls(elem, prefix):
    try:
        if elem.url.startswith(xml_path):
            elem._url = os.path.join(prefix, elem.url[len(xml_path):])
        elif not (elem.url.startswith('http://')
                  or elem.url.startswith('https://')):
            raise NineMLCatalogError(
                "Cannot save to NineML catalog as non-catalog or web url "
                "found in model '{}'".format(elem.url))
    except AttributeError:  # if element doesn't have a url
        pass
    try:
        for child in elem.elements:
            _convert_to_relative_urls(child, prefix)
    except AttributeError:  # if element doesn't have child elements
        pass
