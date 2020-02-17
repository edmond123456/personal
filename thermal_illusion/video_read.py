from PIL import Image
import cv2
import sys
import os
import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import cm

#img = Image.open('C:/Users/saku_/Documents/GitHub/personal/thermal_illusion/test_video.tiff')
img = Image.open('C:/Users/Hayato/Documents/GitHub/personal/thermal_illusion/test_video.tiff')

for i in range(87):
    try:
        img.seek(i)
        #img.save('C:/Users/saku_/Documents/GitHub/personal/thermal_illusion/frames/'+'%s.tif'%(i,))
        img.save('C:/Users/Hayato/Documents/GitHub/personal/thermal_illusion/frames/'+'%s.tif'%(i,))
    except EOFError:
        break
print("split ended")



#img_path = 'C:/Users/saku_/Documents/GitHub/personal/thermal_illusion/frames/'
#img_list = os.listdir(img_path)
#img_trans_path = "C:/Users/saku_/Documents/GitHub/personal/thermal_illusion/frames_trans/"

img_path = 'C:/Users/Hayato/Documents/GitHub/personal/thermal_illusion/frames/'
img_list = os.listdir(img_path)
img_trans_path = "C:/Users/Hayato/Documents/GitHub/personal/thermal_illusion/frames_trans/"

for img_name in img_list:
    if '.tif' in img_name:
        print(img_name)
        #保持不变读取
        img = cv2.imread(os.path.join(img_path, img_name), -1)
        #print('non-transform reading')
        #print(img.dtype)
        #print(img.shape)
        #默认读取方式
        #img = cv2.imread(os.path.join(img_path, img_name))
        #print('transform reading')
        #print(img.dtype)
        #print(img.shape)
        img_trans = img/100 -273.15
        plt.imshow(img_trans, cmap=cm.plasma,vmin=20,vmax=45) 
        pp = plt.colorbar(orientation= "vertical")
        plt.axis([0,79,0,59])
        #plt.show()
        plt.savefig(img_trans_path + img_name + ".png")
        plt.close()

        
print("convert ended")



