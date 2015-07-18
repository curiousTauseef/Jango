import re
import os
import jangopath

WORDS = {1:"DATE", 2:"TIME", 3:"DAY", 4:"JOKE", 5:"MEANING"}
MODULES = {1:"/date.py", 2:"/time.py", 3:"/day.py", 4:"/joke.py", 5:"/mean.py"}

class Brain(object):
   def isValid(self, text, word):
      return bool(re.search(word, text, re.IGNORECASE))   

   def query(self,text):
      for i in WORDS.keys():
         if self.isValid(text, WORDS[i]):
            path = jangopath.MODULE_PATH + MODULES[i]
            os.system("python " + path + " " + text)
            return      
      print "No module could handle this."
            

