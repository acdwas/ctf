
#AP Lab: English Language

s = "1dd3|y_3tttb5g`q]^dhn3j"

l = [4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3]

t = [11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]

p = ['']*23

def fun_x(s):
    w = ''
    for i in range(23):
        w += chr(ord(s[i])^l[i])
    return w

def fun_t(s):
    for i in range(23):
        p[t[i]] = s[i]
    return ''.join(p)

for i in range(3):
    s = fun_x(s)    
    s = fun_t(s)

print(s)