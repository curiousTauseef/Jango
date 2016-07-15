import ConfigParser
import imaplib
import email
import datetime
import jangopath

Config = ConfigParser.ConfigParser()
f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')

def process_mailbox(M):
   flag = 0
   rv, data = M.search(None, "(UNSEEN)")
   if rv!="OK":
      f.wrtie("No messages found!")
      print "No messages found!"
      return

   for num in data[0].split():
      rv, data = M.fetch(num, '(RFC822)') #Returns a raw data format, use email method to parse it.
      if rv!="OK":
          f.write("Something went wrong.")
          print "Something went wrong.", num
          return

      msg = email.message_from_string(data[0][1]) #Returns a message object, and we can then access header items as a dictionary on that object.
      print 'Message %s: %s' % (num, msg['Subject'])
      f.write('Message %s: %s' % (num, msg['Subject']) + '<br>')
      date_tuple = email.utils.parsedate_tz(msg['Date'])
      if date_tuple:
         local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
         print "Local Date:", \
              local_date.strftime("%a, %d %b %Y %H:%M:%S")
         flag = 1  
   if flag==0:
      print "No messages found!" 
      f.wrtie("No messages found!")         

M = imaplib.IMAP4_SSL('imap.gmail.com') #Create an imap object.

Config.read(jangopath.CONFIG_PATH)

username = Config.get('Person', 'uname')
password = Config.get('Person', 'pswd')

try:
   M.login(username, password) #If login is successfull, we can do operations with our imap object.
   rv, mailboxes = M.list() #Methods returns tuples and status(mostly=='OK')->Use to get list of mailboxes.
   rv, data = M.select("INBOX") #Select a particular label.
   if rv == "OK":
      process_mailbox(M)
      M.close()
   M.logout()
except imaplib.IMAP4.error:
   f.write("Something went wrong." )
   print "Something went wrong."  

f.close()

