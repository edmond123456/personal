###   https://blog.csdn.net/huanglu_thu13/article/details/52337013
###    https://blog.csdn.net/liuweiyuxiang/article/details/80591640
### https://qiita.com/neriai/items/448a36992e308f4cabe2



import cv2  
import numpy
import matplotlib.pyplot as plot

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('/Users/junjie_hua/onedrive/OneDrive - Maeda Laboratory/Pepper/ICAT2018/Teaser_Video/20181016.mp4')


while(1):
    # get a frame
    ret, frame = cap.read()
    # convert image to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # threshold for image, with threshold 50. 超えなかった場合は、黒いピクセルに置き換える
    _, threshold_img = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)
    _, contours, _= cv2.findContours(threshold_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # 各輪郭に対する処理
    for i in range(0, len(contours)):

        # 輪郭の領域を計算
        area = cv2.contourArea(contours[i])

        # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
        if area < 1e3 or 1e5 < area:
            continue

        # 外接矩形
        if len(contours[i]) > 0:
            rect = contours[i]
            x, y, w, h = cv2.boundingRect(rect)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 