from flask import Flask, request
from flask import render_template
from jinja2 import Markup
from brain import Brain
import note
import re

Make_Notes = 0
Internet_Check = 0

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def start():
   global Make_Notes, internet_Check
   if request.method=='GET':
      res = ""
      return render_template('test.html',res=res)
   else:
      brain = Brain()
      query = request.form['url']
      if bool(re.search('make', query, re.IGNORECASE))==True or bool(re.search('write', query, re.IGNORECASE))==True:
         Make_Notes = 1
         return render_template('test.html',res="What shall I note down?")
      if Make_Notes==1:
         Make_Notes=0
         note.handle(query)
      else:
        brain.query(query)
      f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','r')
      res = ""
      line = ""
      while True:
   		line = f.readline()
   		if line:
   			res = res+line
   		else:
   			break
      f.close()
      res = strip_non_ascii(res)
      res = res.replace('\n','')
      res = Markup(res)
      if bool(re.search('search', query, re.IGNORECASE))==True:
         print "1"
         return render_template('test.html',res=res)
      else:
         print "2"
         return render_template('test.html',res2=res)

if __name__ == '__main__':
    app.run(debug=True)