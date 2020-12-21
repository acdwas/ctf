
from z3 import *

s = Solver()

a = [BitVec('a{}'.format(i), 32) for i in range(30)]

for i in range(30):
    s.add(a[i] >= 0x20, a[i] <= 0x7f)

l = [0xFB, 0xD1, 0x51, 0x8A, 0xEE, 0x7E, 0x54, 0x69, 0x9B, 0x6F, 0x77, 0xB0, 0x80, 0xEE, 0x70,
     0xC1, 0x29, 0x67, 0x71, 0xE4, 0x9C, 0xEA, 0x72, 0xED, 0x93, 0x5F, 0x11, 0xEA, 0xA4, 0x78]

a2 = 3
v2 = (0x2492492492492493 * a2) >> 64
v3 = 7 * ((v2 + ((a2 - v2) >> 1)) >> 2)
for i in range(30):
    j = 0
    while True:
        result = j
        if (j >= a2 - v3):
            break
        a[i] = ((a[i] >> 7) & 0xff) | ((2 * a[i]) & 0xff)
        a[i] &= 0xff
        j += 1

for i in range(30):
    a[i] ^= i + 5
    a[i] &= 0xff

a2 = 2
v2 = (0x2492492492492493 * a2) >> 64
v3 = 7 * ((v2 + ((a2 - v2) >> 1)) >> 2)
for i in range(30):
    j = 0
    while True:
        if (j >= a2 - v3):
            break
        v5 = (a[i] & 1) & 0xff
        a[i] >>= 1
        a[i] &= 0xff
        a[i] |= v5 << 7
        a[i] &= 0xff
        j += 1

for i in range(30):
    a[i] ^= 0xA

for i in range(30):
    s.add(a[i] == l[i])

s.check()
m = s.model()

flag = {}

for d in m.decls():
    flag[int(d.name()[1:])] = m[d].as_long()

w = ''

for i in sorted(flag):
    w += chr(flag[i])

print(w)

# X-MAS{N0is__g0_g3t_th3_points}
