#Extract latest movies products
#Developed by Rahul Arora
print "Initializing movies module..."

import requests
from bs4 import BeautifulSoup
import os

f = open('say.txt','w')

ctr = 0

f.write("Movies showing now are;\n")
while ctr!=2:
   url = "http://timescity.com/delhi/movies/hindi-language/"
   if ctr==1:
      url = "http://timescity.com/delhi/movies/hindi-language/?pg=2"
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src)
   for info,info2 in zip(ob.findAll('h3',{'class','srch_hdng'}),ob.findAll('span',{'class':'NowshowingBtn flags f_now_showing '})):
      name = info.text
      name = name.strip()
      date = info2.text
      if name=='Map':
         continue
      if date!='Now Showing':
         break
      f.write(name + ";\n")
   ctr += 1

ctr = 0

f.close()
os.system("festival --tts say.txt")
os.system("python jango-write.py &")
os.remove("say.txt")


