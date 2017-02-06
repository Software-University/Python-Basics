from sys import stdout

a = float (input ())
b = float (input ())

stdout.write ("{0:.2f}".format (a * b))
stdout.write (" ")
print ("{0:.2f}".format (2 * (a + b)))
