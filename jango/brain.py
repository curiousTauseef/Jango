import re
import os
import jangopath

WORDS = {1:"INTRO", 2:"JOKE", 3:"LIFE", 4:"WEATHER", 5:"NOTE", 6:"SEARCH", 7:"SOLVE", 8:"MAIL", 9:"SET", 10:"STOP", 11:"MEANING", 12:"DATE", 13:"DAY", 14:"TIME", 15:"SONG", 16:"SAYING"}
MODULES = {1:"/intro.py", 2:"/joke.py", 3:"/life.py", 4:"/weather.py", 5:"/note.py", 6:"/search.py", 7:"/solve.py", 8:"/mail.py", 9:"/timer.py", 10:"/kill.py", 11:"/mean.py", 12:"/date.py", 13:"/day.py", 14:"/Time.py", 15:"/music.py", 16:"/sms.py"}

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
      path = jangopath.MODULE_PATH + "/last.py"     
      os.system("python " + path + " " + text)
      #print "No module could handle this."
            

