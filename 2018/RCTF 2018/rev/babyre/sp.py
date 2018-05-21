
# python sp.py 2>/dev/null

import sys
import r2pipe
import random
import string
import sys

r2 = r2pipe.open('./babyre')

l = [0xB80C91FE, 0x70573EFE,
     0xBEED92AE, 0x7F7A8193,
     0x7390C17B, 0x90347C6C,
     0xAA7A15DF, 0xAA7A15DF,
     0x526BA076, 0x153F1A32,
     0x545C15AD, 0x7D8AA463,
     0x526BA076, 0xFBCB7AA0,
     0x7D8AA463, 0x9C513266,
     0x526BA076, 0x6D7DF3E1,
     0xAA7A15DF, 0x9C513266,
     0x1EDC3864, 0x9323BC07,
     0x7D8AA463, 0xFBCB7AA0,
     0x153F1A32, 0x526BA076,
     0xF5650025, 0xAA7A15DF,
     0x1EDC3864, 0xB13AD888]


def run():
    r2.cmd('db 0x08048965')
    r2.cmd('e dbg.profile=sp.rr2')
    r2.cmd('doo')
    r2.cmd('dc; sr eip')


def zap(i, j):
    with open('plik.txt', 'w') as f:
        f.write('%s\n' % (''.join(random.sample(string.ascii_letters, 15))))
        f.write('%d\n' % i)
        f.write('%s' % j * 30)


b = 0
w = ''
while 1:
    for x in range(0xff):
        zap(10, chr(x))
        run()
        a = r2.cmd('pxw 4 @ %d' % (r2.cmdj('drj')['ebp'] - 0x0c)).split()[1]
        if int(a, 16) == l[b]:
            w += chr(x)
            out = "Flag: " + w
            sys.stdout.write('\r' + out)
            sys.stdout.flush()
            b += 1
            break
    if b == 30:
        break
print
