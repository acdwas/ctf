
```py

from z3 import *

s = Solver()

a = [BitVec(f'a{i}', 32) for i in range(48)]

for i in range(48):
	s.add(And(a[i] > 0x20, a[i] < 0x7f))

def sub_401210(x):
	global a
	return And(a[x + 0] == 98, a[x + 1] == 119, a[x + 2] == 99, a[x + 3] == 116, a[x + 4] == 102, a[x + 5] == 123, a[x + 47] == 125)

def sub_401240(x):
	global a
	return And(a[x + 3] == 45, a[x + 9] == 45, a[x + 15] == 45, a[x + 21] == 45, a[x + 27] == 45, a[x + 33] == 45)

def sub_401270(x):
	global a
	return a[x + 13] < a[x + 14]

def sub_401280(x):
	global a
	return a[x + 2] ^ a[x + 30] == 100

def sub_401290(x):
	global a
	return a[x + 14] < a[x + 17]

def sub_4012A0(x):
	global a
	return a[x + 2] * a[x + 8] == 7654

def sub_4012C0(x):
	global a
	return a[x + 5] < a[x + 32]

def sub_4012D0(x):
	global a
	return a[x + 12] > a[x + 30]

def sub_4012E0(x):
	global a
	return a[x + 12] == a[x + 31]

def sub_4012F0(x):
	global a
	return a[x + 0] * a[x + 14] == 3417

def sub_401310(x):
	global a
	return a[x + 1] > a[x + 3]

def sub_401320(x):
	global a
	return a[x + 7] < a[x + 13]

def sub_401330(x):
	global a
	return a[x + 8] > a[x + 21]

def sub_401340(x):
	global a
	return a[x + 28] + a[x + 34] == 103

def sub_401360(x):
	global a
	return a[x + 10] ^ a[x + 11] == 102

def sub_401370(x):
	global a
	return a[x + 1] ^ a[x + 19] == 102

def sub_401380(x):
	global a
	return a[x + 15] + a[x + 23] == 133

def sub_4013A0(x):
	global a
	return a[x + 10] + a[x + 41] == 146

def sub_4013C0(x):
	global a
	return a[x + 4] + a[x + 40] == 126

def sub_4013E0(x):
	global a
	return a[x + 7] > a[x + 23]

def sub_4013F0(x):
	global a
	return a[x + 2] < a[x + 32]

def sub_401400(x):
	global a
	return a[x + 5] ^ a[x + 13] == 97

def sub_401410(x):
	global a
	return a[x + 18] ^ a[x + 26] == 101

def sub_401420(x):
	global a
	return a[x + 2] < a[x + 28]

def sub_401430(x):
	global a
	return a[x + 0] == a[x + 10]

def sub_401440(x):
	global a
	return a[x + 10] * a[x + 19] == 6699

def sub_401460(x):
	global a
	return a[x + 12] ^ a[x + 18] == 123

def sub_401470(x):
	global a
	return a[x + 4] ^ a[x + 14] == 21

def sub_401480(x):
	global a
	return a[x + 5] < a[x + 30]

def sub_401490(x):
	global a
	return a[x + 21] ^ a[x + 22] == 14

def sub_4014A0(x):
	global a
	return a[x + 13] * a[x + 33] == 4335

def sub_4014C0(x):
	global a
	return a[x + 12] ^ a[x + 27] == 10

def sub_4014D0(x):
	global a
	return a[x + 2] ^ a[x + 22] == 28

def sub_4014E0(x):
	global a
	return a[x + 21] > a[x + 42]

def sub_4014F0(x):
	global a
	return a[x + 11] > a[x + 30]

def sub_401500(x):
	global a
	return a[x + 14] == a[x + 31]

def sub_401510(x):
	global a
	return a[x + 14] * a[x + 18] == 4264

def sub_401530(x):
	global a
	return a[x + 15] < a[x + 19]

def sub_401540(x):
	global a
	return a[x + 14] + a[x + 15] == 132

def sub_401560(x):
	global a
	return a[x + 5] * a[x + 28] == 3840

def sub_401580(x):
	global a
	return a[x + 2] + a[x + 12] == 135

def sub_4015A0(x):
	global a
	return a[x + 14] + a[x + 17] == 103

def sub_4015C0(x):
	global a
	return a[x + 1] * a[x + 12] == 3417

def sub_4015E0(x):
	global a
	return a[x + 8] > a[x + 35]

def sub_4015F0(x):
	global a
	return a[x + 4] + a[x + 22] == 132

def sub_401610(x):
	global a
	return a[x + 25] + a[x + 28] == 137

def sub_401630(x):
	global a
	return a[x + 3] ^ a[x + 5] == 25

def sub_401640(x):
	global a
	return a[x + 19] * a[x + 42] == 3519

def sub_401660(x):
	global a
	return a[x + 4] * a[x + 6] == 2448

def sub_401680(x):
	global a
	return a[x + 14] + a[x + 38] == 120

def sub_4016A0(x):
	global a
	return a[x + 6] * a[x + 23] == 3570

def sub_4016C0(x):
	global a
	return a[x + 1] + a[x + 21] == 154

def sub_4016E0(x):
	global a
	return a[x + 3] ^ a[x + 11] == 103

def sub_4016F0(x):
	global a
	return a[x + 8] + a[x + 15] == 100

def sub_401710(x):
	global a
	return a[x + 1] * a[x + 15] == 6003

def sub_401730(x):
	global a
	return a[x + 8] == a[x + 17]

def sub_401740(x):
	global a
	return a[x + 2] ^ a[x + 3] == 114

def sub_401750(x):
	global a
	return a[x + 10] ^ a[x + 27] == 12

def sub_401760(x):
	global a
	return a[x + 4] ^ a[x + 8] == 100

def sub_401770(x):
	global a
	return a[x + 21] + a[x + 36] == 150



s.add(sub_401210(0x00) == True)
s.add(sub_401240(0x08) == True)
s.add(sub_401270(0x05) == True)
s.add(sub_401280(0x04) == True)
s.add(sub_401290(0x04) == True)
s.add(sub_4012A0(0x22) == True)
s.add(sub_4012C0(0x04) == True)
s.add(sub_4012D0(0x07) == True)
s.add(sub_4012E0(0x07) == True)
s.add(sub_4012F0(0x0D) == True)
s.add(sub_401310(0x17) == True)
s.add(sub_401320(0x17) == True)
s.add(sub_401330(0x0B) == True)
s.add(sub_401340(0x06) == True)
s.add(sub_401360(0x09) == True)
s.add(sub_401370(0x13) == True)
s.add(sub_401380(0x16) == True)
s.add(sub_4013A0(0x02) == True)
s.add(sub_4013C0(0x06) == True)
s.add(sub_4013E0(0x15) == True)
s.add(sub_4013F0(0x06) == True)
s.add(sub_401400(0x15) == True)
s.add(sub_401410(0x10) == True)
s.add(sub_401420(0x06) == True)
s.add(sub_401430(0x08) == True)
s.add(sub_401440(0x02) == True)
s.add(sub_401460(0x0D) == True)
s.add(sub_401470(0x02) == True)
s.add(sub_401480(0x0A) == True)
s.add(sub_401490(0x09) == True)
s.add(sub_4014A0(0x0C) == True)
s.add(sub_4014C0(0x04) == True)
s.add(sub_4014D0(0x18) == True)
s.add(sub_4014E0(0x00) == True)
s.add(sub_4014F0(0x03) == True)
s.add(sub_401500(0x01) == True)
s.add(sub_401510(0x08) == True)
s.add(sub_401530(0x03) == True)
s.add(sub_401540(0x00) == True)
s.add(sub_401560(0x05) == True)
s.add(sub_401580(0x16) == True)
s.add(sub_4015A0(0x08) == True)
s.add(sub_4015C0(0x08) == True)
s.add(sub_4015E0(0x0B) == True)
s.add(sub_4015F0(0x06) == True)
s.add(sub_401610(0x02) == True)
s.add(sub_401630(0x09) == True)
s.add(sub_401640(0x01) == True)
s.add(sub_401660(0x1C) == True)
s.add(sub_401680(0x01) == True)
s.add(sub_4016A0(0x07) == True)
s.add(sub_4016C0(0x17) == True)
s.add(sub_4016E0(0x11) == True)
s.add(sub_4016F0(0x0A) == True)
s.add(sub_401710(0x06) == True)
s.add(sub_401730(0x11) == True)
s.add(sub_401740(0x06) == True)
s.add(sub_401750(0x09) == True)
s.add(sub_401760(0x06) == True)
s.add(sub_401770(0x0A) == True)

while s.check() == sat:
    m = s.model()

    w = ''
    
    for i in range(48):
        w += chr(m[a[i]].as_long())

    print(w)

    s.add(Or([a[i] != m[a[i]] for i in range(48)]))

```

# FLAG

**`bwctf{WE1C0-M3T0B-1U3W4-T3RCT-FH0P3-Y0UH4-VEFUN}`**



