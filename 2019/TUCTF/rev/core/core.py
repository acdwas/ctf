
s = '55544255477A623173325E65746C713E5E4F327732735E69323573655E31675E7831747C0B'

w = ''
for i in range(0, len(s), 2):
    w += chr(int(s[i:i + 2], 16) ^ 1)

print(w)
