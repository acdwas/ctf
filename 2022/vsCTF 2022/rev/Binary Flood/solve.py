
import base64

s = []

for i in range(1337):

    with open(f'file_{i}', 'rb') as f:
        l = f.read()

        s.append(l[0x4020:0x4020+39].decode())
    f.close()


l = [('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB', 'AAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABA', 'AAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAA', 'AAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAA', 'AAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAA', 'AAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAA', 'AAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAA', 'AABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA', 'BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAA', 'AAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAA', 'ABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABA'), ('AAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAA'), ('AAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAA'), ('AAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAA'), ('AAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAA'), ('AAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAA'), ('AAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAA'), ('AAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAA'), ('AAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'), ('AABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA'), ('ABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAA'), ('BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAA')]

d = []

for a,b in l:
    d.append((a.index('B'), b.index('B')))

x = b''

for t in s:
    w = [''] * 39
    for a,b in d:
        w[a] = t[b]
    # print(''.join(w))
    # break
    # w.append('==')
    x += ''.join(w).encode()

x += b'=='

with open('file.pdf', 'wb') as f:
    f.write(base64.b64decode(x))
