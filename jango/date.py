# -*- coding: utf-8 -*-

import datetime
import jangopath

def handle():

	now = datetime.datetime.now()

	f = open(jangopath.HOME_DIR + '/ans.txt','w')
	f.write("Current date is : " + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
	f.close()

	print "Current date : " + str(now.year) + "-" + str(now.month) + "-" + str(now.day)

handle()