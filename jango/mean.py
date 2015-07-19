import sys
from mewe import dic

query = ""
flag = 0

for arg in sys.argv:
   if flag==1:
      query = arg
      break
   if arg=='of':
      flag = 1

try:
   ans = dic.get(query)
   for i in ans:
      print i
except:
   print "Something went wrong."
