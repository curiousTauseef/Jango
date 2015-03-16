#Set timer
#Developed by Rahul Arora
print "Initializing timer script..."

import os
import string

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    
         numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     
         numwords[word] = (1, idx * 10)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

h = 0
m = 0
s = 0
tot = 0
f = open('query.txt','r')
f2 = open('say.txt','w')
f3 = open('timer.txt','w')
check = f.readline()

temp = check.split()


for i in range(0,len(temp)):
   if temp[i]=='for':
      if temp[i+2]=='hours':
         h = text2int(temp[i+1])  
         try: 
            if temp[i+4]=='minutes' or temp[i+4]=='minute':
               m = text2int(temp[i+3])
               try:
                  if temp[i+6]=='seconds' or temp[i+6]=='second':
                     s = text2int(temp[i+5])
                  elif temp[i+4]=='seconds' or temp[i+4]=='second':
                     s = text2int(temp[i+3])
               except IndexError:
                  pass
         except IndexError:
            pass
         

      elif temp[i+2]=='minutes' or temp[i+2]=='minute':
         m = text2int(temp[i+1]) 
         try: 
            if temp[i+4]=='seconds' or temp[i+4]=='second':
               s = text2int(temp[i+3])
         except IndexError:
            pass

      elif temp[i+2]=='seconds' or temp[i+2]=='second':
         s = text2int(temp[i+1]) 

i = 0
while temp[i]!='for':
   temp[i] = ' '
   i += 1
temp = string.join(temp)   
temp = temp.strip()

f2.write("Timer set ;" + temp + " ; starting now")      
h = h*3600
m =  m*60
tot = h + m + s   
tot = str(tot)    
f3.write(tot)
  
temp = 'Time up ' + temp
f3.write("\n" + temp)

f.close()
f2.close()
f3.close()
os.system("python jango-write.py &")
os.system('python jango-15_1.py &')
os.system("festival --tts say.txt")
os.remove('query.txt')
os.remove('say.txt')








