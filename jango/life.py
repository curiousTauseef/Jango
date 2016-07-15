import random
import jangopath

ans = random.randrange(100)
f = open(jangopath.HOME_DIR + '/ans.txt','w')

if ans%2==0:
   f.write("The answer to the ultimate question of life, the universe and everything is 42." )
   print "The answer to the ultimate question of life, the universe and everything is 42."   

else:
   f.write("It's 42. How many time do I have to tell you?")
   print "It's 42. How many time do I have to tell you?"

f.close()




      
