#Add a calender event
#Developed by Rahul Arora
print "Initializing calender script..."

import os
import string
import datetime

f = open('cal.txt','a')
days = {"monday","tuesday","wednesday","thursday","friday","saturday","sunday"}
months = ["january","february","march","april","may","june","july","August","september","october","november","december"]
new = []
date = []
flag = 0
day = 0

f2 = open('say.txt','w')
f2.write("What would you like to add?;")
f2.close()
os.system("festival --tts say.txt")

check = raw_input()
temp = check.split()

for i in range(0,len(temp)):
   if temp[i]=='today' or temp[i]=='tommorrow' or temp[i]=='tonight':
      flag = 1
      break

if flag!=1:
   for i in range(0,len(temp)-1):
      if temp[i+1] in days:
         if temp[i]!='on':
            new.append(temp[i])
            new.append("on")
         else:
            new.append("on")
      else:
         new.append(temp[i])

   new.append(temp[i+1])

   for w in days:
      for i in range(0,len(temp)):
         if temp[i]==w:
            day = temp[i]

   if day=='monday':
      day = 0
   elif day=='tuesday':
      day = 1
   elif day=='wednesday':
      day = 2
   elif day=='thursday':
      day = 3
   elif day=='friday':
      day = 4
   elif day=='saturday':
      day = 5
   elif day=='sunday':
      day = 6

   day = day-datetime.datetime.today().weekday()
   if day<0:
      day *= 1

   for i in range(0,len(new)):
      if new[i] in days:
         new[i] = (datetime.date.today() + datetime.timedelta(day)).isoformat()
         break

   new = string.join(new)

if flag==1:
   for i in range(0,len(temp)-1):
      if temp[i+1]!='today' and temp[i+1]!='tommorrow' and temp[i+1]!='tonight': 
         new.append(temp[i])
      else:
         new.append(temp[i])
         new.append('on')
   new.append(temp[i+1])   
   new = string.join(new)
   new = new.replace('today',(datetime.date.today() + datetime.timedelta(0)).isoformat())
   new = new.replace('tonight',(datetime.date.today() + datetime.timedelta(0)).isoformat())
   new = new.replace('tommorrow',(datetime.date.today() + datetime.timedelta(1)).isoformat())
   
new = new.split()

for i in range(0,len(new)-1):
   if new[i]=='on':
      date = new[i+1]
      break

date_new = date.split('-')

num = int(date_new[1])-1

date_new2 = months[num] + " " + date_new[2] + " " + date_new[0] 

new = string.join(new)

new = new.replace(date,date_new2)


f3 = open('say.txt','w')
f3.write("Added event ;" + new + ";\n")
f3.write("Is that what you wanted?")
f3.close()
os.system("festival --tts say.txt")

check = raw_input()

if check=="yes":
   f.write(new + ";\n")
   f.close()
else:
   f.close()
   os.remove('say.txt')
   execfile('jango-12.py')

f4 = open('say.txt','w')
f4.write("O K; I added it to your calendar list;")
f4.close()
os.system("festival --tts say.txt")
os.remove('say.txt')


