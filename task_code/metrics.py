"""
Metrics
"""

import numpy as np


def pix_to_pix_rmse(img1, img2):
    """
    Calculates pixel-wise RMSE between two images.
    :param img1: 2D numpy array
    :param img2: 2D numpy array
    :return: float, pixel-wise RMSE
    """
    error = img1.flatten() - img2.flatten()
    square_error = np.multiply(error, error)
    mean_square_error = square_error.mean()
    return np.sqrt(mean_square_error)
