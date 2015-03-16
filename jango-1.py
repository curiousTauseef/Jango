#Extract latest news information
#Developed by Rahul Arora
print "Initializing news module..."

import requests
from bs4 import BeautifulSoup
import time
import os

f = open('say.txt','w')
url = "http://www.ndtv.com/"

page = requests.get(url)
src = page.text
ob = BeautifulSoup(src)

for news in ob.findAll('a',{'class':'item-title'}):
   try:   
      info = news.text
      info.replace('.',';')
      f.write(info)
      f.write("....;\n")      
   except UnicodeEncodeError:
      pass

f.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
   
