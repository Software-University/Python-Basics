import math

x = float (input ())
y = float (input ())

if x * x + y * y <= 4:
    print ("yes " + "{0:.2f}".format (math.sqrt (x * x + y * y)))
else:
    print ("no " + "{0:.2f}".format (math.sqrt (x * x + y * y)))
