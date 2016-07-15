import sys
import requests
from bs4 import BeautifulSoup
import re

f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')

def handle(query):
    flag = 0
    url = "http://www.merriam-webster.com/dictionary/"
    url = url + query
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src, "lxml")

    results = []
    for info in ob.findAll('p',{'class':'definition-inner-item'}):
        word = info.text
        word = word.split(':')
        for i in word:
            if i.strip():
                flag = 1
                results.append(i.strip())
        break

    if flag==0:
        results.append("No result found")
    return results

query = ""
flag = 0

for arg in sys.argv:
   if flag==1:
      query = arg
      break
   if arg=='of' or arg=='for':
      flag = 1

try:
   ans = handle(query)
   for i in ans:
      f.write(i + "\n")
      print i
except:
   f.write("Something went wrong.")
   print "Something went wrong."

f.close()

