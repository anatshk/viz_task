from task_code import metrics
import numpy as np


import unittest


class TestMetrics(unittest.TestCase):
    def test_pix_to_pix_rmse_sanity(self):
        img1 = np.array([[1, 2], [0, -8]])
        img2 = np.array([[0, 6], [0, 4]])
        expected_rmse = np.sqrt(np.mean([(1 - 0)**2, (2 - 6)**2, (0 - 0)**2, (-8 - 4)**2]))
        self.assertEqual(expected_rmse, metrics.pix_to_pix_rmse(img1, img2))
