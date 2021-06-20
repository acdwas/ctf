
from pwn import *

r = remote('not-really-math.hsc.tf', 1337)

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
    for i in range(len(s)):
        if s[i] == '+':
            if s[i-1] == '|':
                pass
            else:
                s[i-1] = str(int(s[i-1]) + int(s[i+1]))
                s[i] = '|'
                s[i+1] = '|'
    result = filter(lambda val: val !=  '|', s) 
    return list(result)

def find_p(s):
    for i in range(len(s)):
        if s[i] == '+':
            return True
    return False

r.readline()

while True:
    l = r.readline().strip().decode()
    if 'flag' in l :
        print('\n',l,'\n')
        break
    l = l.replace('m','*').replace('a','+')
    l = to_list(l)
    w = ''
    while True:
        if find_p(l):
            l = sum(l)
        else:
            break
    for i in sum(l):
        w += i

    r.recvuntil(b': ')
    r.sendline(str(eval(w)%4294967295))

# flag{yknow_wh4t_3ls3_is_n0t_real1y_math?_c00l_m4th_games.com}