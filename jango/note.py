import datetime
import jangopath
import sys


def handle(text):
   f2 = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')
   #note = raw_input("What shall I note down? : ")
   note = text
   note = note + " * " + str(datetime.date.today()) + "\n"
   try:
      f = open(jangopath.TEXT_PATH, 'a')
      f.write(note)
      f.close()
      f2.write("Note written successfully.")
   except:
      f2.wrtie("Something went wrong.")
      print "Something went wrong."
      f2.close()
      return

def handle2():
   f2 = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')
   try:
      f = open(jangopath.TEXT_PATH, 'r')
   except:
      f2.write("Something went wrong.")
      print "Something went wrong."
      f2.close()
      return
   flag = 0
   while True:
      note = f.readline()
      if not note:
         break
      else:
         try:
            note = note.split("*")
            if str(note[1]).strip()==str(datetime.date.today()):
               if flag==0:
                  f2.write("Notes for today are : <br>")
               f2.write("<li>" + note[0] + "<br>")
               print note[0]
               flag = 1
         except:
            pass
   if flag==0:
      f2.write("No notes for today.")
      print "No notes for today."
      f2.close()

#for arg in sys.argv:
 #  flag = 0
  # if "write"==arg.lower() or "make"==arg.lower():
   #   handle()
    #  flag = 1
     # break

flag = 0

if flag==0:
   handle2()


