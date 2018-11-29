import winsound
import time


time.sleep(5)
winsound.Beep(600,2000) # winsound.Beep(frequency, duration)
time.sleep(2)

for num in range(1,10):
    winsound.Beep(600,2000)
    time.sleep(2)
    winsound.Beep(800,2000)
    winsound.Beep(600,2000)

winsound.Beep(600,4000)
