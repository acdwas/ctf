
from z3 import *

s = Solver()

l = [BitVec('l{}'.format(i), 32) for i in range(35)]
ll = [BitVec('ll{}'.format(i), 32) for i in range(35)]

x = 0x2a

for i in range(35):
    s.add(Or(And(l[i] >= 0x30, l[i] <= 0x39), l[i] == 0x5f, And(
        l[i] >= 0x41, l[i] <= 0x5a), And(l[i] >= 0x61, l[i] <= 0x7a)))

for i in range(35):
    a = x ^ l[i]
    a = If(a >= 0x61, a - 0x61, a)
    a += 0x1e
    ll[i] = a
    a ^= x
    a = If(a >= 0x80, a - 0x80, a)
    x = a

a = x ^ ll[0]
a = If(a >= 0x61, a - 0x61, a)
a += 0x1e
ll[0] = a

w = b"A96`''@+5.pJ`!#?yAZuN%!z06<b.wL#0/'"

for i in range(35):
    s.add(ll[i] == w[i])

while s.check() == sat:
    m = s.model()

    w = ''
    for i in range(35):
        w += chr(m[l[i]].as_long())
    print(w)

    s.add(Or(l[0] != s.model()[l[0]],
             l[1] != s.model()[l[1]],
             l[2] != s.model()[l[2]],
             l[3] != s.model()[l[3]],
             l[4] != s.model()[l[4]],
             l[5] != s.model()[l[5]],
             l[6] != s.model()[l[6]],
             l[7] != s.model()[l[7]],
             l[8] != s.model()[l[8]],
             l[9] != s.model()[l[9]],
             l[10] != s.model()[l[10]],
             l[11] != s.model()[l[11]],
             l[12] != s.model()[l[12]],
             l[13] != s.model()[l[13]],
             l[14] != s.model()[l[14]],
             l[15] != s.model()[l[15]],
             l[16] != s.model()[l[16]],
             l[17] != s.model()[l[17]],
             l[18] != s.model()[l[18]],
             l[19] != s.model()[l[19]],
             l[20] != s.model()[l[20]],
             l[21] != s.model()[l[21]],
             l[22] != s.model()[l[22]],
             l[23] != s.model()[l[23]],
             l[24] != s.model()[l[24]],
             l[25] != s.model()[l[25]],
             l[26] != s.model()[l[26]],
             l[27] != s.model()[l[27]],
             l[28] != s.model()[l[28]],
             l[29] != s.model()[l[29]],
             l[30] != s.model()[l[30]],
             l[31] != s.model()[l[31]],
             l[32] != s.model()[l[32]],
             l[33] != s.model()[l[33]],
             l[34] != s.model()[l[34]],
             ))

# 0n3_t0_0n3_Qu3st10n_M4rk_e43dbbf1a5
# FLAG: COMPFEST12{0n3_t0_0n3_Qu3st10n_M4rk_e43dbbf1a5}
