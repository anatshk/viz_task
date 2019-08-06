"""
Utils file
"""
from imageio import imread, imwrite
import numpy as np


def get_image(path_to_image):
    return np.asarray(imread(path_to_image))


def save_image(img, path_to_image):
    imwrite(path_to_image, img)
    # FIXME: the test fails - img --> save --> load --> loaded image, the loaded images is not identical to saved.

