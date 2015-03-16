#Extract word meaning products
#Developed by Rahul Arora
print "Initializing Dictionary module..."

import requests
from bs4 import BeautifulSoup
import os

f = open('say.txt','w')
f2 = open('query.txt','r')
check = f2.readline()
check.strip()

url = "http://www.merriam-webster.com/dictionary/" + check

page = requests.get(url)
src = page.text
ob = BeautifulSoup(src)

for info in ob.findAll('div',{'class':'ld_on_collegiate'}):
   word = info.text
   word = word.replace(',',';')
   f.write(word)

f.close()
f2.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
os.remove("query.txt")


