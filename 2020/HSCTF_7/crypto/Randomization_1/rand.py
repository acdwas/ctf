
from pwn import *

def fun():
    with open("/dev/urandom", encoding='utf-8', errors='ignore') as f:
        x = ord(f.read(1))
    return x

def fun1(curr):
    curr = 37 * curr + 65
    return curr

# r = process('./rand1')
r = remote('crypto.hsctf.com', 6001)

x = fun()

print(r.readline())
u = int(r.readline().split()[-1])
# 
q = 0
for i in range(0xff+1):
    if (37*i+65)&0xff == u:
        q = i
        break 

q = fun1(q) & 0xff

for i in range(10):
    r.recvuntil('number: ')
    a = fun1(q) & 0xff
    r.sendline(str(a))
    q = a
print(r.recvall())

