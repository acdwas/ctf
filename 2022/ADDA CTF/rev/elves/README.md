
## for i in {0..728}; do objdump -Mintel -d binary$i | grep cmp -B 1 >> file.txt; done

# solve.py

```py
l = []

with open('./file.txt') as f:
    for i in f.readlines():
        l.append(int(i.split()[-1][3:], 16))

w = ''

for i in range(0, len(l), 2):
    w += chr(l[i] ^ l[i+1])

print(w)
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet dictum sit amet. Purus sit amet volutpat consequat mauris nunc. Convallis posuere morbi leo urna molestie. Congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Diam ut venenatis tellus in metus vulputate. Sed odio morbi quis commodo. Pulvinar neque laoreet suspendisse interdum. Aenean sed adipiscing diam donec adipiscing tristique risus nec feugiat. The flag is <b>ctf{L0r3m_1p5um_d010r_s1t_4m3t}</b>. Tempus iaculis urna id volutpat lacus. Libero nunc consequat interdum varius. Nibh nisl condimentum id venenatis a condimentum vitae. Porta non pulvinar neque laoreet suspendisse.


# FLAG

**`ctf{L0r3m_1p5um_d010r_s1t_4m3t}`**
