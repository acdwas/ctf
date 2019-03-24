
from pwn import *

ll = [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48,
      0x49, 0x4b, 0x4c, 0x4d, 0x4e, 0x4f, 0x50,
      0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57,
      0x58, 0x59, 0x5a]


b = [0] * 28

x = 0
y = 0
s = 'AAAAAAAAAAAAAA'
while x < 28:
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        s = list(s)
        s[y] = i
        v16 = 0
        for k in range(14):
            for l in range(5):
                for m in range(5):
                    if ll[m + 5 * l] == ord(s[k]):
                        b[v16] = l + 65
                        v4 = v16 + 1
                        b[v4] = m + 49
                        v16 = v4 + 1
        w = ''
        for i in range(len(b)):
            w += chr(i % 4 ^ b[i])
        if w[:x + 2] == "B0C2A2C6A3A7C5@6B5F0A4G2B5A2"[:x + 2]:
            x += 2
            y += 1
            break

p = process('./rev')
p.recvuntil('PASSWORD:', timeout=0.1)
p.sendline(''.join(s))
w= p.recv()
print '\n' + w + '\n'



