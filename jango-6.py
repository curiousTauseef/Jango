#Extract latest jokes information
#Developed by Rahul Arora
print "Initializing jokes script..."

import requests
from bs4 import BeautifulSoup
import os

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

f = open('say.txt','w')
url = "http://www.ajokeaday.com/ChisteAlAzar.asp?"

page = requests.get(url)
src = page.text
ob = BeautifulSoup(src)

for info in ob.findAll('div',{'class':'chiste'}):
   joke = info.text
   joke = strip_non_ascii(joke)
   joke.replace('.',' ')
   f.write(joke)
   
f.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove('say.txt')
