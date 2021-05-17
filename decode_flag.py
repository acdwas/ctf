
from z3 import *

s = Solver()

a = [BitVec(f'a{i}', 32) for i in range(22)]

for i in range(22):
    s.add(a[i] > 0x20, a[i] < 0x7f)

s.add(a[0] == ord('d'))
s.add(a[1] == ord('c'))
s.add(a[2] == ord('t'))
s.add(a[3] == ord('f'))
s.add(a[4] == ord('{'))
s.add(a[21] == ord('}'))

l = b'dctf{mPI(U>TYkgTh%]>b}'

# dctf{mPI(U>TYkgTh%]>b} {390278217489621, 106611495198620, 404577678518429},
# 390278217489621 106611495198620 404577678518429
# 111335652

xx = [[0x15, 0x14, 0x1d],
[0x77, 0x78, 0xa9],
[0xd9, 0x1c8, 0x1f9],
[0x13b, 0x3dc, 0x40d],
[0x110d, 0xe6c, 0x1655],
[0x5a8f, 0x5d30, 0x81f1],
[0x163b3, 0xabf4, 0x18b15],
[0x5d1c5, 0x68984, 0x8c08d],
[0x2465e7, 0x23ae28, 0x32f839],
[0xd1b2a9, 0xd26a68, 0x12910c9],
[0x4c8a90b, 0x4c7f14c, 0x6c36c7d],
[0x124e1287, 0x8bd7830, 0x1448d5f9],
[0x2964ce19, 0x447058d0, 0x4ffbb699],
[0x407b89ab, 0xae50b094, 0xb9dc0e5d],
[0x28fddf437, 0x1a111b9f8, 0x3093e78e9],
[0x6c4c2718b, 0x293d2c35c, 0x73e22f63d],
[0xcdf2901a7, 0x38693ccc0, 0xd58898659],
[0x2e9d63a7d9, 0x37f5f8dcc0, 0x48d5162fd9],
[0xd2f8ba7159, 0x6c655decc0, 0xed306cf959],
[0x1e032db5ad9, 0xa0d4c2fcc0, 0x1fa6a8de2d9],
[0x4935e71270b, 0x714660f7ea4, 0x86dfbda64bd],
[0x7468a06f33d, 0x12ee4e8798ec, 0x1447e4527f05],
[0x4725dbad3ca5, 0x2cf1031eb07c, 0x542735f8c86d],
[0xbb0a9681b52d, 0x46f3b7b5c80c, 0xc80bf0cd40f5],
[0x162f4ba845cd5, 0x60f66c4cdf9c, 0x16ff614cfe89d]]

for j in range(25):
    for i in range(5, len(l)-1):
        v4 = xx[j][i % 3] % 95 + a[i]
        v4 = v4 & 0xff
        a[i] = If(v4 > 126, v4 - 95, v4)

for i in range(5, len(l)-1):
    s.add(a[i] == l[i])

print(s.check())
print(s.model())

# dctf{x_p3de_h3rc00lem}
