
# import dis

def fun(cipher):
    key = 'w'

    a = cipher.split(' ')

    key_1 = ord(key)
    key_2 = int(key.encode('hex'))

    keyes = [key_1, key_2]

    cipher = ''

    for x in range(0, len(a)):
        if x % 2 == 1:
            cipher += chr(int(a[x]) ^ keyes[0])

        if x % 2 == 0:
            cipher += chr(int(a[x]) ^ keyes[1])
        
    print(cipher)

fun('31 35 1 12 5 67 53 40 15 14 25 68 105 83 48')

# dis.dis(fun)

# RTL{H4x_ByT3$$}

