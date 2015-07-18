import requests
from bs4 import BeautifulSoup
import random

url = "http://www.ajokeaday.com/ChisteAlAzar.asp?"

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def handle():
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, 'lxml')
   for info in ob.findAll('div',{'class':'chiste'}):
         joke = info.text.strip()
         joke = strip_non_ascii(joke)
         print joke
         return

handle()
