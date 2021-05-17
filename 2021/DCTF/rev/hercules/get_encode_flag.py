
from pwn import *

s = {}

for i in range(100):
    r = remote('dctf-chall-hercules.westeurope.azurecontainer.io', 5569)
    l = r.readline()
    ll = r.readline()
    s[l] = ll
    r.close()

with open('plik.txt', 'w+') as f:
    for k,v in s.items():
        w = ''
        w = k.decode().strip() + ' ' + v.decode()
        f.write(w)