# -*- coding: utf-8 -*-

import datetime
import jangopath

now = datetime.datetime.now()

f = open(jangopath.HOME_DIR + '/ans.txt','w')
f.write("Current time is : " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
f.close()

print "Current time : " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) 