
text = 'a7 f9 de 54 29 92 7f 61 9a 7a 5f f3 f4 1a 88 a1 8f ca 97 47'.split()
key = "MANGEKYOU"

s = []

k = []

for i in key:
    k.append(((ord(i))))

for i in range(0,256):
    s.append(i) # i.e. s = [0 1 2 3 4 5 6 7 ..]
    if i >= len(key):
        k.append(k[i%len(key)])

def key_sche(s,k):
    j = 0
    for i in range(0,256):
        j = (j + s[i] + k[i])%256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        # print("s in the iteration:",i+1," is :",s)
    return s
def key_stream(text,s):
    ks = []
    i = 0
    j = 0
    status = 1
    while(status == 1):
        i = (i+1) % 256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        t = (s[i]+s[j])%256
        ks.append(s[t])
        if len(ks) == len(text):
            status = 0
    return ks

key_new = key_stream(text,key_sche(s,k))

print(f'KEY: {key_new}')

flag = ''

for i in range(len(key_new)):
    flag += chr(key_new[i] ^ int(text[i], 16))

print(f'FLAG: {flag}')

# KEY: [244, 177, 155, 24, 101, 233, 44, 85, 201, 49, 10, 192, 171, 79, 203, 233, 190, 130, 163, 58]
# FLAG: SHELL{S4SKU3_UCH1H4}

