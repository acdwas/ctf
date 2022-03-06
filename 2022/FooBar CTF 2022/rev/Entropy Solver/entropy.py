
from z3 import *

s = Solver()

a = BitVec('a', 32)
b = BitVec('b', 32)
c = BitVec('c', 32)
d = BitVec('d', 32)
e = BitVec('e', 32)
f = BitVec('f', 32)

b ^= a
b ^= 0x153c3a3c
a += 0x10
a ^= 0x47554c57
c -= 0x20
c ^= 0x6c417534
d &= 0xffffffff
d ^= 0x4e40725f
e ^= 0x22
e ^= 0x694d3046
f += 2
f ^= 1
f ^= 0x7d52335d
a |= b
a |= c
a |= d
a |= e
a |= f


s.add(a == 0x0)

s.check()
m = s.model()

flag = {}

for i in m.decls():
    flag[i.name()] = m[i].as_long()

w = b''

for i in sorted(flag):
    w += bytes.fromhex(hex(flag[i])[2:])[::-1]

print(w)

# GLUG{viRTuAl_r@Nd0MiZ3R}

