import os.path
import nineml

root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'catalog'))
# Check to see if package has been installed via pip (not actually recommended)
# and catalog has been linked inside the package directory, else use the one
# in the repo root.
if not os.path.exists(root):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                        'xml'))


class NineMLCatalogError(Exception):
    pass


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


def save(element, path, name=None):
    if isinstance(element, nineml.Document):
        document = element
    else:
        if name is None:
            raise NineMLCatalogError(
                "Can only save nineml.Document objects if name is not "
                "provided")
        document = load(path)
        document[name] = element
    full_path = get_full_path(path)
    # Deepcopy document so we can change the catalog urls to relative paths
    xml = document.to_xml()
    # Descend through the XML tree and change all 'url' attributes to be
    # relative to the document path
    stack = [xml]
    while stack:
        elem = stack.pop()
        try:
            url = elem.attrib['url']
            if url == path:  # is a local reference
                url = None
            elif url.startswith('.'):
                if element.url.startswith(root):
                    url_path = os.path.abspath(
                        os.path.join(os.path.dirname(element.url), url))
                    if not os.path.exists(url_path):
                        raise NineMLCatalogError(
                            "Reference to missing catalog entry '{}'"
                            .format(url_path))
                else:
                    raise NineMLCatalogError(
                        "Cannot save references to relative files outside the"
                        "catalog '{}', please add them to the catalog first"
                        .format(url))
            elif url.startswith(root + '/'):  # references a catalog file
                url = os.path.relpath(url, full_path)
            elif not (url.startswith('http://') or url.startswith('https://')):
                raise NineMLCatalogError(
                    "Cannot save to NineML catalog as non-catalog or web url "
                    "found in model '{}'".format(url))
            elem.attrib['url'] = url
        except KeyError:
            pass
        stack.extend(elem.getchildren())
    nineml.document.write_xml(xml, full_path)


def get_full_path(path):
    if isinstance(path, basestring):
        if path.endswith('.xml'):
            path = path[:-4]
        path = path.strip('/').split('/')
    return os.path.join(root, *path) + '.xml'
