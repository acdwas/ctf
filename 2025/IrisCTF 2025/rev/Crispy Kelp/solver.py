
from z3 import *

s = Solver()

w = 'ebb398ebb58cebb594ebb389ebb3a4ebb4b1ebb693ebb2b4ebb58febb38debb5a3ebb59cebb3a2ebb682ebb68eebb39debb485ebb3b3ebb488ebb480ebb2acebb580ebb39febb58debb59cebb5b5ebb4abebb3a4ebb6a2ebb5bfebb69aebb48cebb5b2ebb486ebb3b7ebb5b6ebb4b1ebb58febb6a4ebb587ebb48aebb583ebb382ebb59aebb385ebb395ebb384ebb2acebb2a6f097a4a9f097a8bef097a8b9f097a4bff097a59ff097a9b4f097a6bef097a5a7f097a8b3f097a5bff097a998f097a980f097a4a7f097a895f097a6bbf097a59bf097a894f097a687f097a6a8f097a88ff097a584f097a99cf097a4b8f097a8a8f097a8b9f097aa8bf097aa82f097a68ff097a794f097a9b0f097a880f097a6aff097a8b3f097a6b1f097a4bbf097a9aef097a8b3f097a99ff097a7a2f097a9bcf097a782f097a8a7f097a5a3f097a8acf097a691f097a4b0f097a695f097a5bd'

l = []

def fun(s):
    global l
    i = 0
    while True:
        x1 = (i >> 12) | 0xE0
        x2 = (i >> 6) & 0x3F | 0x80
        x3 = i & 0x3F | 0x80
        if x1 == int(s[:2], 16) and x2 == int(s[2:4], 16) and x3 == int(s[4:], 16):
            print(hex(x1), hex(x2), hex(x3), f'{i} = {hex(i)}')
            l.append(i)
            break
        i += 1

def fun1(s):
    global l
    i = 0
    while True:
        x1 = (i >> 18) | 0xF0
        x2 = (i >> 12) & 0x3F | 0x80
        x3 = (i >> 6) & 0x3F | 0x80
        x4 = i & 0x3F | 0x80
        if x1 == int(s[:2], 16) and x2 == int(s[2:4], 16) and x3 == int(s[4:6], 16) and x4 == int(s[6:], 16):
            print(hex(x1), hex(x2), hex(x3), hex(x4), f'{i} = {hex(i)}')
            l.append(i)
            break
        i += 1


i = 0

w_len = len(w)

while i < w_len:
    if w[i] == 'e':
        fun(w[i:i+6])
        i += 6
    else:
        fun1(w[i:i+8])
        i += 8

n = len(l) // 2

ll = l[n+1:]
l = l[:n]

a = [BitVec(f'a{i}', 32) for i in range(n)]
b = [BitVec(f'b{i}', 32) for i in range(n)]
c = BitVec('c', 32)

for i in range(n):
    s.add(And(a[i] >= 0, a[i] < 0x100))

for i in range(n):
    s.add(And(b[i] > 0x20, b[i] < 0x7f))

for i in range(n):
    x = (b[i] ^ a[i]) + c
    s.add(x == l[i])
    s.add((x^a[i])+c == ll[i])


s.check()
m = s.model()

for i in range(n):
    print(chr(m[b[i]].as_long()), end='')

print()
