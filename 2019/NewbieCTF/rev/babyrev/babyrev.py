
import subprocess
import string

def write_f(s):
    with open('file.txt', 'w') as f:
        f.write(s)
    f.close()


def open_f():
    with open('enc.txt', encoding="latin-1") as f:
        s = f.read()
    f.close()
    return s


with open('enc.txt_1', encoding="latin-1") as f:
    f2 = f.read()
f.close()

flag = ['*'] * 36

i = 0
while i < 36:
    for c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!_{}$':
        # for c in string.printable:
        flag[i] = c
        write_f(''.join(flag))
        subprocess.call(["babyrev.exe", "file.txt"])
        s = open_f()
        if ord(f2[i]) == ord(s[i]):
            # print(flag)
            i += 1
            break
print()
print('FLAG: ' + ''.join(flag))
