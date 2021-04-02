
from z3 import *

s = Solver()

a = [BitVec('a{}'.format(i),64) for i in range(34)]

l = [ 0x012F78,  0x012F30, 0x012F72,  0x012F5F, 0x012F61,  0x012F6E, 0x012F64,  0x012F5F, 0x012F6C,  0x012F30, 0x012F67,  0x012F31, 0x012F63,  0x012F40, 0x012F6C,  0x012F5F, 0x012F73,  0x012F68, 0x012F31,  0x012F66, 0x012F74,  0x012F5F, 0x012F65,  0x012F40, 0x012F73,  0x012F79, 0x012F5F,  0x012F72, 0x012F31,  0x012F67, 0x012F68,  0x012F38, 0x012F3F,  0x012F3F ]

x = BitVec('x', 64)

for i in range(34):
    s.add(a[i] >= 0x20, a[i] <= 0x7f)
    s.add(a[i] ^ x == l[i])


while s.check() == sat:
  m = s.model()

  w = ''
  for i in range(34):
    w += chr(m[a[i]].as_long())
  print(w)

  s.add(Or(    a[0] != s.model()[a[0]],
           a[1] != s.model()[a[1]],
           a[2] != s.model()[a[2]],
           a[3] != s.model()[a[3]],
           a[4] != s.model()[a[4]],       
            a[5] != s.model()[a[5]],
           a[6] != s.model()[a[6]],
           a[7] != s.model()[a[7]],
           a[8] != s.model()[a[8]],
           a[9] != s.model()[a[9]],
           a[10] != s.model()[a[10]],
           a[11] != s.model()[a[11]],
           a[12] != s.model()[a[12]],
           a[13] != s.model()[a[13]],
           a[14] != s.model()[a[14]],
           a[15] != s.model()[a[15]],
           a[16] != s.model()[a[16]],
           a[17] != s.model()[a[17]],
           a[18] != s.model()[a[18]],
           a[19] != s.model()[a[19]],
           a[20] != s.model()[a[20]],
           a[21] != s.model()[a[21]],
           a[22] != s.model()[a[22]],
           a[23] != s.model()[a[23]],
           a[24] != s.model()[a[24]],
           a[25] != s.model()[a[25]],
           a[26] != s.model()[a[26]],
           a[27] != s.model()[a[27]],
           a[28] != s.model()[a[28]],
           a[29] != s.model()[a[29]],
           a[30] != s.model()[a[30]],
           a[31] != s.model()[a[31]],
           a[32] != s.model()[a[32]],
           a[33] != s.model()[a[33]],
           ))

# g/m@~q{@s/x.|_s@lw.yk@z_lf@m.xw'  
# f.lApzAr.y/}^rAmv/xjA{^mgAl/yv&!!
# d,nC}rxCp,{-\pCot-zhCy\oeCn-{t$##
# `(jGyv|Gt(){XtGkp)~lG}XkaGj)p ''
# h bOq~tO| w!sP|Ocx!vdOuPciOb!wx(//


# x0r_and_l0g1c@l_sh1ft_e@sy_r1gh8??     <-----------------


# y1s^`oe^m1f0bAm^ri0gu^dArx^s0fi9>>
# {3q\bmg\o3d2`Co\pk2ew\fCpz\q2dk;<<
# z2p]clf]n2e3aBn]qj3dv]gBq{]p3ej:==
# ~6tYghbYj6a7eFjYun7`rYcFuYt7an>99

