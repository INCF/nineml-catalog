from unittest import TestCase
from ninemlcatalog import load, save

LIAF_PATH = 'neuron/LeakyIntegrateAndFire'
LIAF_NAME = 'LeakyIntegrateAndFire'
BRUNEL_SR_PATH = 'network/brunel2000/SR'


class TestSave(TestCase):

    def test_liaf_round_trip(self):
        liaf_doc = load(LIAF_PATH)
        liaf = load(LIAF_PATH, LIAF_NAME)
        save(liaf, LIAF_PATH, LIAF_NAME)
        reloaded_doc = load(LIAF_PATH)
        # FIXME: Should check a modified version of the model and then resave
        #        the original
        self.assertEqual(liaf_doc, reloaded_doc)

    def test_brunel_round_trip(self):
        brunel = load(BRUNEL_SR_PATH)
        save(brunel, BRUNEL_SR_PATH)
        reloaded_brunel = load(BRUNEL_SR_PATH)
        # FIXME: Should check a modified version of the model and then resave
        #        the original
        self.assertEqual(brunel, reloaded_brunel)
