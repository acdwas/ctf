
# Yet Another Crypto Task

from z3 import *
from pwn import *

s = Solver()

a = BitVec('a', 8)
b = BitVec('b', 8)

while True:
    r = remote('tasks.kksctf.ru', 30050)
    r.readline()
    l = r.readline().decode().strip().split()
    c = [BitVec('c{}'.format(i), 8) for i in range(len(l))]
    for i in range(len(l)):
        s.add(c[i] > 0x20, c[i] < 0x7f)
    x = ord('k') ^ int(l[0], 16)

    for i in range(1, len(l), 1):
        s.add((((x*a)+b) & 0xff) ^ c[i] == int(l[i], 16))
        x = ((x*a)+b) & 0xff

    if s.check() == sat:
        m = s.model()
        w = ''.join(chr(m[c[i]].as_long()) for i in range(len(l)))
        print('k'+w[1:])
        break
    s.reset()
    r.close()
