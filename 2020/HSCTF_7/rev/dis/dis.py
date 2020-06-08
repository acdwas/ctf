
def a(s):
    o = [0] * len(s)
    for i,c in enumerate(s):
        o[i] = (c * 2) - 60
    return o

def e(s):
    s = [ord(c)for c in s]
    o = [(c ^ 5) - 30 for c in b(a(s),c(s))]
    try:
        return bytes(o)
    except:
        return 0

def b(s,t):
    for x,y in zip(s,t):
        yield (x + y) - 50

def c(s):
    return [c + 5 for c in s]


def main():
    # s = input('Guess?')
    x = 6
    w = 'flag{'
    o = b'\xae\xc0\xa1\xab\xef\x15\xd8\xca\x18\xc6\xab\x17\x93\xa8\x11\xd7\x18\x15\xd7\x17\xbd\x9a\xc0\xe9\x93\x11\xa7\x04\xa1\x1c\x1c\xed'
    while x <= len(o):
        for i in range(0x20,0x7f):
            ww = w 
            ww += chr(i)
            if e(ww) == o[:x]:
                x += 1
                w += chr(i)
                break 
    print(w)
    # print(e('flag{'))
    # print(e(s))
    # if e(s) == o:
    #     print('Correct!')
    # else:
    #     print('Wrong...')

main()

# flag{5tr4ng3_d1s45s3mbly_1c0a88}