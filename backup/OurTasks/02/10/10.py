from sys import stdout

x = float (input ())
y = float (input ())

dist = (x - 1) ** 2 + (y - 1) ** 2

if (dist <= 1.5 ** 2):
    stdout.write ("inside circle ")
else:
    stdout.write ("outside circle ")

if (-1 <= x < 4 and 1 <= y < 2):
    print ("inside rectangle")
else:
    print ("outside rectangle")
