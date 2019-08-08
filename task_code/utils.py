"""
Utils file
"""
import pickle
from imageio import imread, imwrite
import numpy as np
from sklearn.feature_extraction import image


def get_image(path_to_image):
    return np.asarray(imread(path_to_image))


def save_image(img, path_to_image):
    imwrite(path_to_image, img)
    # FIXME: the test fails - img --> save --> load --> loaded image, the loaded images is not identical to saved.


def extract_patches(img, patch_size):
    """
    Extracts patches from img.
    Note: patches can overlap. but for exercise purpose, we'll deal with non-overlapping patches.
    :param img: 2D numpy array
    :param patch_size: int > 0
    :return: 3D numpy array, total patch number X patch_size X patch_size
    """
    return image.extract_patches_2d(img, patch_size=(patch_size, patch_size))


def save_to_pkl(pth, **vars):
    with open(pth, 'wb') as f:
        pickle.dump(vars, f)
    print('saved to {}'.format(pth))


def load_from_pkl(pth):
    with open(pth, 'rb') as f:
        return pickle.load(f)
