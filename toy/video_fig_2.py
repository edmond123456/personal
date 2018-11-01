### 视频中添加图片 但是延迟很高

import cv2  
import numpy as np
import os
import PIL
from PIL import Image
 
cap = cv2.VideoCapture(0) 
c = 0
 
#加载需要P上去的图片
tmp_img = Image.open('/Users/junjie_hua/personal/toy/mark.png')
#这里可以选择一块区域或者整张图片
#region = tmp_img.crop((0,0,304,546)) #选择一块区域
#或者使用整张图片
region = tmp_img
box = (166, 64, 320, 337)  # 底图上需要P掉的区域
region = region.resize((box[2] - box[0], box[3] - box[1]))

while (1):    
    c = c + 1  
    ret, frame = cap.read()
    cv2.imwrite('/Users/junjie_hua/personal/toy/frame.png', frame)
    # open frame
    base_img  = Image.open('/Users/junjie_hua/personal/toy/frame.png')
    
    base_img.paste(region, box)
    #base_img.show() # 查看合成的图片
    base_img.save('/Users/junjie_hua/personal/toy/out.png') #保存图片
    image = cv2.imread('/Users/junjie_hua/personal/toy/out.png') 
    # show processed frame
    cv2.imshow("capture", image)
    # remove saved file
    os.remove('/Users/junjie_hua/personal/toy/frame.png')
    os.remove('/Users/junjie_hua/personal/toy/out.png')
    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
 
cap.release()
cv2.destroyAllWindows()  






