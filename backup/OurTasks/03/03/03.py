cards = "23456789JQKA"
a = input ()
if (a in cards and len (a) == 1 or a == "10"):
    print ("yes " + str (a))
else:
    print ("no " + str (a))                
