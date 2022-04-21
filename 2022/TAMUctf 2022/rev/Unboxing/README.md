
# solver-template.py

``` py
from pwn import *
import r2pipe

p = remote("tamuctf.com", 443, ssl=True, sni="unboxing")
for binary in range(5):

	FILE = f"elf{binary}"

	with open(FILE, "wb") as file:
		file.write(bytes.fromhex(p.recvline().rstrip().decode()))

	ALF = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_='

	offset = 0x15100

	with open('sp.rr2', 'w') as f:
		s = f'#!/usr/bin/rarun2\n'
		s += f'program={FILE}\n'
		s += f'stdin="{ALF}"\n'
		s += f'stdout=\n'
		f.write(s)

	r2 = r2pipe.open(f'{FILE}')
	r2.cmd('e dbg.profile=sp.rr2')
	r2.cmd('doo')

	ADDR = r2.cmdj('dmj')[0]['addr']

	db = ADDR + 0x1224

	r2.cmd(f'db {db}')

	r2.cmd('dc')

	OO = ADDR+offset

	xx = []

	for i in r2.cmdj(f'pdj 190'):
		if 'movzx' in i['disasm']:
			addr = i['offset']+int(i['disasm'].split()[-1][:-1], 16)+i['size']
			if r2.cmd(f'px0 1 @{addr}').strip() == '':
				xx.append('00')
			else:
				xx.append(r2.cmd(f'px0 1 @{addr}').strip())
	
	X1= xx

	r2.quit()

	with open('sp1.rr2', 'w') as f:
		s = f'#!/usr/bin/rarun2\n'
		s += f'program={FILE}\n'
		s += f'stdin=stdio.txt\n'
		s += f'stdout=\n'
		f.write(s)

	r2 = r2pipe.open(f'{FILE}')
	r2.cmd('e dbg.profile=sp1.rr2')
	r2.cmd('doo')

	ADDR = r2.cmdj('dmj')[0]['addr']

	db = ADDR + 0x1224

	r2.cmd(f'db {db}')

	r2.cmd('dc')

	OO = ADDR+offset

	xx = []
	for i in r2.cmdj(f'pdj 190'):
		if 'movzx' in i['disasm']:
			addr = i['offset']+int(i['disasm'].split()[-1][:-1], 16)+i['size']
			xx.append(r2.cmd(f'px0 1 @{addr}').strip())

	X2 = xx

	r2.quit()

	w = [''] * 64

	for i in range(len(X1)):
		w[ALF.index(chr(int(X1[i], 16) ^ int(X2[i], 16)))] = chr(int(X2[i], 16))

	EEE = ''.join(w)

	p.sendline(f'{EEE}'.encode().hex().encode())

p.interactive()

```

# FLAG

**`gigem{unb0x1n6_74muc7f5_m057_3xclu51v3_fl46_ch3ck3r}`**



