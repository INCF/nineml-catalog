import os.path
from unittest import TestCase
import nineml
from ninemlcatalog import lookup, save


class TestSave(TestCase):

    def test_liaf_round_trip(self):
        path = 'neuron/LeakyIntegrateAndFire'
        name =  'LeakyIntegrateAndFire'
        liaf_doc = lookup(path)
        liaf = lookup(path, name)
        save(liaf, path, name)
        reloaded_doc = lookup(path)
        # FIXME: Should check a modified version of the model and then resave
        #        the original
        self.assertEqual(liaf_doc, reloaded_doc)

    def test_brunel_round_trip(self):
        path = 'network/Brunel2000/SR'
        brunel = lookup(path)
        save(brunel, path)
        reloaded_brunel = lookup(path)
        # FIXME: Should check a modified version of the model and then resave
        #        the original        
        self.assertEqual(brunel, reloaded_brunel)
            