"""
Runs on given dataset, calculates RMSE for jpg and bmp images.

(runs ~8 sec, MEAN RMSE is 1.65)
"""

import numpy as np
import os
import pandas as pd

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
all_img_rmse = pd.DataFrame(columns=['image_name', 'pixelwise_rmse'])
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
    all_img_rmse = all_img_rmse.append(pd.Series(data={'image_name': fname, 'pixelwise_rmse': img_rmse}), ignore_index=True)
    print('=== {}/{} - {}, RMSE - {:.3f} ==='.format(img_ix, unique_img_num, fname, img_rmse))

mean_rmse = all_img_rmse['pixelwise_rmse'].mean()
print('=== FINISHED, MEAN RMSE is {:.3f} ==='.format(mean_rmse))
all_img_rmse = all_img_rmse.append(pd.Series(data={'image_name': 'total', 'pixelwise_rmse': mean_rmse}), ignore_index=True)

all_img_rmse.to_csv('baseline_rmse.csv', index=False)

