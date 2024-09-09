
## solver.py

```py

sbox =[ 0x48, 0x5c, 0xbc, 0x97, 0x81, 0x91, 0x60, 0xad, 0x94, 0xcb, 0x92, 0x39, 0x1a, 0x0f, 0x30, 0x2d, 0x45, 0xde,
        0x14, 0xa2, 0x08, 0x57, 0xb6, 0xae, 0x76, 0x8e, 0x87, 0x15, 0x0c, 0xe7, 0x62, 0xc8, 0x58, 0x29, 0x6d, 0xc9,
        0xa7, 0xbe, 0x04, 0x49, 0x05, 0xfa, 0x75, 0x9f, 0xfd, 0x95, 0xbb, 0x5b, 0x79, 0xbf, 0xda, 0xeb, 0x21, 0x9b, 
        0xa5, 0x82, 0x3a, 0x3e, 0xb9, 0x99, 0xf0, 0xf5, 0x6b, 0x06, 0xfc, 0xaf, 0xf2, 0xb0, 0x78, 0x86, 0xcf, 0xd4, 
        0x83, 0x59, 0x00, 0x4a, 0xb5, 0xfe, 0xab, 0x3d, 0xc7, 0x8c, 0xe3, 0xc3, 0xe5, 0x03, 0x5a, 0x1d, 0x9d, 0x1f, 
        0x0a, 0x56, 0xc0, 0xba, 0x43, 0x25, 0x77, 0x24, 0x7c, 0xa6, 0xdf, 0xf1, 0x4b, 0x44, 0xff, 0x4c, 0xaa, 0xc1, 
        0x69, 0xf9, 0x38, 0x88, 0x9a, 0xa4, 0xe6, 0x10, 0xdc, 0xea, 0x68, 0x8d, 0x5f, 0x63, 0xbd, 0x8b, 0xf3, 0x7e, 
        0xdb, 0x73, 0x5d, 0x65, 0x67, 0xa1, 0x72, 0xd8, 0xb1, 0x1b, 0x9e, 0x84, 0x16, 0x32, 0xe1, 0xf4, 0xef, 0x93, 
        0xac, 0x74, 0x36, 0x8f, 0xcc, 0x61, 0x0d, 0x35, 0x12, 0xdd, 0x4e, 0xc4, 0x64, 0x3f, 0x09, 0x70, 0x2a, 0xfb, 
        0xc5, 0x85, 0x3b, 0x1c, 0x50, 0x19, 0xd5, 0xe9, 0x47, 0x0b, 0xe2, 0xca, 0xc6, 0xf7, 0xb2, 0xd6, 0xf8, 0x11, 
        0x54, 0x6e, 0x90, 0xc2, 0xec, 0x96, 0x51, 0xd7, 0xe8, 0x31, 0x80, 0x7d, 0x18, 0x34, 0xb7, 0x02, 0xa0, 0x7a, 
        0xb3, 0xd0, 0x46, 0x66, 0x37, 0x1e, 0x7b, 0x42, 0x6c, 0x17, 0xd9, 0x33, 0x2b, 0x22, 0xce, 0xa9, 0x7f, 0xb4, 
        0x07, 0x6a, 0x41, 0x40, 0x26, 0x2f, 0xa8, 0xcd, 0x71, 0xb8, 0x53, 0x13, 0x5e, 0xf6, 0xe0, 0x52, 0x4f, 0x6f, 
        0xe4, 0x89, 0x3c, 0x9c, 0xa3, 0x8a, 0x4d, 0x28, 0x0e, 0xd3, 0xd2, 0x98, 0xee, 0x2c, 0x2e, 0xed, 0x27, 0x20, 
        0x01, 0x23, 0x55, 0xd1 ]

with open('./hieroglyphs.txt', 'rb') as f_hist:
    hist = f_hist.read().split()

with open('./message.txt', 'rb') as f_msg:
    msg = f_msg.read()

msg = [msg[i:i+4] for i in range(0, len(msg), 4)]

pos = []

for i in range(len(msg)):
    pos.append(hist.index(msg[i]))

def washing_machine_rev(a):
    a2 = len(a)
    j = 0

    while True:
        if  j >= a2 >> 1:
            break
        v4 = a[j]
        a[j] = a[a2 - j - 1]
        a[a2 - j - 1] = v4
        j += 1

    for i in range(len(a)-1, 0, -1):
        v5 = a[i-1] ^ a[i]
        a[i] = v5

    return a

washing_machine_rev(pos)

a = list(b'csawctf{_________________________________________________________________}')

v18 = [0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0x00]

a1 = [0] * 11000

xxx = 8
yyy = 73

while xxx < 74:
    for y in range(0x20, 0x7f):
        
        memory = [0] * 512

        v24 = 0
        v25 = 1

        regs = [0] * 100

        a[xxx] = y
        aaa = a[::]

        v3 = a[0]

        for i in range(1, len(a), 1):
            v5 = v3 ^ aaa[i]
            aaa[i] = v5
            v3 = v5

        a2 = len(a)

        j = 0

        while True:
            if  j >= a2 >> 1:
                break
            v4 = aaa[j]
            aaa[j] = aaa[a2 - j - 1]
            aaa[a2 - j - 1] = v4
            j += 1

        v7 = 0

        for i in range(74):
            a1[v7] = 0
            a1[v7 + 1] = 1
            v4 = v7 + 2
            v8 = v7 + 3
            a1[v4] = aaa[i]
            for j in range(10):
                a1[v8] = 0
                a1[v8 + 1] = 0
                a1[v8 + 2] = v18[(10 * i + j) % 5]
                a1[v8 + 3] = 8
                a1[v8 + 4] = 1
                a1[v8 + 5] = 3
                a1[v8 + 6] = 3
                a1[v8 + 7] = 1
                a1[v8 + 8] = 1
                a1[v8 + 9] = 1
                a1[v8 + 10] = 0
                a1[v8 + 11] = 2
                a1[v8 + 12] = 1
                v5 = v8 + 13
                v8 += 14
                a1[v5] = 3
            a1[v8] = 4
            a1[v8 + 1] = 1
            v6 = v8 + 2
            v7 = v8 + 3
            a1[v6] = i

        a1[v7] = 7

        while v25:
            v1 = v24
            v24 += 1
            v13 = a1[v1]
            v2 = v13
            match v13:
                case 0:
                    v14 = a1[v24]
                    v3 = v24 + 1;
                    v24 += 2
                    v4 = a1[v3]
                    v2 = v14
                    regs[v14] = v4
                case 1:
                    v15 = a1[v24]
                    v5 = v24 + 1
                    v24 += 2
                    v23 = a1[v5]
                    v2 = v15
                    regs[v15] ^= regs[v23]
                case 2:
                    v16 = a1[v24]
                    v6 = v24 + 1
                    v24 += 2
                    v20 = a1[v6]
                    v2 = v16
                    regs[v16] = (regs[v16] >> (8 - v20)) | (regs[v16] << v20) & 0xff
                case 3:
                    v7 = v24
                    v24 += 1
                    v2 = a1[v7]
                    regs[v2] = sbox[regs[v2] & 0xff]
                case 4:
                    v17 = a1[v24]
                    v8 = v24 + 1
                    v24 += 2
                    v2 = a1[v8]
                    memory[v2] = regs[v17]
                case 5:
                    v18 = a1[v24]
                    v9 = v24 + 1
                    v24 += 2
                    v22 = a1[v9]
                    v2 = v18
                    regs[v18] = memory[v22]
                case 6:
                    v10 = v24
                    v24 += 1
                    v2 = regs[a1[v10]]
                case 7:
                    v25 = 0
                case 8:
                    v19 = a1[v24]
                    v11 = v24 + 1
                    v24 += 2
                    v21 = a1[v11]
                    v2 = v19
                    regs[v19] = (regs[v19] << (8 - v21)) | (regs[v19] >> v21) & 0xff

        if memory[yyy-xxx] == pos[yyy-xxx]:
            print(''.join(chr(i) for i in a), end='')
            xxx += 1
            print()
            break


```

# FLAG

**`csawctf{w41t_1_54w_7h353_5ymb0l5_47_7h3_m3t_71m3_70_r34d_b00k_0f_7h3_d34d}`**



