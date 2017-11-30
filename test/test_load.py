import sys
import os.path
from unittest import TestCase
import traceback
import ninemlcatalog

LIAF_PATH = 'neuron/LeakyIntegrateAndFire'
LIAF_NAME = 'LeakyIntegrateAndFire'


class TestLoadCatalog(TestCase):

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    catalog_root = os.path.join(repo_root, 'ninemlcatalog', 'catalog')

    def setUp(self):
        with open(os.path.join(self.repo_root, '.gitignore')) as f:
            self.gitignore = f.read().split('\n')

    def iterate_paths(self, dirname):
        """
        Descencds into the file directory tree and yields every path
        ending with 'xml'
        """
        for f in os.listdir(dirname):
            if not f.startswith('.') and f not in self.gitignore:
                pth = os.path.abspath(os.path.join(dirname, f))
                if os.path.isdir(pth):
                        for p in self.iterate_paths(pth):
                            yield p
                elif f.endswith('.xml'):
                    yield pth[len(self.catalog_root):-4]

    def test_load_all(self):
        errors = []
        for pth in self.iterate_paths(self.catalog_root):
            # Just check to see whether all elements of the document load
            # without error
            try:
                _ = list(ninemlcatalog.load(pth).elements)
            except Exception:
                errors.append(
                    (pth, traceback.format_exception(*sys.exc_info())))
        self.assert_(
            not errors,
            "The following failures occured while attempting to load all "
            "models from the catalog:\n\n{}"
            .format('\n\n'.join("{}\n---\n{}".format(pth, '\n'.join(trace))
                                for pth, trace in errors)))

    def test_load_name(self):
        liaf = ninemlcatalog.load(LIAF_PATH, LIAF_NAME)
        self.assertEqual(liaf.name, LIAF_NAME,
                         "Element loaded from '{}' did not match name "
                         "supplied '{}'".format(LIAF_PATH, LIAF_NAME))
        liaf2 = ninemlcatalog.load(LIAF_PATH + '#' + LIAF_NAME)
        self.assertEqual(liaf2.name, LIAF_NAME,
                         "Element loaded from '{}' did not match name "
                         "supplied '{}'".format(LIAF_PATH, LIAF_NAME))
        self.assertRaises(
            ninemlcatalog.NineMLCatalogSpecifiedMultipleNamesError,
            ninemlcatalog.load,
            LIAF_PATH + '#' + LIAF_NAME,
            LIAF_NAME)

    def test_load_xml_path(self):
        liaf_doc = ninemlcatalog.load(LIAF_PATH + '.xml')
        self.assert_(LIAF_NAME in liaf_doc,
                     "Did not load file with path ending in '.xml'")
