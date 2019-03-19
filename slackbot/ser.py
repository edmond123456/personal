""" https://blog.csdn.net/JasonTang1992/article/details/59716319 
https://os.mbed.com/users/yamato/notebook/serial/
"""


import serial
ser = serial.Serial('COM4', 115200)  # open serial port
while True:
    if ser.isOpen():
        #data = ser.read()
        data = ser.read(5)
        print (data)
    else:
        break