import os.path
import nineml

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'xml'))


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
    doc = nineml.read(os.path.join(root, *path) + '.xml')
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
    xml = document.to_xml()
    # Get the relative url prefix to the root of the catalog
    prefix = '/'.join(['..'] * (len(path) - 1))
    # Descend through the XML tree and change all 'url' attributes to be
    # relative to the document path
    stack = [xml]
    while stack:
        elem = stack.pop()
        try:
            url = elem.attrib['url']
            if url.startswith(root + '/'):
                url = os.path.join(prefix, url[(len(root) + 1):])
            elif not (url.startswith('http://') or url.startswith('https://')):
                raise NineMLCatalogError(
                    "Cannot save to NineML catalog as non-catalog or web url "
                    "found in model '{}'".format(url))
            elem.attrib['url'] = url
        except KeyError:
            pass
        stack.extend(elem.getchildren())
    nineml.document.write_xml(xml, os.path.join(root, *path) + '.xml')
