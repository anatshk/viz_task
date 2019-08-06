"""
Runs on given dataset, calculates RMSE for jpg and bmp images.

(runs ~8 sec, MEAN RMSE is 1.65)
"""

import numpy as np
import os

from task_code.metrics import pix_to_pix_rmse
from task_code.utils import get_image

# define path to data (extracted images)
PATH_TO_DATA = r'C:\Users\Anat\Downloads\viz'
if not os.path.exists(PATH_TO_DATA):
    # support for Google colab Drive mapping
    PATH_TO_DATA = '/content/drive/My Drive/Viz'

# get a list of all file names
all_files = os.listdir(PATH_TO_DATA)
unique_img_num = len(all_files) // 2

# go over files, load bmp and jpg, calculate rmse
all_img_rmse = np.empty((unique_img_num,))
for file_ix in range(0, len(all_files), 2):
    img_ix = file_ix // 2
    fname = all_files[file_ix][:-4]
    if 'slice' not in fname:
        continue
    jpg = os.path.join(PATH_TO_DATA, fname + '.jpg')
    bmp = os.path.join(PATH_TO_DATA, fname + '.bmp')
    jpg_img = get_image(jpg)
    bmp_img = get_image(bmp)
    img_rmse = pix_to_pix_rmse(bmp_img, jpg_img)
    all_img_rmse[img_ix] = img_rmse
    print('=== {}/{} - {}, RMSE - {} ==='.format(img_ix, unique_img_num, fname, img_rmse))

print('=== FINISHED, MEAN RMSE is {:.2f} ==='.format(all_img_rmse.mean()))

