# -*- coding: utf-8 -*-

import textrazor
import wolframalpha
import re
import sys
import jangopath



def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

app_id_textrazor = "b5f5ad018717f7128f86e4f3e7c33cca047f360a407cafe062c2464c"
app_id_wolframalpha = "YTVEWP-QUTUQR68AP"
flag = 0
query = ""

for arg in sys.argv:
   query = query + arg + " "

query = str(query.split(jangopath.HOME_DIR + "/last.py")[1]).strip()

wclient = wolframalpha.Client(app_id_wolframalpha)
textrazor.api_key = app_id_textrazor

tclient = textrazor.TextRazor(extractors=["entities"])

res = wclient.query(query)

f = open(jangopath.HOME_DIR + '/ans.txt','w')

for pod in res.pods:
    #For Facts 
    if pod.title=="Result" or pod.title=="Current result" or pod.title=="Approximate result" or pod.title=="Results" or pod.title=="Average result":
        print pod.text
        mid = pod.text
        mid = mid.replace('\\xc3','X')
        mid = strip_non_ascii(pod.text)
        f.write(mid + "\n")
        flag = 1
    if pod.title=="Value":
        ans = pod.text.split("\n")
        print ans[0]
        ans[0] = strip_non_ascii(ans[0])
        f.write(ans[0] + "\n")
        flag = 1
    #For Morse
    if pod.title=="Morse code translation":
        print pod.text
        mid = strip_non_ascii(pod.text)
        f.write(mid + "\n")
        flag = 1
    #For Natural Questions
    if pod.title=="Response":
        print pod.text
        mid = pod.text
        mid = mid.replace('\\xc3','X')
        mid = strip_non_ascii(pod.text)
        f.write(mid + "\n")
        flag = 1

if flag==0:
   response = tclient.analyze(query)

   for entity in response.entities():
       if entity.id.lower()!="jango":
           query = entity.id

   #print query

   res = wclient.query(query)
 
   for pod in res.pods:
       #For People
       if pod.title=="Basic information":
           ans = pod.text.split("\n")
           print ans[0] + "\n" + ans[1] + "\n"
           f.write(ans[0] + "\n" + ans[1] + "\n")
       if pod.title=="Notable facts":
           ans = pod.text.split("\n")
           print "* " + ans[0] + "\n" + "* " + ans[1] + "\n" + "* " + ans[2] + "\n"
           f.write(". " + ans[0] + "\n" + "* " + ans[1] + "\n" + "* " + ans[2] + "\n")

       #For Countries or Places
       if pod.title=="Capital city":
           print "Capital -> " + pod.text
           f.write("Capital -> " + pod.text)
       if pod.title=="Bordering countries/regions":
           print "Bordering countries/regions -> " + pod.text
           f.write("Bordering countries/regions -> " + pod.text)
       if pod.title=="Currency":
           ans = pod.text.split("\n")
           print "Currency -> " + ans[1] + "\n"
           ans[1] = strip_non_ascii(ans[1])
           f.write("Currency -> " + ans[1] + "\n")

f.close()

   

