
# solve_z3.py

```py
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
```
# Password: p4wR0d

# solve_js.js

```js
(function (_0x2884ac, _0x38f3eb) {
  const _0x137f7b = {
      _0x586027: 0xee,
      _0x57c107: 0xe1,
      _0x1d48a8: 0xad,
    },
    _0x171d27 = _0x5c99,
    _0x10bc21 = _0x2884ac();
  while (true) {
    try {
      const _0x1a4853 =
        -parseInt(_0x171d27(0xb8)) / 0x1 +
        -parseInt(_0x171d27(_0x137f7b._0x586027)) / 0x2 +
        (-parseInt(_0x171d27(0xd8)) / 0x3) * (parseInt(_0x171d27(0xd2)) / 0x4) +
        -parseInt(_0x171d27(0xc2)) / 0x5 +
        -parseInt(_0x171d27(0xe4)) / 0x6 +
        (-parseInt(_0x171d27(_0x137f7b._0x57c107)) / 0x7) * (-parseInt(_0x171d27(0xd5)) / 0x8) +
        parseInt(_0x171d27(_0x137f7b._0x1d48a8)) / 0x9;
      if (_0x1a4853 === _0x38f3eb) break;
      else _0x10bc21.push(_0x10bc21.shift());
    } catch (_0x24f655) {
      _0x10bc21.push(_0x10bc21.shift());
    }
  }
})(_0x38b0, 0xc958c);

function _0x38b0() {
  const _0x5b6324 = [
    '0-9a-zA-Z_',
    'tawhS',
    'add',
    'vjIFk',
    '\\( *\\)',
    'KEEYF',
    'while (tru',
    '4071180IKAcVS',
    'e) {}',
    'classList',
    'Owsw',
    'KtZtq',
    'bVwqF',
    'return (fu',
    'jJVzm',
    'correct',
    'AbVuU',
    'jMnxz',
    'remove',
    'yaMBa',
    'wrong',
    'display',
    'rn this")(',
    '1526224IkJlQw',
    '9WKWdho02x',
    'Utf8',
    '1696dLUZvM',
    'EpsRr',
    'IMdXv',
    '12rYBiMM',
    'kbcnB',
    'aexhm',
    'fiuFN',
    'length',
    'GJBgu',
    'call',
    'YKTVG',
    'constructo',
    '16758eQjzTM',
    '(((.+)+)+)',
    'fiiMO',
    '3468798myqMyY',
    'kIwHW',
    'CKAtD',
    'bfkJr',
    'iZuiL',
    'input',
    '{}.constru',
    'gger',
    'getElement',
    'AES',
    '2449368MuOzxb',
    'nction() ',
    'enc',
    'uZdqo',
    'ById',
    'mqOgh',
    'U2FsdGVkX1',
    'chain',
    'yjxAk',
    'ryceI',
    'nkWDv',
    'test',
    'debu',
    'azJUB',
    'decrypt',
    'IAcfz',
    'yceSy',
    'ltuLh',
    'ILCeK',
    'apply',
    'a-zA-Z_$][',
    'VCufu',
    'stateObjec',
    'init',
    'log',
    '41863131urBGNT',
    'setInterva',
    'action',
    'vRtgB',
    'textConten',
    'search',
    'toString',
    'KIHrU',
    '\\+\\+ *(?:[',
    'Ib5OEO0CW3',
    'iVVui',
    '190994ELOSFq',
    'LgxSB',
    'laufb',
  ];
  _0x38b0 = function () {
    return _0x5b6324;
  };
  return _0x38b0();
}

function _0x5c99(_0x14849d, _0x217100) {
  const _0x25d557 = _0x38b0();
  return (
    (_0x5c99 = function (_0xde7d19, _0x4dc1ff) {
      _0xde7d19 = _0xde7d19 - 0xac;
      let _0xcbf979 = _0x25d557[_0xde7d19];
      return _0xcbf979;
    }),
    _0x5c99(_0x14849d, _0x217100)
  );
}

const _0x3e9efa = {
    _0x1a26ec: 0xca,
    _0x1b2286: 0xcf,
    _0x4f4a11: 0xdc,
    _0x3d2fb4: 0xe7,
    _0x3c1c8a: 0xbe,
    _0x30de5d: 0xe6,
    _0x4c27c3: 0xe3,
    _0x47af85: 0xe3,
    _0x5c5bf0: 0xcb,
    _0x19a370: 0xc9,
    _0x4532a0: 0xe3,
    _0xf9f18b: 0xbc,
    _0x4a6e51: 0xb4,
    _0x4b9f9d: 0xd3,
    _0x36d449: 0xed,
    _0x19cb18: 0xfc,
    _0x17077e: 0xf0,
    _0x923869: 0xec,
    _0x47b7a1: 0xb1,
    _0xb9fb1a: 0xf2,
    _0x51e768: 0xbd,
    _0x5d3e88: 0xf6,
  },
  _0xf27653 = _0x5c99;

var CryptoJS = require('crypto-js');

let _0x56aaac =
  _0xf27653(0xf4) +
  _0xf27653(_0x3e9efa._0x4b9f9d) +
  'WkalqVZ3YrA7QrNN4JPO' +
  _0xf27653(0xb6) +
  'Qj8trHrcQN' +
  _0xf27653(0xc5);

var key = 'p4wR0d';

_0x401b01 = CryptoJS[_0xf27653(_0x3e9efa._0x36d449)]
  [_0xf27653(_0x3e9efa._0x19cb18)](_0x56aaac, key)
  [_0xf27653(0xb3)](CryptoJS[_0xf27653(_0x3e9efa._0x17077e)][_0xf27653(0xd4)]);

console[_0xf27653(0xac)](_0x401b01);
```

# FLAG

**`bctf{345y-p4s5w0rd->w<}`**



