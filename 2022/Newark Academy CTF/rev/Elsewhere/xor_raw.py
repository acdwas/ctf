
with open('./elsewhere', 'rb') as f:
    l = f.read()

l = list(l)

x = b''

with open('xor_raw', 'wb') as f:
    for i in range(0, 0x940, 8):
        x += (int.from_bytes(l[0x2010+i:0x2010+i+8], byteorder='little') ^ 0x67616C6620746F6E).to_bytes(8, byteorder='little')
    f.write(x)
