
from z3 import *

s = Solver()

l = [0x00001337deadbeef, 0x0000c0de12345678, 0x0000abcdef012345, 0x00009876543210ab]
key = [0xfd83487a8f04bc91, 0x1ea9b29316416331, 0x2fbea4546b08944f, 0x922e9e7e9854dcaf]

def fun(arg1, arg2):
    arg1 ^= arg2
    temp = arg1
    temp = (temp << 13) | LShR(temp, (64 - 13))
    
    rax = arg1
    rax = (rax << 5) - rax
    rax ^= temp
    
    return rax

b = [BitVec(f'b{i}', 8) for i in range(32)]

for i in range(32):
    s.add(b[i] >= 0x20, b[i] <= 0x7e)


a = [
    Concat(b[7], b[6], b[5], b[4], b[3], b[2], b[1], b[0]),
    Concat(b[15], b[14], b[13], b[12], b[11], b[10], b[9], b[8]),
    Concat(b[23], b[22], b[21], b[20], b[19], b[18], b[17], b[16]),
    Concat(b[31], b[30], b[29], b[28], b[27], b[26], b[25], b[24]),
]

x = fun(a[1], l[0])
b_val = x ^ a[0] 

x = fun(b_val, l[1]) 
b1_val = x ^ a[1] 

x = fun(b1_val, l[2]) 
b_val = b_val ^ x 

x = fun(b_val, l[3]) 
b1_val = b1_val ^ x 

x = fun(a[3], l[0])
b2_val = x ^ a[2]

x = fun(b2_val, l[1])
b3_val = x ^ a[3]

x = fun(b3_val, l[2])
b2_val = b2_val ^ x

x = fun(b2_val, l[3])
b3_val = b3_val ^ x

s.add(b_val == key[0])
s.add(b1_val == key[1])
s.add(b2_val == key[2])
s.add(b3_val == key[3])

if s.check() == sat:
    model = s.model()
    solution = [model[b[i]].as_long() for i in range(32)]
    flag = bytes(solution).decode('ascii')
    print("Solution found:")
    print(flag)
else:
    print("No solution found")