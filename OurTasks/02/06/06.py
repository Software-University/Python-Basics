y = int (input ())
a = y // 1000 % 10
b = y // 100 % 10
c = y // 10 % 10
d = y // 1 % 10
print (a + b + c + d);
print ("".join ([str(d), str(c), str(b), str(a)]));
print ("".join ([str(d), str(a), str(b), str(c)]));
print ("".join ([str(a), str(c), str(b), str(d)]));
