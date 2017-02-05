num = int (input ())

third_digit = num // 100 % 10;

if third_digit == 7:
    print ("True")
else:
    print ("False " + str (third_digit))
