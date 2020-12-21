
from pwn import *

r = remote('challs.xmas.htsp.ro', 6051)

xx = 1

while True:
    r.recvuntil('array = [')
    x = r.recvuntil(']\n').decode().replace(' ', '').strip()[:-1].split(',')
    r.recvuntil('k1 = ')
    k1 = int(r.recvuntil('\n').decode().strip())
    r.recvuntil('k2 = ')
    k2 = int(r.recvuntil('\n').decode().strip())
    x.sort(key=int)
    w = ''
    for i in x[:k1]:
        w += i + ', '
    w = w[:-2]
    w += '; '
    x = x[::-1]
    for i in x[:k2]:
        w += i + ', '

    w = w[:-2]
    r.sendline(w)
    if xx == 50:
        print(r.recv().decode().split('\n')[2])
        break
    else:
        xx += 1
