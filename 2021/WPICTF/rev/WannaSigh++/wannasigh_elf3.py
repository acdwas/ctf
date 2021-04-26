
from pwn import *
import ctypes
import random

with open('your-flag.ransomed', 'rb') as f:
	flag_enc = f.read()

# wannasigh109fn10fn48vh.wpictf.xyz == 69.164.222.170

r = remote('69.164.222.170', 18610)

r.sendline('Baahhhh_192.168.1.{}'.format(random.randint(0,256)))

seed = int(r.recv())
libsystem = ctypes.CDLL('libc.so.6')

libsystem.srand(seed)

key = []

for i in range(len(flag_enc)):
  key.append(libsystem.rand())

flag = ''

for i in range(len(flag_enc)):
  flag += chr((key[i] ^ flag_enc[i]) & 0xff)

print('\n',flag)

# WPI{backup-your-files}

