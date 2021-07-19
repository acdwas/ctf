
#!/usr/bin/python3
import random

def unshuffle(l, seed):
    random.seed(seed)
    perm = list(range(len(l)))
    random.shuffle(perm)
    res = [None] * len(l)
    for i, j in enumerate(perm):
        res[j] = l[i]
    l[:] = res

for i in range(1, 1000):
    l = list('zftr}__g5y_ee0y1{graua00n1l')
    unshuffle(l, i)
    w = ''.join(l)
    if 'flag' in w:
        print(w)
        break

# flag{y0u_are_gen1051ty_0rz}