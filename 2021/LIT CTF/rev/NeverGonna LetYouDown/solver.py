
from z3 import *

def fun(param_1, param_2, param_3):
  return param_2 & 0xfffffffe | param_3 >> (param_1 & 0x1f) & 1

s = Solver()

a = [BitVec(f'a{i}', 32) for i in range(50)]
x = [BitVec(f'x{i}', 32) for i in range(400)]

with open("yougotrickrolled1.bmp", "rb") as f:
    l1 = f.read()
with open("yougotrickrolled2.bmp", "rb") as f:
    l2 = f.read()
with open("yougotrickrolled3.bmp", "rb") as f:
    l3 = f.read()

# i = 0
# while i < len(l1):
#     if l1[i] == l2[i] == l3[i]:
#         pass
#     else:
#         print(i)
#     i += 1

l = []

for i in range(4800,5200):
    if l1[i] == l2[i]:
        l.append(l3[i])
    elif l1[i] == l3[i]:
        l.append(l2[i])
    elif l2[i] == l3[i]:
        l.append(l1[i])

g = 0

for i in range(50):
    for j in range(8):
        s.add(fun(j, x[g], a[i] ^ 0x68) == l[g])
        g += 1

s.check()
m = s.model()

w = ''

for i in range(50):
    w += chr(m[a[i]].as_long())

print(w)

# flag{r1ck_4stley_1s_n3ver_ev3r_g0nna_l3t_y0u_d0wn}