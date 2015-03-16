#Extract current date
#Developed by Rahul Arora
print "Initializing date module..."

import time
import os

f = open('say.txt','w')

localtime = time.asctime( time.localtime(time.time()) )
date = localtime.split()
f.write('Current date is    ')
f.write(date[1] + ' ' + date[2] + ' ' + date[4])

f.close() 
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
