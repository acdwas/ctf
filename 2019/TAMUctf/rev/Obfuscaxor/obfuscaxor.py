import sys
import r2pipe

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+*{}'"

r2 = r2pipe.open('./obfuscaxor')
r2.cmd('e dbg.profile=yyy.rr2')


def fun():
    r2.cmd('doo')
    addr = r2.cmdj('dmj')[0]['addr'] + 0x20b9
    r2.cmd('db %d' % addr)
    r2.cmd('dc')
    return addr


def fun2(s):
    with open('yyy.rr2', 'w') as f:
        w = ''
        w = '#!/usr/bin/rarun2' + '\n'
        w += 'program=./obfuscaxor' + '\n'
        w += 'stdin=' + '"' + s + '"' + '\n'
        w += 'stdout=' + '\n'
        f.write(w)
    f.close()


flag = ['-'] * 16

i = 0
while i < 16:
    for j in charset:
        flag[i] = j
        fun2("".join(flag))
        addr = fun()
        rsi = r2.cmdj('pxj 16 @rsi')
        rdi = r2.cmdj('pxj 16 @rdi')
        r2.cmd('db - %d' % addr)
        if rsi[i] == rdi[i]:
            i += 1
            sys.stdout.write('\r' + "".join(flag))
            sys.stdout.flush()
            break
print
