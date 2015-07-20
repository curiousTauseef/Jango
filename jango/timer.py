import jangopath
import os

def handle():
   time = raw_input("Enter time(HH:MM:SS) : ")
   time = time.split(":")
   hour = int(time[0])
   minute = int(time[1])
   second = int(time[2])
   hour = hour*3600
   minute = minute*60
   total = hour + minute + second
   path = jangopath.MODULE_PATH + "/timer_helper.py"
   os.system("python " + path + " " + str(total) + " & " )

handle()
