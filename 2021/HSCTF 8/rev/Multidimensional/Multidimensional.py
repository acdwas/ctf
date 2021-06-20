
from z3 import *

s = Solver()

a = [[Int(f'a_r={r}_c={c}') for c in range(6)] for r in range(6)]

prob = [Int(f'flag{i}') for i in range(36)]

def Multidimensional():
    global a
    global flag
    for i in range(36):
        a[i % 6][i // 6] = prob[i]

def line():
    global a
    b = [[Int(f'b_r={r}_c={c}') for c in range(6)] for r in range(6)]
    for i in range(6):
        for j in range(6):
            p = i - 1
            q = j - 1
            f = 0
            row = i % 2 == 0
            col = j % 2 == 0
            if row:
                p = i + 1
                f += 1
            else:
                f -= 1
            if col:
                q = j + 1
                f += 1
            else:
                f -= 1
            b[p][q] = a[i][j] + f
    a = b

	
def plane():
    global a
    n = 6
    for i in range(n // 2):
        for j in range(n // 2):
            t = a[j][n - 1 -i]
            a[j][n - 1 -i] = a[n - 1 - i][n - 1 - j]
            a[n - 1 - i][n - 1 - j] = a[n - 1 - j][i]
            a[n - 1 - j][i] = a[i][j]
            a[i][j] = t

    for i in range(6):
        for j in range(6):
            a[i][j] += i + n - j


def space(n):
    global a
    a[(35 - n) // 6][(35 - n) % 6] -= (n // 6) + (n % 6)
    if n != 0:
        n -= 1
        space(n)

	
def time():
    global a
    t = [[8, 65, -18, -21, -15, 55], 
            [8, 48, 57, 63, -13, 5], 
            [16, -5, -26, 54, -7, -2], 
            [48, 49, 65, 57, 2, 10], 
            [9, -2, -1, -9, -11, -10], 
            [56, 53, 18, 42, -28, 5]]
    
    for j in range(6):
        for i in range(6):
            a[i][j] += t[j][i]

Multidimensional()
line()
plane()
space(35)
time()

flag = b"hey_since_when_was_time_a_dimension?"

flag1 = []

x = 0

for i in range(6):
    b = []
    for j in range(6):
        b.append(flag[x])
        x += 1
    flag1.append(b)

for i in range(6):
    for j in range(6):
        s.add(flag1[i][j] == a[i][j])

s.check()
m = s.model()

print(''.join(chr(m[prob[i]].as_long()) for i in range(36)))

# flag{th3_g4t3w4y_b3t233n_d1m3n510n5}