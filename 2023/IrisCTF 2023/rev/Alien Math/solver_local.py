
from pwn import *

r = process('./srand_rand', level='error')

bb = r.recv().split(b'\n')

yy = []

for i in bb:
    yy.append([int(j) for j in i.split()])

yy = yy[:-1]

r.close()

l = [ b'\xe3\x83\xbb\xe2\x94\xa4\xe2\x94\xa4\xe2\x95\x99', 
    b'\xe3\x83\xbb\xe2\x94\x9c\xe2\x94\xb4\xe2\x95\x97\xe2\x95\xac', 
    b'\xe3\x83\xbb\xe2\x95\x9d\xe2\x94\x94\xe2\x94\xa4\xe2\x94\x90\xe2\x94\xbc', 
    b'\xe3\x83\xbb\xe2\x94\xac\xe2\x95\x92\xe2\x94\x98\xe2\x94\x80\xe2\x94\x94\xe2\x94\xb4', 
    b'\xe3\x83\xbb\xe2\x94\x9c\xe2\x95\xa1\xe2\x94\x8c\xe2\x94\x94\xe2\x94\xac\xe2\x95\xa5', 
    b'\xe3\x83\xbb\xe2\x94\xb4\xe2\x94\x90\xe2\x94\xa4\xe2\x94\xac', 
    b'\xe3\x83\xbb\xe2\x94\x94\xe2\x94\x80\xe2\x94\x90\xe2\x94\xa4\xe2\x94\x80\xe2\x94\xb4\xe2\x94\xb4', 
    b'\xe3\x83\xbb\xe2\x94\xac\xe2\x95\xa7\xe2\x94\x80\xe2\x94\x98\xe2\x95\xa3\xe2\x94\x90', 
    b'\xe3\x83\xbb\xe2\x94\x80' ]

rr = process('./alien_math', level='error')

rr.readline()
rr.readline()
rr.readline()
rr.readline()

for j in range(68):

    xx = yy[j][2]

    rr.readline()

    v3 = yy[j][1]
    v4 = yy[j][0]


    if xx == 1:
        r = process('./number', level='error')
        r.sendline(f'{v3-v4}'.encode())
        s = r.recv().decode()
        r.close()
    if xx == 2:
        r = process('./number', level='error')
        r.sendline(f'{v3^v4}'.encode())
        s = r.recv().decode()
        r.close()
    if xx == 3:
        r = process('./number', level='error')
        r.sendline(f'{(3 * v4) / v3}'.encode())
        s = r.recv().decode()
        r.close()
    if xx == 4:
        r = process('./number', level='error')
        r.sendline(f'{3 * v3 % (3 * v4)}'.encode())
        s = r.recv().decode()
        r.close()
    if xx == 5:
        r = process('./number', level='error')
        r.sendline(f'{v3 * v3 + v4}'.encode())
        s = r.recv().decode()
        r.close()
    if xx == 6:
        r = process('./number', level='error')
        r.sendline(f'{v3+v3-v4-v4}'.encode())
        s = r.recv().decode()
        r.close()

    w = b''

    for i in s:
        x = int(i)
        w += l[x]

    rr.sendline(w)

print(f'Flag: {rr.recv().split()[-1].decode()}')

