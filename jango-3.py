#Extract current time
#Developed by Rahul Arora
print "Initializing time module..."

import time
import os

f = open('say.txt','w')

localtime = time.asctime( time.localtime(time.time()) )
date = localtime.split()

f.write('Current time is    ')
f.write(date[3])
f.close()

os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
