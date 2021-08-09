
import sys
import r2pipe

flag = ['A'] * 37 

x = 0
r2 = r2pipe.open('./vtr-alternate')
r2.cmd('e dbg.profile=vtr-alternate.rr2')
r2.cmd('db 0x403589')
# r2.cmd('doo')

while x < 37:
    
    for i in range(0x21, 0x7f):
        w = chr(i)
        flag[x] = w

        tmp = f"""
#!/usr/bin/rarun2
program=./vtr-alternate
stdin="{''.join(flag)}"
stdout=
        """

        with open('vtr-alternate.rr2', 'w') as f:
            f.write(tmp)
        f.close()

        r2.cmd('doo')
        r2.cmd('dc')

        r8 = r2.cmdj('drj')['r8']
        r8a = r8 - 160

        if r2.cmdj(f'pxwj @{r8}')[x] == r2.cmdj(f'pxwj @{r8a}')[x]:
            x += 1
            print(''.join(flag))
            break

print(''.join(flag))

# rarctf{See,ThatWasn'tSoHard-1eb519ed}
