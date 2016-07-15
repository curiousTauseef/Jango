# -*- coding: utf-8 -*-

import datetime
now = datetime.datetime.now()
f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')
f.write("Current day is : " + str(now.strftime("%A")))
f.close()
print now.strftime("%A")