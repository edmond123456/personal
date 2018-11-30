import winsound
import time


time.sleep(5)
winsound.Beep(600,2000) # winsound.Beep(frequency, duration)
print ("start")
#time.sleep(2)
#localtime = time.asctime( time.localtime(time.time()) )
#print ("local time is :", localtime)

for num in range(1,10):
    winsound.Beep(1000,396)
    #print ("on")
    #time.sleep(2)
    winsound.Beep(600,264)
    #print ("off")
    #time.sleep(2)

#localtime = time.asctime( time.localtime(time.time()) )
#print ("local time is :", localtime)
winsound.Beep(600,2000)
print ("end")