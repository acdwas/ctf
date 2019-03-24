
from pwn import *


flag = 'securinets{----------------------}'

i = 11
while i < len(flag):
    for x in '0123456789abcdefghijklmnopqrstuvwxyz}_':
        flag = list(flag)
        flag[i] = x
        try:
            os.remove('res')
            os.remove('lla')
        except:
            pass
        p = process('./rev')
        p.recvuntil('PASSWORD:', timeout=0.1)
        p.sendline(''.join(flag))

        for xxx in range(1000000):
            pass

        with open('ll', 'rb') as f:
            l = f.read()
        f.close()

        with open('res', 'rb') as f:
            ll = f.read()
        f.close()

        p.close()

        l = list(l)
        ll = list(ll)

        if l[i] == ll[i]:
            i += 1
            break

print '\n' + 'Flag: ' + ''.join(flag[:-1])
print
