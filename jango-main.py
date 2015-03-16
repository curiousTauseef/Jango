#Driver script
#Developed by Rahul Arora

import sys
import string
import urllib2
import time
import os

os.system('python jango-13.py &')

def internet():
    try:
      response=urllib2.urlopen('https://www.google.co.in/?gfe_rd=cr&ei=wZp5VPObK8vDuASSqIDoDw&gws_rd=ssl')
      return True
    except urllib2.URLError as err: 
      f2 = open('error.txt','w')
      f2.write("Internet connection not working; Reconnecting in 15 seconds;")
      f2.close()
      os.system("festival --tts error.txt")
      os.remove("error.txt")
      time.sleep(15)
    return False

check = []
ans = []

while check!='stop':
   print "Initializing driver script..."

   #while internet()==False:
    #  internet()

   f = open('query.txt','w')
   flag = 0
   check = raw_input(">> ")
   count = 0
   total = int(len(check.split()))

   word_set1 = {"what","time","tell"}
   word_set2 = {"what","date","tell"}
   word_set3 = {"what","day","tell"}
   word_set4 = {"news","headlines"}
   word_set5 = {"search","find","about"}
   word_set6 = {"joke","a"}
   word_set7 = {"word","a"}
   word_set8 = {"search","for","on","flipkart"}
   word_set9 = {"movies"}
   word_set10 = {"what","is","the","meaning","of","tell"}
   word_set11 = {"note"}
   word_set12 = {"calendar"}
   word_set13 = {"do","any" }
   word_set14 = {"set","timer"}
   word_set15 = {"play","a","some","listen"}
   word_set16 = {"remind","remember"}
   word_set17 = {"define"}
   word_set18 = {"talk","casual","interactive"}

   for w in word_set1:
      if w in check.split():
         count += 1

   if count==2:
      execfile('jango-3.py')
      flag=1

   count = 0

   for w in word_set2:
      if w in check.split():
         count += 1

   if count==2:
      execfile('jango-2.py')
      flag=1

   count = 0

   for w in word_set3:
      if w in check.split():
         count += 1

   if count==2:
      execfile('jango-4.py')
      flag=1

   count = 0

   for w in word_set4:
      if w in check.split():
         count += 1

   if count==2:
      execfile('jango-1.py')
      flag=1
 
   count = 0

   for w in word_set6:
      if w in check.split():
         count += 1

   if count==2:
      execfile('jango-6.py')
      flag=1

   count = 0

   for w in word_set7:
      if w in check.split():
         count += 1

   if count==2:
      execfile('jango-7.py')
      flag=1

   count = 0

   for w in word_set9:
      if w in check.split():
         count += 1

   if count==1:
      execfile('jango-9.py')
      flag=1

   count = 0

   for w in word_set11:
      if w in check.split():
         count += 1

   if count==1:
      execfile('jango-11.py')
      flag=1

   count = 0

   for w in word_set18:
      if w in check.split():
         count += 1

   if count==1:
      execfile('jango-casual.py')
      flag=1

   count = 0

   for w in word_set16:
      if w in check.split():
         count += 1

   if count==1:
      f3 = open('reminder.txt','a')
      temp = check.split()
      for i in range(0,len(temp)):
         if temp[i]!='to':
            temp[i] = ' '
         else:
            temp[i] = ' '
            temp = string.join(temp)
            temp = temp.strip() 
            break
      f3.write(temp + "\n")
      f3.close()
      flag=1

   count = 0

   for w in word_set13:
      if w in check.split():
         count += 1

   if count==2:
      temp = check.split()
      for i in range(0,len(temp)):
         if temp[i]=='on':
            f.write(temp[i+1])
            break
      execfile('jango-14.py')
      flag=1

   count = 0

   for w in word_set12:
      if w in check.split():
         count += 1

   if count==1:
      execfile('jango-12.py')
      flag=1

   count = 0

   for w in word_set14:
      if w in check.split():
         count += 1

   if count==2:
      f.write(check)
      execfile('jango-15.py')
      flag=1

   count = 0

   for w in word_set15:
      if w in check.split():
         count += 1

   if count==2:
      temp = check.split()
      for i in range(0,len(temp)):
         if temp[i]=='a' or temp[i]=='some':
            f.write(temp[i+1])
            break
      execfile('jango-16.py')
      flag=1
   
   count = 0

   for w in word_set10:
      if w in check.split():
         count += 1

   if count==5 and flag!=1:
      temp = check.split()
      for w in word_set10:
         for ind in range(0,len(temp)):
            if temp[ind] == w:
               temp[ind] = ' ' 
               break   
      temp = string.join(temp)
      temp = temp.strip() 
      try: 
         f.write(temp)
      except ValueError:
         pass
      f.close()
      execfile('jango-10.py')
      flag = 1

   count = 0

   for w in word_set17:
      if w in check.split():
         count += 1

   if count==1 and flag!=1:
      temp = check.split()
      for i in range(0,len(temp)):
         if temp[i]!='define':
            temp[i] = ' '
         else:
            temp[i] = ' '
            break 
      temp = string.join(temp)
      temp = temp.strip() 
      try: 
         f.write(temp)
      except ValueError:
         pass
      f.close()
      execfile('jango-10.py')
      flag = 1

   count = 0

   for w in word_set8:
      if w in check.split():
         count += 1

   if count==4 and flag!=1:
      temp = check.split()
      for w in word_set8:
         for ind in range(0,len(temp)):
            if temp[ind] == w:
               temp[ind] = ' '    
      temp = string.join(temp) 
      try: 
         f.write(temp)
      except ValueError:
         pass
      f.close()
      execfile('jango-8.py')
      flag = 1

   count = 0

   for w in word_set5:
      try:
         if w in check.split():
            count += 1
      except AttributeError:
         pass

   if count==2 and check!='stop' and flag!=1:
      temp = check.split()
      for i in range(0,len(temp)):
         if temp[i]!='search' and temp[i]!='find':
            temp[i] = ' '   
         else:
            temp[i] = ' '
            temp[i+1] = ' '
            break
      temp = string.join(temp)
      temp = temp.strip() 
      try: 
         f.write(temp)
      except ValueError:
         pass
      f.close()
      execfile('jango-5.py')
      flag=1

   

