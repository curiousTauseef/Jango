import requests
from bs4 import BeautifulSoup
import json

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')

while 1:
   url = "http://api.icndb.com/jokes/random"
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, "lxml")

   parsed = json.loads(src)

   joke = parsed['value']['joke']

   joke = joke.replace('Chuck Norris','RajniKant')
         
   if len(joke)<=100:
      f.write(joke)
      print joke
      break
   else:
      continue
      
f.close()