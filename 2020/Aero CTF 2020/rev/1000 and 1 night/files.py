from pwn import *

with open('file.txt') as f:
    s = f.read()

s = eval(s)

r = remote('tasks.aeroctf.com', 44324)

while True:
    w = r.readline()
    if b'Aero' in w:
        print('\n'+w.decode('utf-8'))
        break
    x = s[w.decode('utf-8').strip().split('<')[1][:-1]]
    r.recvuntil('Token: ')
    r.sendline(x)
