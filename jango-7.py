#Extract latest words information
#Developed by Rahul Arora
print "Initializing vocabloury script..."

import requests
from bs4 import BeautifulSoup
import os
import re

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


f = open('say.txt','w')
url = "http://www.merriam-webster.com/word-of-the-day/"

page = requests.get(url)
src = page.text
ob = BeautifulSoup(src)

f.write("Word is; ")
for info in ob.findAll('strong',{'class':'main_entry_word'}):
   word = info.text
   f.write(word + ";\n")
   break

f.write("Meaning is; ")
for info in ob.findAll('span',{'class':'ssens'}):
   word = info.text
   word = strip_non_ascii(word)
   word = re.sub(r'\([^)]*\)',' ',word)
   try:
      f.write(word + ";\n")
      break
   except UnicodeEncodeError:
      pass  
   
f.write("Example is; ")
for info in ob.findAll('p',{'class':'word_example_didu'}):
   word = info.text
   word = strip_non_ascii(word)
   try:
      f.write(word + ";\n")
      break
   except UnicodeEncodeError:
      pass  

f.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove('say.txt')
