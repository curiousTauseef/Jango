import re
import sys

query = ""
for arg in sys.argv:
   query = query + arg + " "  

def handle(query):
    expression = re.findall("\s([0-9\+\-/\*\(\)\.\s]+)", query)
    
    if not expression:
        print "Something went wrong."
        return

    expression = expression[0]

    try:
        print eval(expression)
    except SyntaxError:
        print "Something went wrong."
        return

handle(query)
