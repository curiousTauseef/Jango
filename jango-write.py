import time

f = open('say.txt','r')
while True:
   check = f.readline()
   if not check:
      break
   for i in range(len(check)):
      print check[i]
      time.sleep(0.07)
