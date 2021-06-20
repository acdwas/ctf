
ll = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]

flag = b"4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy"

l = []

for i in range(len(flag)):
    for j in range(-0xff, 0xff):
        if ll[i] + j == flag[i]:
            l.append(j)


for i in range(-8,-33,-1):
    x = l[-6:] + l[i:-6] + l[:i]

    w = ''

    for i in range(len(l)):
        if i%2 == 0:
            for j in range(0x20, 0x7f):
                if x[i] == j + 3 * (i//2):
                    w += chr(j)
                    break
        else:
            w += chr(x[i])
    if 'flag' in w:
        print(w[16:] + w[:16])
        break

# flag{1ncr34s3_1n_3nth4lpy_0f_5y5}