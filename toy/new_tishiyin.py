import tkinter as tk 
import winsound
import time

root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 300, height = 200) 
canvas1.pack()

def helloCallBack():
    time.sleep(5)
    winsound.Beep(600,2000)
    for num in range(1,10):
        winsound.Beep(1000,396)
        winsound.Beep(600,264)  
    winsound.Beep(600,2000)

button1 = tk.Button (root, text='Start', command=helloCallBack) 
canvas1.create_window(100, 100, window=button1) 
      
button2 = tk.Button (root, text='Exit', command=root.destroy) 
canvas1.create_window(200, 100, window=button2) 
    
root.mainloop()