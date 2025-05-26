
## solver.py

```py
from z3 import *

s = Solver()

ss = 'm7xzr7muqtxsr3m8pfzf6h5ep738ez5ncftss7d1cftskz49qj4zg7n9cizgez5upbzzr7n9cjosg45wqjosg3mu'

a = [BitVec(f'a{i}', 8) for i in range(55)]

for i in range(55):
    s.add(And(a[i] > 0x20, a[i] < 0x7f))

w = [ord(i) for i in 'ybndrfg8ejkmcpqxot1uwisza345h769']

A = Array('A', BitVecSort(8), BitVecSort(8))

for i in range(len(w)):
    A = Store(A, i, w[i])

ww = [0] * 88
x = 0

for i in range(0, 55, 5):
    ww[x] = Select(A, a[i] >> 3)
    ww[x+1] = Select(A, (((a[i] << 2 ) & 0xff) | (a[i+1] >> 6)) & 0x1f)
    ww[x+2] = Select(A, (a[i+1] >> 1) & 0x1f)
    ww[x+3] = Select(A, (((a[i+1] << 4) & 0x1f) | (a[i+2] >> 4)) & 0x1f)
    ww[x+4] = Select(A, ((a[i+2] * 2) | (a[i+3] >> 7)) & 0x1f)
    ww[x+5] = Select(A, (a[i+3] >> 2) & 0x1f)
    ww[x+6] = Select(A, (((a[i+3] << 3) & 0xff) | (a[i+4] >> 5)) & 0x1f)
    ww[x+7] = Select(A, a[i+4] & 0x1f)

    x += 8

for i in range(88):
    s.add(ww[i] == ord(ss[i]))

s.check()
m = s.model()

print(''.join(chr(m[a[i]].as_long()) for i in range(55)))
```

### password = __rust_begin_short_backtrace__rust_end_short_backtraces

# FLAG

**`flag{50768fcb270edc499750ea64dc45ee92}`**

