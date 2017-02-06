import math

a = int (input ())
if 0 < a < 10:
    print (a * math.pow (10, (math.ceil (a / 3.0))))
else:
    print ("invalid score")
