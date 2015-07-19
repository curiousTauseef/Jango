import urllib
import json

url = "http://tambal.azurewebsites.net/joke/random"

def handle():
   try:
      data = json.loads(urllib.urlopen(url).read())
      print data['joke']
   except:
      print "Something went wrong."

handle()
