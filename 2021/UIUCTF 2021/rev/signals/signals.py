
from distorm3 import Decode, Decode64Bits

def xor(a):
    l = []
    c = a[0] ^ 0x48
    for i in a:
        l.append(i ^ c)
    return bytes(l), c

with open("signals", "rb") as f :
    code = f.read()

base = 0x3020

flag = ''

for i in range(41):
    raw = code[base:][:7]
    raw_code, c = xor(raw)
    flag += chr(c)
    dis_code = Decode(0x100, raw_code, Decode64Bits)
    base = eval(str(base+7)+dis_code[0][2][13:-1])

print(flag)

# uiuctf{another_ctf_another_flag_checker}