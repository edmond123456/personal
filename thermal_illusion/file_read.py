import cv2
import sys
import os
import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import cm

#img_path = 'C:/Users/saku_/Documents/GitHub/personal/thermal_illusion/'
img_path = 'C:/Users/Hayato/Documents/GitHub/personal/thermal_illusion/'


img_list = os.listdir(img_path)

for img_name in img_list:
    if '.tiff' in img_name:
        print(img_name)
        #保持不变读取
        img = cv2.imread(os.path.join(img_path, img_name), -1)
        print('non-transform reading')
        #print(img.dtype)
        #print(img.shape)
        #默认读取方式
        #img = cv2.imread(os.path.join(img_path, img_name))
        #print('transform reading')
        #print(img.dtype)
        #print(img.shape)
    
"""
figure read succeeded!
"""

img_trans = img/100 -273.15
plt.imshow(img_trans, cmap=cm.plasma,vmin=20,vmax=45) 
pp = plt.colorbar(orientation= "vertical")
plt.axis([0,79,0,59])
plt.show()