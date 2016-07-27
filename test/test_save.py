import os.path
import shutil
from unittest import TestCase
from ninemlcatalog import load, save, root
import errno


LIAF_PATH = 'neuron/LeakyIntegrateAndFire'
LIAF_NAME = 'LeakyIntegrateAndFire'
BRUNEL_SR_PATH = 'network/brunel2000/SR'
TMP_SUFFIX = '_tmp'


class TestSave(TestCase):

    def _remove_ignore_missing(self, path):
        try:
            os.remove(path)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

    def test_liaf_round_trip(self):
        liaf_doc = load(LIAF_PATH)
        save_path = LIAF_PATH + TMP_SUFFIX
        # Create a copy
        shutil.copy(os.path.join(root, LIAF_PATH + '.xml'),
                    os.path.join(root, save_path + '.xml'))
        liaf = load(save_path, LIAF_NAME)
        try:
            save(liaf, save_path, LIAF_NAME)
            reloaded_doc = load(save_path)
            self.assertEqual(liaf_doc, reloaded_doc)
        finally:
            self._remove_ignore_missing(
                os.path.join(root, save_path + '.xml'))

    def test_brunel_round_trip(self):
        brunel = load(BRUNEL_SR_PATH)
        brunel = brunel.duplicate()
        save_path = BRUNEL_SR_PATH + TMP_SUFFIX
        brunel.url = save_path + '.xml'
        try:
            save(brunel, save_path)
            reloaded_brunel = load(save_path)
            self.assertEqual(brunel, reloaded_brunel)
        finally:
            self._remove_ignore_missing(
                os.path.join(root, save_path + '.xml'))
