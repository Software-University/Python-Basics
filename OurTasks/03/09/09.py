Type = str (input ())
if Type == "integer":
    a = int (input ())
    print (a + 1)
elif Type == "real":
    a = float (input ())
    print ("{0:.2f}".format (a + 1))
else:
    a = str (input ())
    print (a + "*")
