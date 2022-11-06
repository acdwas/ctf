

from crypto_commons.rsa.rsa_commons import modinv
import itertools

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def hack(a):
    n = 0x6c7bd55985a8fb0991e07a947dd39d29
    p = 10830293516065295497 
    q = 13314468632857240481

    phi = (p-1)*(q-1)
    d = modinv(0x10001, phi)

    return bytes.fromhex(hex(pow(int.from_bytes(a, 'little'), d, n))[2:].rjust(30, '0'))[::-1]

def slash(a):
    n = 0x7838f58b2ab7ca1e35a5a0d5371f3917
    p = 10963757462568095959 
    q = 14575578571502293441

    phi = (p-1)*(q-1)
    d = modinv(0x10001, phi)

    return bytes.fromhex(hex(pow(int.from_bytes(a, 'little'), d, n))[2:].rjust(30, '0'))[::-1]

def quack_data(data):
    return b''.join([b(a) for a, b in zip(chunks(data, 16), itertools.cycle([hack, slash]))])



with open('./flag.png.encrypt_me.hacked_and_slashed', 'rb') as f:
    l = f.read()

with open('p4_ctf.png', 'wb') as f:
    f.write(quack_data(l))

