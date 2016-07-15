# -*- coding: utf-8 -*-

import datetime
import jangopath

now = datetime.datetime.now()
f = open(jangopath.HOME_DIR + '/ans.txt','w')
f.write("Current day is : " + str(now.strftime("%A")))
f.close()
print now.strftime("%A")