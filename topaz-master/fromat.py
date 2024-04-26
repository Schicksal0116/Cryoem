import os
import mrcfile
import numpy as np
from PIL import Image

def convert_mrc_to_jpg(mrc_path, jpg_path):
    with mrcfile.open(mrc_path, permissive=True) as mrc:
        img_data = mrc.data
        if img_data.ndim > 2:
            img_data = img_data[0] 

        # 转换数据范围到0-255并转换为uint8
        img_data_normalized = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data))
        img_uint8 = (img_data_normalized * 255).astype(np.uint8)
        img = Image.fromarray(img_uint8)
        img.save(jpg_path)

def convert_all_mrc_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.mrc'):
            mrc_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename.replace('.mrc', '.jpg'))
            convert_mrc_to_jpg(mrc_path, jpg_path)
            print(f'Converted {mrc_path} to {jpg_path}')

# 指定包含.mrc文件的目录
directory = 'tutorial/data/EMPIAR-10016/denoised'
convert_all_mrc_to_jpg(directory)
