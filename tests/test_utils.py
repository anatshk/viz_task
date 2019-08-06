import unittest

import numpy as np
import os
import tarfile
import tempfile

from task_code import utils


class TestUtils(unittest.TestCase):
    def test_get_image_jpg(self):
        pth = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files', 'series_009_slice_093.jpg')
        img = utils.get_image(pth)
        self.assertIsInstance(img, np.ndarray)
        self.assertEqual(img.shape, (512, 512))
        self.assertEqual((img.min(), img.max()), (0, 255))

    def test_get_image_bmp(self):
        pth = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files', 'series_009_slice_093.bmp')
        img = utils.get_image(pth)
        self.assertIsInstance(img, np.ndarray)
        self.assertEqual(img.shape, (512, 512))
        self.assertEqual((img.min(), img.max()), (0, 255))

    @unittest.skip('Need to understand why saved image is not loaded as is')
    def test_save_image(self):
        img = np.array([[255] * 10, [100] * 10, [0] * 10,
                        [255] * 10, [100] * 10, [0] * 10,
                        [255] * 10, [100] * 10, [0] * 10,
                        [255] * 10], dtype='uint8')
        temp_dir = tempfile.mkdtemp()
        temp_file = os.path.join(temp_dir, 'temp_img.jpg')
        utils.save_image(img, temp_file)
        self.assertTrue(os.path.exists(temp_file))
        loaded_img = utils.get_image(temp_file)
        np.testing.assert_almost_equal(img, loaded_img)
