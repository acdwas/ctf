
from z3 import *
from gmssl.sm4 import CryptSM4, SM4_DECRYPT

key = b'UBHPjBKlsQ2TuNSk'
iv = b'7y0M69TQScm7mfXv'

crypt_sm4 = CryptSM4()

crypt_sm4.set_key(key, SM4_DECRYPT)

s = Solver()

a = [BitVec(f'a{i}', 8) for i in range(32)]

a0 = Concat(a[0], a[1], a[2], a[3])
a1 = Concat(a[4], a[5], a[6], a[7])
a2 = Concat(a[8], a[9], a[10], a[11])
a3 = Concat(a[12], a[13], a[14], a[15])
a4 = Concat(a[16], a[17], a[18], a[19])
a5 = Concat(a[20], a[21], a[22], a[23])
a6 = Concat(a[24], a[25], a[26], a[27])
a7 = Concat(a[28], a[29], a[30], a[31])

rax = a0
rcx = -1817971763
rax = rax - rcx
s.add(rax == 0)
rcx = a1
rax = rax + rcx
rcx = 0x1337beef
rax = rax ^ rcx
rcx = 0x33aef5cb
rax = rax - rcx
s.add(rax == 0)
rcx = a2
rax = rax + rcx
rcx = a3
rdx = a4
rbx = rax
rax = rax ^ rdx
rbx = rbx ^ rcx
rdx = 0x550d68ce
rax = rax - rdx
s.add(rax == 0)
rdx = 0x5f9751eb
rbx = rbx - rdx
s.add(rbx == 0)
rax = rax + rbx
rcx = a5
rdx = a6
rcx = rcx + rax
rdx = rdx + rax
rax = a7
rdx = rdx ^ rax
rcx = rcx ^ rax
rax = 0x4aa34a4
rbx = 0x2c786553
rbx = rbx - rdx
s.add(rbx == 0)
rax = rax - rcx
s.add(rax == 0)
rax = rax + rbx
rcx = a2
rax = rax + rcx
rcx = a3
rdx = a4
rax = rax ^ rdx
rax = rax ^ rcx
rbx = 0x74180051
rax = rax - rbx
s.add(rax == 0)
rcx = a5
rax = rax + rcx
rcx = a6
rdx = a7
rax = rax ^ rdx
rax = rax ^ rcx
rbx = 0x3e07994c
rax = rax - rbx
s.add(rax == 0)

s.check()
m = s.model()

w = b''
for i in range(32):
    w += (m[a[i]].as_long()).to_bytes(1, 'little')

ww = crypt_sm4.crypt_cbc(iv, w)
print(ww)

# bi0s{jitrustyjeRPUGEbTa}
