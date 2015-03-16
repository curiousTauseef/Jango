#Plays music
#Developed by Rahul Arora
print "Initializing music script"

import pygame
import time
import random
import os

f = open('query.txt','r')
f2 = open('say.txt','w')
check = f.readline()
check = check.strip()
check = "Music/" + check
check = check.rstrip()

files = os.listdir(check)
ans = files[random.randrange(len(files))]
check = check + "/" + ans
check = check.rstrip()

f2.write("Playing " + ans)
f2.close()
f.close()
os.system("python jango-write.py &")
pygame.init()
pygame.mixer.music.load(check)
pygame.mixer.music.play()   

time.sleep(5)
os.remove('say.txt')
os.system("clear")
while True:
   num = random.randrange(100)
   if num%3==0 or num%7==0 :
      print "\n\n\n\n\n\n\n\t\t\t   __              __" 
      print "\n\t\t\t ______________________"
      print "\n\t\t\t|                      |"
      print "\t\t\t ______________________"
      time.sleep(0.5)
      os.system("clear")
      num = 1
   else:
      print "\n\n\n\n\n\n\n\t\t\t   __              __"  
      print "\n\t\t\t ______________________"
      print "\t\t\t|                      |"
      print "\t\t\t ______________________"
      time.sleep(0.5)
      os.system("clear")
      
