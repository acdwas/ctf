
from pwn import *
from z3 import *

s = Solver()

a = [BitVec('a{}'.format(i), 32) for i in range(2)]


def fun_dis(l):
    a = int(disasm(l[0x12f3:0x12f3+7]).split()[-1], 16)
    b = int(disasm(l[0x1319:0x1319+3]).split()[-1], 16)
    c = int(disasm(l[0x131c:0x131c+5]).split()[-1], 16)
    d = int(disasm(l[0x134a:0x134a+5]).split()[-1], 16)
    e = int(disasm(l[0x1370:0x1370+5]).split()[-1], 16)
    return [a, b, c, d, e]


key = ''

for i in range(400):
    file_r = './out{}'.format(str(i).rjust(3, '0'))
    with open(file_r, 'rb') as f:
        l = f.read()
    f.close()
    l = fun_dis(l)

    s.add(And((a[1] + a[0] + l[0] >> l[1] == l[2]),
              ((a[1] ^ a[0]) + a[0] == l[3])), (a[1] * a[0] == l[4]))

    if s.check() == sat:
        m = s.model()
        w = chr(m[a[0]].as_long()) + chr(m[a[1]].as_long())
        # print(w)
        key += w
    else:
        print(file_r)
    s.reset()

print(key)
