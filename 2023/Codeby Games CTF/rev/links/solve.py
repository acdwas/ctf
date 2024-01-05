
from z3 import *

s = Solver()

n = 7 # length name 5...6...7...8...

a = [BitVec(f'a{i}', 8) for i in range(n)]
b = [BitVec(f'b{i}', 32) for i in range(3)]

for i in range(n):
    a[i] = ZeroExt(56, a[i])
    s.add(Or(And(a[i] >= 0x61, a[i] <= 0x7a), And(a[i] >= 0x41, a[i] <= 0x5a),))

a4 = ZeroExt(32, b[2])
a3 = ZeroExt(32, BitVecVal(0x434F4445, 32))

A = Array('A', BitVecSort(64), BitVecSort(64))

for i, val in enumerate([0xB42DD243, 0x304BD9D9, 0x177934A3, 0x17DAA0BA, 0x77713B7C, 0x29C33CDF]):
    xx = BitVecVal(val, 32)
    A = Store(A, i, ZeroExt(32, xx))

v19 = BitVecVal(0, 32)
v19 = ZeroExt(32, v19)

v6 = BitVecVal(0, 32)
v6 = ZeroExt(32, v6)

v20 = BitVecVal(0, 32)
v20 = ZeroExt(32, v20)

for i in range(n):
    v3 = 1192722 * a[i]
    v20 += 1050640 * ((v3 << 12) + 32 * v3 * 16 * v3 + (v3 << 7) + (v3 << 24))

v20 &= 0xffffffff

for i in range(n):
    v3 = 13448 * a[i]
    v4 = 8 * v3 + 8 * v3 * 32 * v6 + (v3 << 8) + (v6 << 20)
    v6 = 32 * v6 + 8 * v6 + 48 * v4 + (v4 << 20)
    v19 += v6

v19 &= 0xffffffff

a4 ^= v19

a4 &= 0xffffffff

v15 = (a4 ^ a3) % 0x39 - 11

v14 = ZeroExt(32, b[0])
v12 = ZeroExt(32, b[1])

v8 = 1

v11 = (a4 ^ a3) << (((a4 ^ a3) % 0x39 - 11 + 68) ^ 0x61)

v11 >>= 32

v9 = 3

v13 = v12 - ((((v11 + A[(v11 >> (v8 // 9 + 3)) & 3]) ^ (v14 + ((v14 >> (v8 // 0x14 + 6)) ^ (v14 << (v8 // 0xC))))) - 0) ^ 0xFFFFCDF3)

v13 &= 0xffffffff
v11 -= (a4 ^ a3)
v11 &= 0xffffffff
v12 = v13 - 0
v12 &= 0xffffffff
v7 = v12 << ((v8 // 9 + 4) ^ 8)
v7 &= 0xffffffff

v66 = LShR(v12, (((v8 >> 1) - v9 + 58) ^ 0x64) % 32)

v10 = v12 + (v66 ^ v7)
v10 &= 0xffffffff

v14 -= ((v10 ^ (A[v11 & 3] + v11)) - 0x123) ^ 0x17BEE2

v14 &= 0xffffffff

x = v14 ^ 4
y = v12 ^ 7

m1 = (((v8 + 1337) >> 3) - 9) ^ y ^ 0x5277
m1 &= 0xffffffff
n1 = ((a4 ^ a3) % 0x39 - 106) ^ x ^ 0x1E
n1 &= 0xffffffff

s.add(v15 == 1)
s.add((a4 ^ a3) % 0x39 != 11)
s.add(v19 == m1)
s.add(v20 == n1)

while s.check() == sat:
    m = s.model()

    w = ''
    for i in range(n):
        w += chr(m.eval(a[i]).as_long())

    print(w)
    print(f'{hex(m[b[0]].as_long())[2:].zfill(8)}-{hex(m[b[1]].as_long())[2:].zfill(8)}-{hex(m[b[2]].as_long())[2:].zfill(8)}')

    conditions = []
    for i in range(n):
        conditions.append(a[i] != s.model().eval(a[i]))

    s.add(Or(*conditions))
