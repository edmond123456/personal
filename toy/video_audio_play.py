# -*- coding: utf-8 -*-
 

###  https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
###  python C:\Users\saku_\Documents\GitHub\personal\toy/video_audio_play.py
 
import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('C:/Users/saku_/Documents/GitHub/personal/toy/test_video_audio.avi')
cv2.namedWindow("[Frame]") 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.moveWindow('Frame',0,0)
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
