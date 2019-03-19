
"""
 https://www.youtube.com/watch?v=cuKQ9w9nr1o
https://api.slack.com/methods/chat.postMessage/test
https://api.slack.com/apps/AH25TSLQ4/general

"""

import requests
import json
import time
import serial
ser = serial.Serial('COM4', 115200)  # open serial port

web_hook_url = 'https://hooks.slack.com/services/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'

slack_msg ={'text': ' test from python'}
while True:
    if ser.isOpen():
        #data = ser.read()
        data = ser.read(5)
        if data == b'\x00\x00\x00\x00\x00':
            print("yes")
            #requests.post(web_hook_url,data=json.dumps(slack_msg))
        time.sleep()
    else:
        break
