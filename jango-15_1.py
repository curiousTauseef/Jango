#Child process of jango-15.py
#Developed by Rahul Arora

import pynotify
import time
import os

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

f= open('timer.txt','r')
tot = f.readline()
tot = int(tot)
temp = f.readline()

time.sleep(tot)
sendmessage('Timer Alert!!',temp )
os.system("/usr/bin/canberra-gtk-play --id='phone-outgoing-busy'")

f.close()
try:
   os.remove('timer.txt')
except OSError:
   pass
