import cv2
import sys
import os

img_path = 'C:/Users/Hayato/Documents/GitHub/personal/thermal_illusion/test_figure.tiff'

img_list = os.listdir(img_path)

for img_name in img_list:
    if '.tiff' in img_name:
        #保持不变读取
        img = cv2.imread(os.path.join(img_path, img_name), -1)
        print('non-transform reading')
        print(img.dtype)
        print(img.shape)
        #默认读取方式
        img = cv2.imread(os.path.join(img_path, img_name))
        print('transform reading')
        print(img.dtype)
        print(img.shape)
    if '.jpg' in img_name:
        #上述文件保存为jpg后读取
        img = cv2.imread(os.path.join(img_path, img_name), -1)
        print(img.dtype)
        print(img.shape)