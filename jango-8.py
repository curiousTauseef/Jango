#Extract flipkart products
#Developed by Rahul Arora
print "Initializing flipkart module..."

import requests
from bs4 import BeautifulSoup
import os

f = open('query.txt','r')
f2 = open('say.txt','w')

def check(k):
    flag=0
    ctr=0
    url = "http://www.flipkart.com/search?q=" + str(k) + "&as=off&as-show=on&otracker=start"
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)

    for find,find2 in zip(ob.findAll('a',{'class':'lu-title'}),ob.findAll('div',{'class':'pu-final fk-font-17 fk-bold'})):
      if flag==0:
         f2.write("Top ten products are;\n")
         flag=1
      title = find.text
      f2.write(title + ";\n")
      price = find2.text
      price = price.replace('Rs.','Rupees')
      f2.write(price.strip() + ";\n")
      ctr += 1
      if ctr==10:
         break
      
    if flag!=1:
      f2.write("Exact match not found;\n") 
      f2.write("Similar Top three products are;\n")
      for temp,temp2 in zip(ob.findAll('div',{'class':'pu-final'}),ob.findAll('a',{'class':'fk-display-block'})): 
         price = temp.text
         title = temp2.text
         f2.write(title + ";\n")
         price = price.replace('Rs.','Rupees')
         f2.write(price.strip() + ";\n")
         ctr += 1
         if ctr==3:
            break

word = f.readline()
check(word)
f.close()
f2.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove("say.txt")
os.remove("query.txt")
