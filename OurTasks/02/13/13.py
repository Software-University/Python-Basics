N = int (input ())
P = int (input ())
new_val = int (input ())
current_bit = ((N >> P) ^ 0) % 2

if new_val != current_bit:
    N += (new_val - current_bit) * (1 << P)

print (N)

