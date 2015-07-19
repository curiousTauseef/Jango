import datetime
import jangopath
import sys
   
def handle():
   note = raw_input("What shall I note down? : ")
   note = note + " * " + str(datetime.date.today()) + "\n"
   try:
      f = open(jangopath.TEXT_PATH, 'a')
      f.write(note)
      f.close()
   except:
      print "Something went wrong."
      return

def handle2():
   try:
      f = open(jangopath.TEXT_PATH, 'r')
   except:
      print "Something went wrong."
      return
   flag = 0
   while True:
      note = f.readline()
      if not note:
         break
      else:
         note = note.split("*")
         if str(note[1]).strip()==str(datetime.date.today()):
            print note[0]
            flag = 1
   if flag==0:
      print "No notes for today."

for arg in sys.argv:
   flag = 0
   if "write"==arg.lower() or "make"==arg.lower():
      handle()
      flag = 1
      break

if flag==0:
   handle2()
