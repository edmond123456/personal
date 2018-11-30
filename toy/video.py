import tkinter as tk 
import time
import cv2
import numpy as np

root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 400, height = 200) 
canvas1.pack()

def video_audio_record():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 60)           # カメラFPSを60FPSに設定
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980) # カメラ画像の横幅を1280に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1020) # カメラ画像の縦幅を720に設定
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('C:/Users/saku_/Documents/GitHub/personal/toy/test_video_audio.avi',fourcc,20,(1920,1080))
    while True:
        ret,frame = cap.read()  # 获取图像
        if ret == True:
            cv2.imshow("frame", frame)  # 显示帧
            out.write(frame) # 保存视频
            if cv2.waitKey(1) & 0xFF == ord('q'):#按下‘q’退出
                print('quit\n')
                break
        else:
            break
    # 释放摄像头资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def video_audio_replay():
    cap = cv2.VideoCapture('C:/Users/saku_/Documents/GitHub/personal/toy/test_video_audio.avi')
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()

button1 = tk.Button (root, text='Record', command=video_audio_record) 
canvas1.create_window(100, 100, window=button1) 

button2 = tk.Button (root, text='Replay', command=video_audio_replay) 
canvas1.create_window(200, 100, window=button2) 
      
button3 = tk.Button (root, text='Exit', command=root.destroy) 
canvas1.create_window(300, 100, window=button3) 
    
root.mainloop()