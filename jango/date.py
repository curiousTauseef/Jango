# -*- coding: utf-8 -*-

import datetime

def handle():

	now = datetime.datetime.now()

	f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')
	f.write("Current date is : " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
	f.close()

	print "Current date : " + str(now.year) + "-" + str(now.month) + "-" + str(now.day)

handle()