import ConfigParser
import os
from modules import jangopath, start, conversation, brain, internet

os.system('clear')

Config = ConfigParser.ConfigParser()

class Jango(object):
   def __init__(self):
      if not os.path.exists(jangopath.CONFIG_PATH):
         try:
            start.add_name()   
         except:
            print "Some Error occured while creating config file."

   def run(self):
      if not internet.connection():
         print "Internet connection not working fine."
      try:
         Config.read(jangopath.CONFIG_PATH)
      except:
         print "Couldn't read config file."
      
      try:
         name = Config.get('Person', 'name')
         print "What can I do for you, %s?" % name 
      except:
         print "What can I do for you?"

      conversation.handleForever()
               

print "*******************************************************"
print "*             JANGO - PERSONAL ASSISTANT              *"
print "*******************************************************"
app = Jango()
app.run()
