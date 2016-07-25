import os.path
from unittest import TestCase
import nineml
from ninemlcatalog import load, save


class TestSave(TestCase):

    def test_liaf_round_trip(self):
        path = 'neuron/LeakyIntegrateAndFire'
        name =  'LeakyIntegrateAndFire'
        liaf_doc = load(path)
        liaf = load(path, name)
        save(liaf, path, name)
        reloaded_doc = load(path)
        # FIXME: Should check a modified version of the model and then resave
        #        the original
        self.assertEqual(liaf_doc, reloaded_doc)

    def test_brunel_round_trip(self):
        path = 'network/Brunel2000/SR'
        brunel = load(path)
        save(brunel, path)
        reloaded_brunel = load(path)
        # FIXME: Should check a modified version of the model and then resave
        #        the original        
        self.assertEqual(brunel, reloaded_brunel)
            