
from z3 import *

s = Solver()

a = [BitVec(f'a{i}', 8) for i in range(39)]

for i in range(39):
    a[i] = (a[i] + 59) ^ 0x38
for j in range(39):
  a[j] = (a[j] + 18) ^ 0xFD
for k in range(39):
    a[k] = (a[k] + 4) ^ 0x50
for l in range(39):
    a[l] = (a[l] + 19) ^ 0x68
for m in range(39):
    a[m] = (a[m] + 12) ^ 0x79
for n in range(39):
    a[n] = (a[n] - 68) ^ 0xA0
for ii in range(39):
    a[ii] = (a[ii] + 10) ^ 0xCD
for jj in range(39):
    a[jj] = (a[jj] - 72) ^ 0x5A
for kk in range(39):
    a[kk] = (a[kk] + 11) ^ 0xBD
for ll in range(39):
    a[ll] = (a[ll] - 31) ^ 0xED
for mm in range(39):
    a[mm] = (a[mm] + 69) ^ 0x22
for nn in range(39):
    a[nn] = (a[nn] - 66) ^ 0x6B
for i1 in range(39):
    a[i1] = (a[i1] - 38) ^ 0x6B
for i2 in range(39):
    a[i2] = (a[i2] + 118) ^ 0xFA
for i3 in range(39):
    a[i3] = (a[i3] + 22) ^ 0x6B
for i4 in range(39):
    a[i4] = (a[i4] - 75) ^ 0x6B
for i5 in range(39):
    a[i5] = (a[i5] - 115) ^ 0x64
for i6 in range(39):
    a[i6] = (a[i6] + 10) ^ 0xAB
for i7 in range(39):
    a[i7] = (a[i7] + 99) ^ 0x1B
for i8 in range(39):
    a[i8] = (a[i8] - 43) ^ 0xF0
for i9 in range(39):
    a[i9] = (a[i9] + 117) ^ 0x6B

l = [ 77,185,77,11,212,102,227,41,184,77, 223, 102, 184, 77, 14, 196, 223, 212, 20, 59, 223, 102, 44, 20, 71, 223, 183, 184, 183, 223, 71, 77, 164, 223, 50, 184, 234, 245, 146]


for i in range(39):
    s.add(a[i] == l[i])

print(s.check())
m = s.model()

flag = {}

for d in m.decls():
    flag[int(d.name()[1:])] = m[d].as_long()

w = ''

for i in sorted(flag):
    w += chr(flag[i])

print(w)


