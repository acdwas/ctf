
a = [0x00, 0x72, 0x1D, 0x6F, 0x0A, 0x79, 0x19, 0x65, 0x02, 0x77,
     0x47, 0x1D, 0x63, 0x50, 0x22, 0x78, 0x4F, 0x15, 0x60, 0x50,
     0x37, 0x5D, 0x07, 0x76, 0x1D, 0x47, 0x37, 0x59, 0x69, 0x1C,
     0x2C, 0x76, 0x5C, 0x3D, 0x4A, 0x39, 0x63, 0x02, 0x32, 0x5A,
     0x6A, 0x1F, 0x28, 0x5B, 0x6B, 0x09, 0x53, 0x20, 0x4E, 0x7C,
     0x08, 0x52, 0x32, 0x00, 0x37, 0x56, 0x7d, 0x07]

for i in range(len(a)-1):
    for j in range(0x20, 0x7f):
        if (j >> 4) ^ j ^ a[i] == a[i+1]:
            print(chr(j), end='')

# uiuctf{ar3_y0u_4_r3al_vm_wh3r3_(gpt_g3n3r4t3d_th1s_f14g)}