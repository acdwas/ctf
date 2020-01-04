
from z3 import *

s = Solver()

l = 0
a = [BitVec('a%d' % i, 16) for i in range(8)]

for i in range(8):
    l <<= 2
    l += a[i]

for i in range(8):
    s.add(a[i] >= 0x41, a[i] <= 0x5a)

s.add(l == 0xCFE1)

s.check()
m = s.model()

w = ''
for i in range(8):
    w += chr(m[a[i]].as_long())
print('Password: ' + w)


# while s.check() == sat:
#     m = s.model()

#     w = ''
#     for i in range(8):
#         w += chr(m[a[i]].as_long())
#     print(w)

#     s.add(Or(a[0] != s.model()[a[0]],
#              a[1] != s.model()[a[1]],
#              a[2] != s.model()[a[2]],
#              a[3] != s.model()[a[3]],
#              a[4] != s.model()[a[4]],
#              a[5] != s.model()[a[5]],
#              a[6] != s.model()[a[6]],
#              a[7] != s.model()[a[7]]))
