
from pwn import *

r = process('./elsewhere_patch')

r.readline()

r.sendline(b'\x00' * 0x40 + b'\n')

v = r.read(0x40)

r.close()

# 0x6aa10d9d27909470	0x2fada5679377201a
# 0x2a8ed71020c14304	0x4192b63616879f0f
# 0xbb39d98de2d5e07c	0xe9aabebb74c35a5e
# 0xb5a57bc7e7882e7e	0xdf9575437ccdecd4


x = [ 0x2fada5679377201a6aa10d9d27909470, 0x4192b63616879f0f2a8ed71020c14304, 0xe9aabebb74c35a5ebb39d98de2d5e07c, 0xdf9575437ccdecd4b5a57bc7e7882e7e]

k = []

for i in range(0, len(v), 16):
    k.append(int.from_bytes(v[i:i+16], byteorder='little'))

w = b''

for a,b in zip(x,k):
    w += bytes.fromhex(hex(a^b)[2:])[::-1]

print()
print()
print(w.decode())

