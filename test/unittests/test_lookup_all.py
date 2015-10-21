import os.path
from unittest import TestCase
import nineml


class TestLoadCatalog(TestCase):

    repo_root = os.path.join(os.path.dirname(__file__), '..', '..')

    def setUp(self):
        with open(os.path.join(self.repo_root, '.gitignore')) as f:
            self.gitignore = list(f)

    def iterate_xml_paths(self, dirname):
        """
        Descencds into the file directory tree and yields every path
        ending with 'xml'
        """
        for f in os.listdir(dirname):
            if not f.startswith('.') and f not in self.gitignore:
                pth = os.path.abspath(os.path.join(dirname, f))
                if os.path.isdir(pth):
                     for p in self.iterate_xml_paths(pth):
                         yield p
                elif f.endswith('.xml'):
                    yield pth

    def test_load_and_validate_all(self):
        for p in self.iterate_xml_paths(os.path.join(self.repo_root, 'xml')):
            # Just check to see whether all elements of the document load
            # without error
            all_elems = list(nineml.read(p).elements)
            
             