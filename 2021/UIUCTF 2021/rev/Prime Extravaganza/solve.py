
from z3 import *
import hashlib

s = Solver()

a = [BitVec(f'a{i}', 32) for i in range(5)]

for i in range(5):
    x = 19753 * (i + 1)
    s.add(a[i] < 100000, a[i] > 0)
    s.add(a[i] % x == 0)

value = []

while s.check() == sat:
    m = s.model()

    w = []
    for i in range(5):
        w.append(m[a[i]].as_long())
    value += w
    s.add(Or(a[0] != s.model()[a[0]],
        a[1] != s.model()[a[1]],
        a[2] != s.model()[a[2]],
        a[3] != s.model()[a[3]],
        a[4] != s.model()[a[4]] ))

print('uiuctf{' + hashlib.md5(str(sum(set(value))).encode()).hexdigest() + '}')

# uiuctf{627360eb8aa0da45ff04a514dab40e54}

