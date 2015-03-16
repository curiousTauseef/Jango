#Extract information from wiki 
#Developed by Rahul Arora
print "Initializing search module..."

import os
import re
import wikipedia

f2 = open('query.txt','r')

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

check = f2.readline()
f2.close()

f = open('say.txt','w')
flag = 0

try:
   info =  wikipedia.summary(check, sentences=3)
except wikipedia.exceptions.DisambiguationError:
   info = None
   f.write("Try to be more specific")
   flag=1
except wikipedia.exceptions.PageError:
   info = None
   f.write("No result found!!")
   flag=1

if flag!=1:
   info = re.sub(r'\([^)]*\)',' ',info)
   info = strip_non_ascii(info)

   try:   
      f.write(info)    
   except UnicodeEncodeError:
      pass

f.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
os.remove("query.txt")
