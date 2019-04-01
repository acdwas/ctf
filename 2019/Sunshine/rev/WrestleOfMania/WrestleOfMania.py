
# sysctl kernel.randomize_va_space=0
# python WrestleOfMania.py 2>/dev/null

import sys
import r2pipe

r2 = r2pipe.open('./WrestleOfMania')
r2.cmd('doo')
r2.cmd('e dbg.profile=WrestleOfMania.rr2')
r2.cmd('db 0x565559e4')


def run():
    r2.cmd('doo')
    r2.cmd('dc')


def fun2(s):
    with open('WrestleOfMania.rr2', 'w') as f:
        w = ''
        w = '#!/usr/bin/rarun2' + '\n'
        w += 'program=./WrestleOfMania' + '\n'
        w += 'stdin=' + '"' + s + '"' + '\n'
        w += 'stdout=' + '\n'
        f.write(w)
    f.close()


flag = 'sun{AAAAAAAAAAAAAAAAAAAAAAAAA}'
alf = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'

i = 4
while i < len(flag) - 1:
    for c in alf:
        flag = list(flag)
        flag[i] = c
        fun2(''.join(flag))
        run()
        j = i
        while j > 0:
            r2.cmd('dc')
            j -= 1
        reg = r2.cmdj('drj')
        eax = reg['eax']
        edx = reg['edx']
        if eax == edx:
            sys.stdout.write('\r' + ''.join(flag))
            sys.stdout.flush()
            i += 1
            break
print
