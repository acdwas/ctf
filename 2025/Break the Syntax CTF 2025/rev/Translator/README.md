
## solve.py

```py

from z3 import *

s = Solver()

def sub_555555555270(a1):
    if len(a1) < 4:
        return BitVecVal(0, 16)

    v1 = a1[0]

    def fun_v1(v1):
        return v1 & 0xff

    If(v1 == 0, fun_v1(v1), v1)

    v3 = a1[1]

    def fun_v3(v1, v3):
        v1 >>= 4
        return (v3 + v1) & 0xff
    
    If(v3 == 0, fun_v3(v1, v3), v3)

    v4 = a1[2]

    def fun_v4(v3, v1, v4):
        v3 >>= 4
        v3 += v4
        v1 >>= 4
        return (v3 + v1) & 0xff
    
    If(v4 == 0, fun_v4(v3, v1, v4), v4)

    v5 = a1[3]

    def fun_v5(v4, v3, v1, v5):
        v3 >>= 4
        v3 += v4
        v1 >>= 4
        return (v3 + v1) & 0xff
    
    If(v5 == 0, fun_v5(v4, v3, v1, v5), v5)

    return ( 
        sub_555555555270(a1[4:]) +
        LShR(v5, 4) +
        LShR(v4, 4) +
        LShR(v3, 4) +
        LShR(v1, 4)     )

l = [ 0x5E7E, 0x6E42, 0x6F4C, 0x8554, 0x4A58, 0x6862, 0x8C5D, 0x8A67, 0x4B61, 0x4775, 
     0x656F, 0x4868, 0x5271, 0x6327, 0x4369, 0x7877, 0x7A4F, 0x7F63, 0x3221, 0x4A25, 
     0x8D07 ]

a = [BitVec(f'a_{i}', 16) for i in range(46)]
b = [BitVec(f'b{i}', 8) for i in range(46)]

s.add(a[-1] == 0)
s.add(a[-2] == 0)
s.add(a[-3] == 0)
s.add(a[-4] == 0)
s.add(a[-5] == 0)
s.add(b[-1] == 0)
s.add(b[-2] == 0)
s.add(b[-3] == 0)
s.add(b[-4] == 0)
s.add(b[-5] == 0)

for i in range(len(a)):
    a[i] = ZeroExt(8, b[i])

ll = []

for i in range(0, len(a), 2):

    rax = sub_555555555270(a[i+1:])

    r9 = a[i]
    rdx = r9
    rcx = a[i+1]

    rdx >>= 4
    rdx += rax
    rax = rdx
    rdx += rcx
    rcx &= 0xF0
    rax >>= 4
    rdx &= 0x0f
    rax += r9
    r9 &= 0xF0
    rdx |= rcx
    rax &= 0x0F
    rax |= r9
    rax <<= 8

    ll.append(rax + rdx + 0x1000)

for i in range(len(l)):
    s.add(ll[i] == l[i])

if s.check() == sat:
    m = s.model()
    result = ''.join([chr(m.eval(c).as_long()) for c in b])
    print("Znaleziono rozwiązanie:", result)
else:
    print("Nie znaleziono rozwiązania.")
```


# FLAG

**`BtSCTF{W0W_it_re4l1y_m3aNs_$0methIng!!:)}`**



