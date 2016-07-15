import re
import sys
import jangopath

query = ""
f = open(jangopath.HOME_DIR + '/ans.txt','w')
for arg in sys.argv:
   query = query + arg + " "  

def handle(query):
    expression = re.findall("\s([0-9\+\-/\*\(\)\.\s]+)", query)
    
    if not expression:
        f.write("Something went wrong.")
        print "Something went wrong."
        return

    expression = expression[0]

    try:
        print eval(expression)
        ans = int(eval(expression))
        f.write(str(ans))
    except SyntaxError:
        f.write("Something went wrong.")
        print "Something went wrong."
        return
    f.close()

handle(query)

