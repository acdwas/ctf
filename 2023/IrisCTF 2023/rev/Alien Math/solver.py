
from pwn import *

import base64
import os
import secrets
import socket
import sys
import hashlib

try:
    import gmpy2
    HAVE_GMP = True
except ImportError:
    HAVE_GMP = False
    sys.stderr.write("[NOTICE] Running 10x slower, gotta go fast? pip3 install gmpy2\n")

VERSION = 's'
MODULUS = 2**1279-1
CHALSIZE = 2**128

SOLVER_URL = 'https://goo.gle/kctf-pow'

def python_sloth_root(x, diff, p):
    exponent = (p + 1) // 4
    for i in range(diff):
        x = pow(x, exponent, p) ^ 1
    return x

def python_sloth_square(y, diff, p):
    for i in range(diff):
        y = pow(y ^ 1, 2, p)
    return y

def gmpy_sloth_root(x, diff, p):
    exponent = (p + 1) // 4
    for i in range(diff):
        x = gmpy2.powmod(x, exponent, p).bit_flip(0)
    return int(x)

def gmpy_sloth_square(y, diff, p):
    y = gmpy2.mpz(y)
    for i in range(diff):
        y = gmpy2.powmod(y.bit_flip(0), 2, p)
    return int(y)

def sloth_root(x, diff, p):
    if HAVE_GMP:
        return gmpy_sloth_root(x, diff, p)
    else:
        return python_sloth_root(x, diff, p)

def sloth_square(x, diff, p):
    if HAVE_GMP:
        return gmpy_sloth_square(x, diff, p)
    else:
        return python_sloth_square(x, diff, p)

def encode_number(num):
    size = (num.bit_length() // 24) * 3 + 3
    return str(base64.b64encode(num.to_bytes(size, 'big')), 'utf-8')

def decode_number(enc):
    return int.from_bytes(base64.b64decode(bytes(enc, 'utf-8')), 'big')

def decode_challenge(enc):
    dec = enc.split('.')
    if dec[0] != VERSION:
        raise Exception('Unknown challenge version')
    return list(map(decode_number, dec[1:]))

def encode_challenge(arr):
    return '.'.join([VERSION] + list(map(encode_number, arr)))

def get_challenge(diff):
    x = secrets.randbelow(CHALSIZE)
    return encode_challenge([diff, x])

def solve_challenge(chal):
    [diff, x] = decode_challenge(chal)
    y = sloth_root(x, diff, MODULUS)
    return encode_challenge([y])

def can_bypass(chal, sol):
    from ecdsa import VerifyingKey
    from ecdsa.util import sigdecode_der
    if not sol.startswith('b.'):
        return False
    sig = bytes.fromhex(sol[2:])
    with open("/kctf/pow-bypass/pow-bypass-key-pub.pem", "r") as fd:
        vk = VerifyingKey.from_pem(fd.read())
    return vk.verify(signature=sig, data=bytes(chal, 'ascii'), hashfunc=hashlib.sha256, sigdecode=sigdecode_der)

def verify_challenge(chal, sol, allow_bypass=True):
    if allow_bypass and can_bypass(chal, sol):
        return True
    [diff, x] = decode_challenge(chal)
    [y] = decode_challenge(sol)
    res = sloth_square(y, diff, MODULUS)
    return (x == res) or (MODULUS - x == res)


rr = remote('alien.chal.irisc.tf', 10600, level='error')
ll = rr.recvuntil(b'? ', timeout=0.5).split()[-3]


challenge = ll.decode()
solution = solve_challenge(challenge)

if verify_challenge(challenge, solution, False):
    xxx = solution

rr.sendline(xxx.encode())

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

# rr = process('./alien_math', level='error')

rr.readline()
rr.readline()
rr.readline()
rr.readline()
rr.readline() # <-- add end competitions

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


rr.recv()
print(f'Flag: {rr.recv().split()[-1].decode()}')

# irisctf{w3_are_4_f1ng3r3d_cr34tur3s}
