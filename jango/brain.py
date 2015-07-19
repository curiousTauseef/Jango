import re
import os
import jangopath

WORDS = {1:"USEFUL", 2:"JOKE", 3:"MEANING", 4:"WEATHER", 5:"NOTE", 6:"SEARCH", 7:"SOLVE", 8:"MAIL", 9:"DATE", 10:"TIME", 11:"DAY"}
MODULES = {1:"/intro.py", 2:"/joke.py", 3:"/mean.py", 4:"/weather.py", 5:"/note.py", 6:"/search.py", 7:"/solve.py", 8:"/mail.py", 9:"/date.py", 10:"/time.py", 11:"/day.py"}

class Brain(object):
   def isValid(self, text, word):
      return bool(re.search(word, text, re.IGNORECASE))   

   def query(self,text):
      for i in WORDS.keys():
         if self.isValid(text, WORDS[i]):
            path = jangopath.MODULE_PATH+ MODULES[i]
            try:
               os.system("python " + path + " " + text)
            except:
               print "Something went wrong."
            return      
      print "No module could handle this."
            

