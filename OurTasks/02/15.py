integer = int (input ())
p = int (input ())
q = int (input ())
k = int (input ())

for i in range (0, k):
        f = ((integer & (1 << p)) // (1 << p))
        s = ((integer & (1 << q)) // (1 << q))
        integer -= f << p
        integer -= s << q
        integer += f << q
        integer += s << p
        p += 1
        q += 1

print (integer)
