import sys
import r2pipe

r2 = r2pipe.open('./triptych')
r2.cmd('e dbg.profile=triptych.rr2')


def fun():
    r2.cmd('doo')
    r2.cmd('db 0x0000000000400ac1')
    i = 0
    while i < 245:
        r2.cmd('dc')
        i += 1
    r2.cmd('db 0x00000000004009cb')
    r2.cmd('dc')
    r2.cmd('dc')
    i = 0
    while i < 245:
        r2.cmd('dc')
        i += 1
    r2.cmd('db 0x00000000004008d5')
    r2.cmd('dc')
    r2.cmd('dc')
    i = 0
    while i < 351:
        r2.cmd('dc')
        i += 1
    r2.cmd('db 0x00000000004007ce')
    r2.cmd('dc')


def file_write(s):
    w = ''
    w += "#!/usr/bin/rarun2\n"
    w += "program=./triptych\n"
    w += 'stdin=' + '"' + s + '"'
    w += "\nstdout="
    with open('triptych.rr2', 'w') as f:
        f.write(w)


flag = ['f', 'l', 'a', 'g', '{', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '}']
i = 5
while i < 25:
    for x in range(0x5f, 0x7f):
        flag[i] = chr(x)
        file_write(''.join(flag))
        fun()
        a = i
        while a > 0:
            r2.cmd('dc')
            a -= 1
        drj = r2.cmdj('drj')
        rax = drj['rax']
        rdx = drj['rdx']
        if rax == rdx:
            sys.stdout.write('\r' + ''.join(flag))
            sys.stdout.flush()
            i += 1
            break
