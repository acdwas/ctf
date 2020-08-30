
from z3 import *
from pwn import *

s = Solver()

a = [BitVec('a{}'.format(i), 8) for i in range(16)]

for i in range(16):
    s.add(And(a[i] > 0x30, a[i] <= 0x39))

v2 = 0

for i in range(1, 16, 2):
    v2 = (v2 ^ (a[i] - 48)) + 2 * (~v2 | (a[i] - 48)) - 2 * ~v2

v4 = 0

for i in range(0, 16, 4 - (i ^ 2) + 2 * (i & 0xFFFFFFFD)):
    v3 = 2 * (a[i] - 0x30)
    x = If((3 * (~v3 & 0xFFFFFFF7) + 2 * ~(v3 ^ 0xFFFFFFF7) +
            3 * (v3 & 8) - 2 * ~(v3 & 0xFFFFFFF7)) > 0, 1, 0)
    if is_int(x) == 1:
        v3 = ((v3 % 10) ^ (v3 / 10)) + 2 * ((v3 % 10) & (v3 / 10))
    v4 += v3

s.add((v2 + v4) % 10 == 0)

while s.check() == sat:
    m = s.model()

    w = ''
    for i in range(16):
        w += chr(m[a[i]].as_long())
    # p = process('./welcome')
    p = remote('welcome.fword.wtf', 5000)
    p.readline()
    p.sendline(w)
    ww = p.recv()
    if b'FwordCTF' in ww:
        print('Password: {}'.format(w))
        print('Flag: {}'.format(ww.strip().decode()))
        break
    p.close()

    s.add(Or(a[0] != s.model()[a[0]],
             a[1] != s.model()[a[1]],
             a[2] != s.model()[a[2]],
             a[3] != s.model()[a[3]],
             a[4] != s.model()[a[4]],
             a[5] != s.model()[a[5]],
             a[6] != s.model()[a[6]],
             a[7] != s.model()[a[7]],
             a[8] != s.model()[a[8]],
             a[9] != s.model()[a[9]],
             a[10] != s.model()[a[10]],
             a[11] != s.model()[a[11]],
             a[12] != s.model()[a[12]],
             a[13] != s.model()[a[13]],
             a[14] != s.model()[a[14]],
             a[15] != s.model()[a[15]]
             ))
