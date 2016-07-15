import jangopath

f = open(jangopath.HOME_DIR + '/ans.txt','w')

print "Hello, my name is Jango. I am the first command line based personal assistant."

print "I can help you in your day to day tasks by checking your emails, sending sms, finding meaning of words, making notes and what not. If that's not enough, I can also entertan you by telling jokes and answering to all your questions."

f.write("Hello, my name is Jango. \n\n")
f.write("I can help you in your day to day tasks by checking your emails, sending sms, finding meaning of words, making notes and what not. If that's not enough, I can also entertan you by telling jokes and answering to all your questions.")
f.close()

#print "I can : "
#print "Tell time, date and day."
#print "Find meanings of words."
#print "Entertain you by telling jokes."
#print "Tell current weather."
#print "Make notes."
#print "Search information on wikipedia."
#print "Solve maths for you."
#print "Sync with your gmail account inform you about new messages."
#print "Set timers."
#print "Play songs from your playlists."
#print "Search facts"
#print "Send SMS"
