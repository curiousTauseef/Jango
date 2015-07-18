import re
import os
import jangopath

WORDS = {1:"USEFUL", 2:"DATE", 3:"TIME", 4:"DAY", 5:"JOKE", 6:"MEANING", 7:"WEATHER", 8:"NOTE", 9:"SEARCH"}
MODULES = {1:"/intro.py", 2:"/date.py", 3:"/time.py", 4:"/day.py", 5:"/joke.py", 6:"/mean.py", 7:"/weather.py", 8:"/note.py", 9:"/search.py"}

class Brain(object):
   def isValid(self, text, word):
      return bool(re.search(word, text, re.IGNORECASE))   

   def query(self,text):
      for i in WORDS.keys():
         if self.isValid(text, WORDS[i]):
            path = jangopath.MODULE_PATH + MODULES[i]
            try:
               os.system("python " + path + " " + text)
            except:
               print "Something went wrong."
            return      
      print "No module could handle this."
            

