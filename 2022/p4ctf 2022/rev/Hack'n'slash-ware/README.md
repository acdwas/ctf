
# hack-n-slash_enc.py

```py
import itertools, sys, os

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def hack(a,b):
    return pow(a, 0x10001, 0x6c7bd55985a8fb0991e07a947dd39d29)

def slash(a,b):
    return pow(a, 0x10001, 0x7838f58b2ab7ca1e35a5a0d5371f3917)


def quack_data(data):
    return b''.join([b[0](int.from_bytes(a, 'little'), b[1]).to_bytes(16, 'little') for a, b in zip(chunks(data, 15), itertools.cycle([(x, y) for x, y in zip([hack, slash], [105, 42])]))])


def main() -> None:
    filename = sys.argv[1]
    if not filename.endswith('.encrypt_me'):
        raise AssertionError
    with open(filename, 'rb') as (f):
        data = f.read()
    os.remove(filename)
    with open(f"{filename}.hacked_and_slashed", 'wb') as (f):
        f.write(quack_data(data))


if __name__ == '__main__':
    main()
```

# p4_ctf.nasm

```nasm
bits 64

section .text
global _start

_start:
    mov        rax, 105
    movd       xmm0,eax
    movdqa     xmm1, [dat_00394e90]
    punpcklbw  xmm0,xmm0
    punpcklwd  xmm0,xmm0
    pshufd     xmm0,xmm0,0x0
    pxor       xmm1,xmm0
    pxor       xmm0, [dat_00394ea0]
    movaps     [tmp+0x10],xmm0
    movaps     [tmp],xmm1

    mov        rax, 1
    mov        rdi, 1
    mov        rsi, hack
    mov        rdx, 15
    syscall

    mov        rax, 1
    mov        rdi, 1
    mov        rsi, tmp
    mov        rdx, 33
    syscall

    pxor        xmm0, xmm0
    pxor        xmm1, xmm1

    mov        rax, 42
    movd       xmm0,eax
    movdqa     xmm1, [dat_00394e70]
    punpcklbw  xmm0,xmm0
    punpcklwd  xmm0,xmm0
    pshufd     xmm0,xmm0,0x0
    pxor       xmm1,xmm0
    pxor       xmm0, [dat_00394e80]
    movaps     [tmp+0x10],xmm0
    movaps     [tmp],xmm1

    mov        rax, 1
    mov        rdi, 1
    mov        rsi, slash
    mov        rdx, 15
    syscall

    mov        rax, 1
    mov        rdi, 1
    mov        rsi, tmp
    mov        rdx, 33
    syscall

    mov        eax, 60
    xor        rdi, rdi
    syscall

section .data
    dat_00394e70 db 0x1d, 0x12, 0x19, 0x12, 0x4c, 0x1f, 0x12, 0x48, 0x18, 0x4b, 0x48, 0x1d, 0x49, 0x4b, 0x1b, 0x4f
    dat_00394e80 db 0x19, 0x1f, 0x4b, 0x1f, 0x4b, 0x1a, 0x4e, 0x1f, 0x19, 0x1d, 0x1b, 0x4c, 0x19, 0x13, 0x1b, 0x1d 
    dat_00394e90 db 0x5f, 0x0a, 0x5e, 0x0b, 0x0d, 0x5c, 0x5c, 0x50, 0x51, 0x5c, 0x08, 0x51, 0x0f, 0x0b, 0x59, 0x50
    dat_00394ea0 db 0x50, 0x58, 0x0c, 0x59, 0x5e, 0x08, 0x50, 0x5d, 0x5e, 0x0d, 0x0d, 0x5a, 0x50, 0x0d, 0x5b, 0x50
    tmp times   34  db  0x0a, 0x00
    hack    db  "hack  -> n = 0x", 0x00
    slash    db  "slash -> n = 0x", 0x00

; hack  -> n = 0x6c7bd55985a8fb0991e07a947dd39d29
; slash -> n = 0x7838f58b2ab7ca1e35a5a0d5371f3917
```

# hack-n-slash_solve.py

```py
from crypto_commons.rsa.rsa_commons import modinv
import itertools

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def hack(a):
    n = 0x6c7bd55985a8fb0991e07a947dd39d29
    p = 10830293516065295497 
    q = 13314468632857240481

    phi = (p-1)*(q-1)
    d = modinv(0x10001, phi)

    return bytes.fromhex(hex(pow(int.from_bytes(a, 'little'), d, n))[2:].rjust(30, '0'))[::-1]

def slash(a):
    n = 0x7838f58b2ab7ca1e35a5a0d5371f3917
    p = 10963757462568095959 
    q = 14575578571502293441

    phi = (p-1)*(q-1)
    d = modinv(0x10001, phi)

    return bytes.fromhex(hex(pow(int.from_bytes(a, 'little'), d, n))[2:].rjust(30, '0'))[::-1]

def quack_data(data):
    return b''.join([b(a) for a, b in zip(chunks(data, 16), itertools.cycle([hack, slash]))])



with open('./flag.png.encrypt_me.hacked_and_slashed', 'rb') as f:
    l = f.read()

with open('p4_ctf.png', 'wb') as f:
    f.write(quack_data(l))
```

