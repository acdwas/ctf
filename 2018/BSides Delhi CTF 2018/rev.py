
from z3 import *

check = [0x7c, 0x23, 0x34, 0x62, 0x7e, 0x57, 0x37, 0x68, 0x3b, 0x57, 0x6a, 0x3c, 0x35, 0x21, 0x6b, 0x3d, 0x6f, 0x6e, 0x39, 0x62, 0x35, 0x3f]


def fun(s, v):
    y = [BitVec('y{}'.format(x), 8) for x in range(22)]
    for i in s:
        x += ord(i)
    x /= 30
    for i in range(22):
        if i & 1:
            y[i] = v[i] - 4
        else:
            y[i] = v[i] + 4
        y[i] ^= x
    return y


s = Solver()

v = [BitVec('v{}'.format(x), 8) for x in range(22)]

a = fun('bi0s', v)


for i in range(22):
    s.add(a[i] == check[i])

if s.check() == sat:
    m = s.model()
    w = ''
    for i in range(22):
        w += chr(int(str(m[v[i]])))

print w
