from z3 import *

s = Solver()

a = [BitVec(f'a{i}', 32) for i in range(24)]

for i in range(24):
    s.add(And(a[i] > 0x20, a[i] < 0x7f))

def fun_0x555555555381_z3(a1, a2):
    return a1 + a2

def fun_0x555555555401_z3(a1, a2):
    return a1 - a2

def fun_0x55555555553b_z3(a1, a2):
    return a1 * a2

def fun_0x5555555555b8_z3(a1, a2):
    return a1 & a2

def fun_0x55555555564a_z3(a1, a2):
    return a1 | a2

def fun_0x5555555556c8_z3(a1, a2):
    return a1 ^ a2

ebx = a[9]
r12d = a[0]
edx = a[12]
eax = a[13]
eax = fun_0x55555555564a_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x1326)

ebx = a[20]
r12d = a[22]
edx = a[10]
eax = a[14]
eax = fun_0x55555555564a_z3(eax, edx)
eax = fun_0x555555555401_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0xffffffc0)

ebx = a[2]
r12d = a[12]
edx = a[10]
eax = a[7]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x555555555401_z3(eax, r12d)
eax = fun_0x555555555401_z3(eax, ebx)
s.add(eax == 0xffffffb9)

ebx = a[11]
r12d = a[16]
edx = a[7]
eax = a[20]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x5555555555b8_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x22e2)

ebx = a[7]
r12d = a[15]
edx = a[8]
eax = a[1]
eax = fun_0x55555555553b_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x44126)

ebx = a[20]
r12d = a[8]
edx = a[1]
eax = a[22]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x55555555564a_z3(eax, ebx)
s.add(eax == 0x73)

ebx = a[1]
r12d = a[11]
edx = a[20]
eax = a[18]
eax = fun_0x55555555564a_z3(eax, edx)
eax = fun_0x555555555381_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0xe5)

ebx = a[21]
r12d = a[4]
edx = a[0]
eax = a[13]
eax = fun_0x55555555553b_z3(eax, edx)
eax = fun_0x55555555553b_z3(eax, r12d)
eax = fun_0x5555555555b8_z3(eax, ebx)
s.add(eax == 0x50)

ebx = a[22]
r12d = a[6]
edx = a[12]
eax = a[4]
eax = fun_0x555555555381_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0x8c)

ebx = a[6]
r12d = a[3]
edx = a[19]
eax = a[17]
eax = fun_0x555555555401_z3(eax, edx)
eax = fun_0x5555555555b8_z3(eax, r12d)
eax = fun_0x5555555555b8_z3(eax, ebx)
s.add(eax == 0x00)

ebx = a[5]
r12d = a[18]
edx = a[2]
eax = a[3]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x555555555381_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x19a0)

ebx = a[14]
r12d = a[6]
edx = a[0]
eax = a[18]
eax = fun_0x55555555553b_z3(eax, edx)
eax = fun_0x5555555555b8_z3(eax, r12d)
eax = fun_0x555555555381_z3(eax, ebx)
s.add(eax == 0x40)

ebx = a[5]
r12d = a[4]
edx = a[2]
eax = a[2]
eax = fun_0x5555555555b8_z3(eax, edx)
eax = fun_0x55555555564a_z3(eax, r12d)
eax = fun_0x5555555555b8_z3(eax, ebx)
s.add(eax == 0x52)

ebx = a[15]
r12d = a[12]
edx = a[9]
eax = a[0]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x55555555553b_z3(eax, r12d)
eax = fun_0x555555555401_z3(eax, ebx)
s.add(eax == 0x7cc)

ebx = a[11]
r12d = a[21]
edx = a[12]
eax = a[17]
eax = fun_0x55555555553b_z3(eax, edx)
eax = fun_0x555555555381_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0x21f4)

ebx = a[17]
r12d = a[22]
edx = a[12]
eax = a[22]
eax = fun_0x5555555555b8_z3(eax, edx)
eax = fun_0x555555555381_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0xad)

ebx = a[17]
r12d = a[23]
edx = a[16]
eax = a[23]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x5555555555b8_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x69)

ebx = a[21]
r12d = a[1]
edx = a[0]
eax = a[2]
eax = fun_0x555555555401_z3(eax, edx)
eax = fun_0x5555555555b8_z3(eax, r12d)
eax = fun_0x555555555401_z3(eax, ebx)
s.add(eax == 0xffffffbf)

ebx = a[2]
r12d = a[0]
edx = a[22]
eax = a[14]
eax = fun_0x55555555553b_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x73f8c)

ebx = a[20]
r12d = a[18]
edx = a[15]
eax = a[4]
eax = fun_0x555555555401_z3(eax, edx)
eax = fun_0x55555555553b_z3(eax, r12d)
eax = fun_0x555555555401_z3(eax, ebx)
s.add(eax == 0x35b)

ebx = a[1]
r12d = a[5]
edx = a[8]
eax = a[1]
eax = fun_0x555555555401_z3(eax, edx)
eax = fun_0x55555555553b_z3(eax, r12d)
eax = fun_0x55555555553b_z3(eax, ebx)
s.add(eax == 0x3102)

ebx = a[6]
r12d = a[3]
edx = a[16]
eax = a[14]
eax = fun_0x555555555401_z3(eax, edx)
eax = fun_0x555555555381_z3(eax, r12d)
eax = fun_0x555555555401_z3(eax, ebx)
s.add(eax == 0xffffffda)

ebx = a[11]
r12d = a[21]
edx = a[21]
eax = a[23]
eax = fun_0x5555555556c8_z3(eax, edx)
eax = fun_0x5555555555b8_z3(eax, r12d)
eax = fun_0x5555555555b8_z3(eax, ebx)
s.add(eax == 0x2)

ebx = a[6]
r12d = a[19]
edx = a[13]
eax = a[23]
eax = fun_0x5555555555b8_z3(eax, edx)
eax = fun_0x555555555381_z3(eax, r12d)
eax = fun_0x555555555401_z3(eax, ebx)
s.add(eax == 0x63)

ebx = a[4]
r12d = a[16]
edx = a[23]
eax = a[11]
eax = fun_0x555555555381_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0xd9)

ebx = a[8]
r12d = a[3]
edx = a[13]
eax = a[13]
eax = fun_0x55555555553b_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x555555555381_z3(eax, ebx)
s.add(eax == 0x3562)

ebx = a[8]
r12d = a[1]
edx = a[15]
eax = a[21]
eax = fun_0x5555555555b8_z3(eax, edx)
eax = fun_0x5555555556c8_z3(eax, r12d)
eax = fun_0x55555555564a_z3(eax, ebx)
s.add(eax == 0x71)

ebx = a[11]
r12d = a[2]
edx = a[15]
eax = a[14]
eax = fun_0x5555555555b8_z3(eax, edx)
eax = fun_0x555555555401_z3(eax, r12d)
eax = fun_0x5555555556c8_z3(eax, ebx)
s.add(eax == 0xffffffa0)

print(s.check())

m = s.model()

print("Flag:", ''.join(chr(c) for c in [m[a[i]].as_long() for i in range(24)]))
