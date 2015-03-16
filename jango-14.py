#Check a calender event
#Developed by Rahul Arora
print "Initializing calender script..."

import os
import string
import datetime

day = 0
flag = 0
months = ["january","february","march","april","may","june","july","August","september","october","november","december"]
f = open('query.txt','r')
check = f.readline()
check = check.strip()
f2 = open('cal.txt','r')
f3 = open('say.txt','w')

if check=='today':
   day = (datetime.date.today() + datetime.timedelta(0)).isoformat()

elif check=='tommorrow':
   day = (datetime.date.today() + datetime.timedelta(1)).isoformat()

else:
   if check=='monday':
      day = 0
   elif check=='tuesday':
      day = 1
   elif check=='wednesday':
      day = 2
   elif check=='thursday':
      day = 3
   elif check=='friday':
      day = 4
   elif check=='saturday':
      day = 5
   elif check=='sunday':
      day = 6

   day = day-datetime.datetime.today().weekday()
   if day<0:
      day *= -1
   
   day = (datetime.date.today() + datetime.timedelta(day)).isoformat()


date_new = day.split('-')

num = int(date_new[1])-1

date_new2 = months[num] + " " + date_new[2] + " " + date_new[0] 

date_new2 = date_new2.split()

with open('cal.txt','r') as f2:
   for check in f2:
      temp = check.split()
      for i in range(0,len(temp)-3):
         if temp[i]=='on':
            if temp[i+1]==date_new2[0]:
               if temp[i+2] in date_new:
                  if temp[i+3] in date_new2:
                     f3.write(check)
                     flag=1

if flag!=1:
   f3.write("No event on this day;")

f.close()
f2.close()
f3.close()
os.system("python jango-write.py &")
os.system("festival --tts say.txt")
os.remove('say.txt')
os.remove('query.txt')



