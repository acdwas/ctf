
from pwn import *

r = remote('not-really-math.hsc.tf', 1337)

r.readline()

def to_list(s):
    a = ''
    tmp = []
    for i in range(len(s)):
        if s[i].isdigit():
            a += s[i]
        else:
            tmp.append(a)
            tmp.append(s[i])
            a = ''
    tmp.append(a)
    return tmp

def sum(s):
    tmp = []
    x = 0
    a = len(s)
    i = 0
    while i < a:
        if s[i] == 'a':
            tmp[x-1] = str(int(tmp[x-1]) + int(s[i+1]))
            i += 2
        else:
            tmp.append(s[i])
            x += 1
            i += 1
    return ''.join(tmp)

while True:
    l = r.readline().strip().decode()
    if 'flag' in l:
        print(l)
        break
    l = to_list(l)

    r.recvuntil(b': ')
    r.sendline(str(eval(sum(l).replace('m','*'))%4294967295))

# flag{yknow_wh4t_3ls3_is_n0t_real1y_math?_c00l_m4th_games.com}
