
import ctypes
libsystem = ctypes.CDLL('libc.so.6')

l = [0x17, 0x0E, 0x02, 0x15, 0x0B, 0x03, 0x04, 0x10, 0x16, 0x05, 0x12, 0x06,
     0x0C, 0x07, 0x13, 0x01, 0x08, 0x14, 0x09, 0x0A, 0x0D, 0x18, 0x00, 0x11, 0x0F]

flag = [
    0x63, 0x51, 0x48, 0x6A, 0x40, 0x09, 0x1E, 0x7A, 0x7A, 0x0C, 0x0B, 0x02, 0x49,
    0x48, 0x4D, 0x43, 0x71, 0x6B, 0x30, 0x5A, 0x12, 0x1B, 0x27, 0x39, 0x53
]

libsystem.srand(0x1548)

v12 = [0] * 5

v4 = 0
for v5 in range(10):
    v10 = libsystem.rand()
    if (v5 & 1) == 0:
        v12[v4] = v10 % 127
        v4 += 1

x = [0] * 25
for i in range(len(flag)):
    x[l[i]] = chr(flag[i] ^ v12[i//5])

print(''.join(x))

# AFFCTF{1t5_N0t_50_r4nd0m}