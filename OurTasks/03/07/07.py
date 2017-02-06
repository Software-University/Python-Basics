a = float (input ())
b = float (input ())
c = float (input ())

print (min (a, b, c))
print (a + b + c - min (a, b, c) - max (a, b, c))
print (max (a, b, c))
