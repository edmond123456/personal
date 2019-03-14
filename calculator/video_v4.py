import sys
import tkinter as tk 
import time
import cv2
import numpy as np


if sys.platform == "win64":
    width=1980
    height=1020
else:
    width=640 
    height=480



root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 400, height = 200) 
canvas1.pack()

def video_audio_record():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("[frame]") 
    cap.set(cv2.CAP_PROP_FPS, 60)           # set up the fps of the camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width) # set up the width of the camera
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height) # set up the height of the camera
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('/test_video_audio.avi',fourcc,20,(width,height))
    #counter = 1
    #timer_start = time.time()
    #timer_current = 0

    while True:
        ret,frame = cap.read()  # capture
        if ret == True:
            cv2.moveWindow('frame',0,0)  #open the window on the upper-left
            cv2.imshow("frame", frame)  # show the image
            out.write(frame) # save
            #counter += 1
            #timer_current = time.time() - timer_start
            if cv2.waitKey(1) & 0xFF == ord('q'):  #press "q"to quit
                #print('quit\n')
                break
        else:
            break
    # release caps
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    #print (counter)
    #print (timer_current)
    #print ('fps: ',counter/timer_current)   #my pc is 16fps


def video_audio_replay():
    cap0 = cv2.VideoCapture(0)
    cv2.namedWindow("[frame]") 
    #timer_start = time.time()
    #timer_current = 0
    while(cap0.isOpened()):
        ret,frame = cap0.read()  # capture 
        if ret == True:
            cv2.moveWindow('frame',0,0)  #open the window on the upper-left
            cv2.imshow("frame", frame)  # show the image
            time.sleep(0.054)
            #timer_current = time.time() - timer_start
            if cv2.waitKey(1) & 0xFF == ord('s'):  #press "s"to replay mode
                cap0 = cv2.VideoCapture('/test_video_audio.avi')
            elif cv2.waitKey(1) & 0xFF == ord('q'):  #press "q"to quit
                break
        else:
            cap0 = cv2.VideoCapture(0)
    cap0.release()
    cv2.destroyAllWindows()
    #print (timer_current)

   

button1 = tk.Button (root, text='Experiment 1', command=video_audio_record) 
canvas1.create_window(70, 100, window=button1) 

button2 = tk.Button (root, text='Experiment 2', command=video_audio_replay) 
canvas1.create_window(200, 100, window=button2) 
      
button3 = tk.Button (root, text='Exit', command=root.destroy) 
canvas1.create_window(300, 100, window=button3) 
    
root.mainloop()