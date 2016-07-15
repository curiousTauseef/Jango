import re
import wikipedia
import sys

flag = 0
query = ""
f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')

for arg in sys.argv:
   if flag==1:
      query = query + arg + " "
   if arg.lower()=="for" or arg.lower()=="about":
      flag = 1

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def handle():
   flag = 0
   try:
      info =  wikipedia.summary(query, sentences=3)
   except wikipedia.exceptions.DisambiguationError:
      info = None
      f.write("Try to be more specific.")
      print "Try to be more specific."
      flag = 1
   except wikipedia.exceptions.PageError:
      info = None
      f.write("No result found!!")
      print "No result found!!"
      flag = 1

   if flag!=1:
      info = re.sub(r'\([^)]*\)',' ',info)
      info = strip_non_ascii(info)
      try:   
         f.write(info)
         print info    
      except UnicodeEncodeError:
         pass
   f.close()

handle()
