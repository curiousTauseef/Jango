#Extract current day
#Developed by Rahul Arora
print "Initializing day module..."

import time
import os

f = open('say.txt','w')

localtime = time.asctime( time.localtime(time.time()) )
date = localtime.split()

f.write('Current day is    ')
f.write(date[0] + "day")
f.close()

os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
