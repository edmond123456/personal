import winsound
import time
import tkinter as tk 


file0 = "C:/Users/saku_/Documents/GitHub/personal/toy/oped.wav"
file1 = "C:/Users/saku_/Documents/GitHub/personal/toy/new1.wav"
file2 = "C:/Users/saku_/Documents/GitHub/personal/toy/new2.wav"



root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 300, height = 200) 
canvas1.pack()

def helloCallBack():
    time.sleep(5)
    winsound.PlaySound(file0,winsound.SND_FILENAME|winsound.SND_NOWAIT,)
    for num in range(1,10):
        winsound.PlaySound(file1,winsound.SND_FILENAME|winsound.SND_NOWAIT,)
        winsound.PlaySound(file2,winsound.SND_FILENAME|winsound.SND_NOWAIT,)
    winsound.PlaySound(file0,winsound.SND_FILENAME|winsound.SND_NOWAIT,)

button1 = tk.Button (root, text='Start', command=helloCallBack) 
canvas1.create_window(100, 100, window=button1) 
      
button2 = tk.Button (root, text='Exit', command=root.destroy) 
canvas1.create_window(200, 100, window=button2) 
    
root.mainloop()