

enc = [281, 547, 54, 380, 392, 98, 158, 440, 724, 218, 406, 672, 193, 457, 694, 208, 455, 745, 196, 450, 724]

exec('def f(x):'+'yield((x:=-~x)*x+-~-x)%727;'*100)

key = 'rarctf{'

i = 0

while True:
    g=f(i)
    find = [*map(lambda c:ord(c)^next(g), list(key))]
    if find == enc[:7]:
        # print(i)
        break
    i += 1

g=f(i)
flag = [*map(lambda c:c^next(g),enc)]

print(''.join(chr(i) for i in flag))

# rarctf{pyg01f_1s_fun}
