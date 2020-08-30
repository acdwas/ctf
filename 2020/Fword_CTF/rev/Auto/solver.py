
from pwn import *
from z3 import *

s = Solver()

a = [BitVec('a{}'.format(i), 32) for i in range(2)]


def fun_dis(l):
    a = int(disasm(l[0x12f3:0x12f3+7]).split()[-1], 16)
    b = int(disasm(l[0x1319:0x1319+3]).split()[-1], 16)
    c = int(disasm(l[0x131c:0x131c+5]).split()[-1], 16)
    d = int(disasm(l[0x134a:0x134a+5]).split()[-1], 16)
    e = int(disasm(l[0x1370:0x1370+5]).split()[-1], 16)
    return [a, b, c, d, e]


key = ''

for i in range(400):
    file_r = './out{}'.format(str(i).rjust(3, '0'))
    with open(file_r, 'rb') as f:
        l = f.read()
    f.close()
    l = fun_dis(l)

    s.add(And((a[1] + a[0] + l[0] >> l[1] == l[2]),
              ((a[1] ^ a[0]) + a[0] == l[3])), (a[1] * a[0] == l[4]))

    if s.check() == sat:
        m = s.model()
        w = chr(m[a[0]].as_long()) + chr(m[a[1]].as_long())
        # print(w)
        key += w
    else:
        print(file_r)
    s.reset()

print(key)

# VPVGL2gI1JXDKRGFiXu0vo8IfD9H7cJJxcQTaHgcfYeEPWM0Zr5gcPSCYmVdRGmfaWJ5Li
# XZm3tOkZqjftZChjVDxvIRvfr0vSQSQVde1iCnghgETVxA8ZBvp81Fn2sWLtQJ5rjDOk07
# hg2tXb25mbqEFvizhg6yVucm93d9DXxD8ravHVeudANWrXlXGWokyrKLetD2Zr5dhSc42d
# D6LPbE8oAFgo5xga9LQSLfWbbuBNfJhVf2kDg1gUIyKdXPsQsqQpZ2pX59Ym3GmpA6zhJe
# 37xoZLSPwrkNShq0SUm5gcZ9PBKAC40auNu9Dzs0nNYvGiLIkmPYJagbGBWy8L7Fk4APAV
# Yz6a7cFRQsRukkLCOP3CyA5YyzinlJMI3b1a9gtD63qifRaSUCHmK2KvOESF9I0XSZPAHf
# p72FAZhP

# FwordCTF{4r3_Y0u_4_r0b0t}

# P2aNT6KqIyaBdLy43mrI4qX2UkOe3bGIfi5xGGGVnLUhcYQ5nzufy9LcOGSI0tYn97Wc03
# Or39p8fF2VfR34cLm2XghPt4FadcelMMj4eVHShF3gGv8CpVf2QGA5gDT3t33xkKdlUfFK
# XeShnVXwSjClwlpzMSOqZOuVTWX1fb1T1Zg7Zf0J6507z3bKV1V9PXkRguIrpSTt0h2AbH
# dmkZ1ZiMmBfK7KiZ1jRALr1zvNRskh9tpRQDTZ5j2XcCtDCvb2UBvrxEW2mU9OnQlk1368
# wzfbFAVsLfbn0F0HP6iS52Olv40jKOXTQoU0clQqnZ6TcHnFq4HaLpeu6t5i6yZflHh


