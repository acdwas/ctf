from z3 import *

s = Solver()

a = [BitVec('a%d' % i, 32) for i in range(0, 29)]

for i in range(0, 29):
  s.add(Or(a[i] >= 48, a[i] == 45))
  s.add(a[i] < 123)


def check_01(a1):
  return And(a1[5] == 45, a1[11] == 45, a1[17] == 45, a1[23] == 45)


def check_02(a1):
  return And((a1[1] - 48) <= 9, (a1[4] - 48) <= 9, (a1[6] - 48) <= 9, (a1[9] - 48) <= 9, (a1[15] - 48) <= 9, (a1[18] - 48) <= 9, (a1[22] - 48) <= 9, (a1[27] - 48) <= 9, (a1[28] - 48) <= 9)


def check_03(a1):
  return And(a1[4] - 48 == 2 * (a1[1] - 48) + 1, a1[4] - 48 > 7, a1[9] == a1[4] - (a1[1] - 48) + 2)


def check_04(a1):
  return (a1[27] + a1[28]) % 13 == 8


def check_05(a1):
  return (a1[27] + a1[22]) % 22 == 18


def check_06(a1):
  return (a1[18] + a1[22]) % 11 == 5


def check_07(a1):
  return (a1[22] + a1[28] + a1[18]) % 26 == 4


def check_08(a1):
  return (a1[1] + a1[4] * a1[6]) % 41 == 5


def check_09(a1):
  v1 = BitVec('v1', 32)
  v1 = ((a1[15] - a1[28]) >> 31) >> 30
  return ((v1 + a1[15] - a1[28]) & 3) - v1 == 1


def check_0A(a1):
  v1 = BitVec('v1', 32)
  v1 = ((a1[22] + a1[4]) >> 31) >> 30
  return ((v1 + a1[22] + a1[4]) & 3) - v1 == 3


def check_0B(a1):
  return And(a1[20] == 66, a1[21] == 66)


def check_0C(a1):
  return (a1[6] + a1[15] * a1[9]) % 10 == 1


def check_0D(a1):
  v1 = BitVec('v1', 32)
  v1 = ((a1[15] + a1[4] + a1[27] - 18) >> 31) >> 28
  return ((v1 + a1[15] + a1[4] + a1[27] - 18) & 0xF) - v1 == 8


def check_0E(a1):
  v1 = BitVec('v1', 32)
  v1 = (a1[28] - a1[9]) >> 31
  return ((v1 + a1[28] - a1[9]) & 1) - v1 == 1


def check_0F(a1):
  return a1[0] == 77


s.add(And(
    check_01(a) == True,
    check_02(a) == True,
    check_03(a) == True,
    check_04(a) == True,
    check_05(a) == True,
    check_06(a) == True,
    check_07(a) == True,
    check_08(a) == True,
    check_09(a) == True,
    check_0A(a) == True,
    check_0B(a) == True,
    check_0C(a) == True,
    check_0D(a) == True,
    check_0E(a) == True,
    check_0F(a) == True,
))

while s.check() == sat:
  m = s.model()

  w = ''
  for i in range(29):
    w += chr(m[a[i]].as_long())
  print w

  s.add(Or(a[0] != s.model()[a[0]],
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
           a[28] != s.model()[a[28]]
           ))
