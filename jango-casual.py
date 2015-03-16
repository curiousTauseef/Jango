#Jango casual module
#Developed by Rahul Arora
print "Initializing Interactive module..."

import os

while True:
   f = open('data1.txt','r')
   q = raw_input(">> ")
   if q=='stop':
      break
   t1 = set(q.split())
   ctr = 0
   check = 0
   temp = 0
   m = 0

   while True:
      ctr += 1
      a = f.readline()
      if not a:
         break
      t2 = set(a.split())
      temp = len(t1.intersection(t2))
      if temp > m and temp>=0.5*len(t1):
         m = temp
         check = ctr
      
   f.close()

   f2 = open('data2.txt','r')
   for i in range(check):
      a = f2.readline()


   f3 = open('say.txt','w')
   f3.write(a)
   f2.close()   

   if check==0:
      f3.write("I don't know what to say!! What shall I say now.")

   f3.close()
   os.system("python jango-write.py &")
   os.system("festival --tts say.txt")
   os.remove('say.txt')      

   if check==0:
      f4 = open('data1.txt','a')
      f4.write(q + "\n")
      f4.close()   
      a = raw_input(">> ")
      f5 = open('data2.txt','a')
      f5.write(a + "\n")
      f5.close()   
   

