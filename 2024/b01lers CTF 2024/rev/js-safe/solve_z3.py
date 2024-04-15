from z3 import *

s = Solver()

fun = {
    'IAcfz': lambda _0x28689b, _0x6e4708: _0x28689b < _0x6e4708,
    'bfkJr': lambda _0x3759f9, _0x48abef: _0x3759f9(_0x48abef),
    'vjIFk': lambda _0x240a91, _0x5eb8f3: _0x240a91 == _0x5eb8f3,
    'CKAtD': lambda _0x49bb92, _0x35fd2c: _0x49bb92 - _0x35fd2c,
    'azJUB': lambda _0x3dd966, _0x3db420: _0x3dd966 ^ _0x3db420,
    'jJVzm': lambda _0x8980f1, _0xb46b78: _0x8980f1 ^ _0xb46b78,
    'kIwHW': lambda _0x297084, _0x458326: _0x297084 == _0x458326,
    'fiuFN': lambda _0x3a4854, _0xd30a49: _0x3a4854 == _0xd30a49,
    'fiiMO': lambda _0x5a3d36, _0x301900: _0x5a3d36 == _0x301900,
    'AbVuU': lambda _0x27648c, _0x5766cc: _0x27648c + _0x5766cc,
    'IaapB': lambda _0x523291, _0x4c802e: _0x523291 + _0x4c802e,
}

x = Bool('x')

a = [BitVec(f'a{i}', 8) for i in range(6)]

x = And(x, fun['vjIFk'](a[4], fun['CKAtD'](a[1], 4)))
x = And(x, a[1] == fun['azJUB'](a[0], 0x44))
x = And(x, fun['vjIFk'](a[0], a[2] - 0x7))
x = And(x, fun['vjIFk'](a[3], fun['jJVzm'](a[2], 0x25)))
x = And(x, fun['kIwHW'](a[5], a[0] ^ 0x14))
x = And(x, fun['fiuFN'](a[4], fun['CKAtD'](a[1], 4)))
x = And(x, fun['fiiMO'](a[0], a[3] ^ 0x22))
x = And(x, fun['fiiMO'](a[0], a[2] - 0x7))
x = And(x, a[0] == fun['AbVuU'](a[5], 0xc))
x = And(x, fun['fiiMO'](a[2], fun['IaapB'](a[4], 0x47)))
x = And(x, fun['fiiMO'](a[2], fun['jJVzm'](a[5], 0x13)))
x = And(x, fun['fiiMO'](a[5], fun['azJUB'](a[3], 0x36)))
x = And(x, 0x52 == a[3])

s.add(x)

print(s.check())
m = s.model()

print(f'Password: {"".join(chr(m[a[i]].as_long()) for i in range(6))}')




