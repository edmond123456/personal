###   https://blog.csdn.net/m0_37606112/article/details/78289802


import cv2
import numpy as np

# 选取摄像头，0为笔记本内置的摄像头，1,2···为外接的摄像头**
cap = cv2.VideoCapture(0)

#定义摄像头的分辨率
#cap.set(3,1080)
#cap.set(4,720)

#大量的错和坑出现在这里
#第一个参数是路径和文件名
#第二个参数是视频格式，“MPEG”是一**种标准格式，百度fourcc可见各种格式
#第二个参数（fourcc）如果设置为-1，允许实时选择视频格式
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc=-1**

# 第三个参数则是镜头快慢的，20为正常，小于二十为慢镜头**
#out = cv2.VideoWriter('/Users/junjie_hua/personal/toy/test_video_audio.avi',fourcc,20,(1080,720))
#out = cv2.VideoWriter('/Users/junjie_hua/onedrive/OneDrive - Maeda Laboratory/test_video_audio.avi',fourcc,20,(640,480))
#out = cv2.VideoWriter('C:/Users/saku_/Documents/GitHub/personal/toy/test_video_audio.avi',fourcc,20,(640,480))
out = cv2.VideoWriter('C:/Users/saku_/Documents/GitHub/personal/toy/test_video_audio.avi',fourcc,20,(640,480))

while True:

    ret,frame = cap.read()  # 获取图像
    if ret == True:
        frame = cv2.flip(frame, 1)# 在帧上进行操作

        cv2.imshow("frame", frame)  # 显示帧

        out.write(frame) # 保存视频

        #if cv2.waitKey(1) == ord('s'):  #按下‘s’保存图片
        #    print('save photo\n')
        #    cv2.imwrite("/Users/junjie_hua/personal/toy/test_fig.png",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):#按下‘q’退出
            print('quit\n')
            break
    else:
        break
# 释放摄像头资源
cap.release()
out.release()
cv2.destroyAllWindows()
