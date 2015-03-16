#Shows reminder from the reminders list
#Developed by Rahul Arora

import pynotify
import os
import time
import string

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

f = open('reminder.txt','r')

while True:
   check = f.readline()
   time.sleep(10)
   if not check:
      f.close()
      f = open('reminder.txt','r')
   else:
      temp = check.split()
      for i in range(0,len(temp)):
         if temp[i]=='at':
            num = int(temp[i+1])
            mod = temp[i+2]
            break
      if mod=='pm':
         num = 1200 + num
         num = str(num)
      elif mod=='am':
         num = str(num)
         num = "0" + num
      
      fin = num[:2] + ":" + num[-2:] + ":00"  
      localtime = time.asctime( time.localtime(time.time()) )
      date = localtime.split()
      fin2 = date[3]
      fin2 = fin2[:2] + ":" + fin2[-5:-3] + ":00"  
      
      if fin==fin2:
         os.system("/usr/bin/canberra-gtk-play --id='phone-outgoing-busy'")
         temp = check.split()     
          
         for j in range(0,len(temp)):
            if temp[j]=='at':
               for k in range(j,len(temp)):
                  temp[k] = ' '
         temp = string.join(temp)
         temp = temp.strip() 
         sendmessage("Reminder",temp)
         time.sleep(20)
     


