# -*- coding: utf-8 -*-

import datetime

now = datetime.datetime.now()

f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')
f.write("Current time is : " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
f.close()

print "Current time : " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) 