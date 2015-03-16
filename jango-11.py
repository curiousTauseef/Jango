#Write down notes
#Developed by Rahul Arora
print "Initializing notes script..."

import os

f2 = open('say.txt','w')
f2.write("What shall i note down?;")
f2.close()
os.system("festival --tts say.txt")

count = 0

note = raw_input()
f = open('notes.txt','a')
f.write(note + ";\n")
f.close()
f4 = open('say.txt','w')
f4.write("I wrote this to your notes;")
f4.close()
os.system("festival --tts say.txt")

os.remove('say.txt')




   


