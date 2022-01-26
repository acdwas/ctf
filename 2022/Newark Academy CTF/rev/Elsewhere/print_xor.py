
with open('./elsewhere', 'rb') as f:
    l = f.read()

l = list(l)

k = [0x6E, 0x6f, 0x74, 0x20, 0x66, 0x6c, 0x61, 0x67]

# 0x67616C6620746F6E

for x in range(0, 0x940):
    i = 0x2010 + x
    print(hex(i), hex(k[i%8]), hex(l[i]), hex(l[i]^k[i%8]))
