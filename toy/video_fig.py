###   https://blog.csdn.net/huanglu_thu13/article/details/52337013
###    https://blog.csdn.net/liuweiyuxiang/article/details/80591640


import cv2  
import numpy
import matplotlib.pyplot as plot

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('/Users/junjie_hua/onedrive/OneDrive - Maeda Laboratory/Pepper/ICAT2018/Teaser_Video/20181016.mp4')


while(1):
    # get a frame
    ret, frame = cap.read()
    #rectangle
    cv2.rectangle(frame,(0,0),(200,200),(0,255,0),3)
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 