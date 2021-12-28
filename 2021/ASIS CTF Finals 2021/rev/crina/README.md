

# crina.py

```python
from pwn import *

with open('./enc.flag.enc', 'rb') as f:
    l = f.read()

v = [0x00]

s = {}

for i in range(0x00, 0xff+1):
    v[0] = i
    with open('flag.png', 'wb') as f:
        f.write(bytes(v))

    f.close()

    r = process('./crina', level='error')

    sleep(1)

    with open('./flag.enc', 'rb') as f:
        k = f.read()

    f.close()

    s[k] = i
    s[k[::-1]] = i

    r.close()

b = []

for i in range(0, len(l), 2):
    b.append(s[l[i:i+2]])

with open('test.png', 'wb') as f:
    f.write(bytes(b))
```

# **FLAG**

***


![](./test.png)

