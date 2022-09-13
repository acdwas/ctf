
l = []

with open('./file.txt') as f:
    for i in f.readlines():
        l.append(int(i.split()[-1][3:], 16))

w = ''

for i in range(0, len(l), 2):
    w += chr(l[i] ^ l[i+1])

print(w)

