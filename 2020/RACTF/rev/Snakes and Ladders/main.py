

def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def encrypt(a):
    some_text = a[::2]
    randnum = 14
    text_length = len(some_text)
    endtext = ""
    for i in range(1, text_length + 1):
        weirdtext = some_text[i - 1]
        if weirdtext >= "a" and weirdtext <= "z":
            weirdtext = chr(ord(weirdtext) + randnum)
            if weirdtext > "z":
                weirdtext = chr(ord(weirdtext) - 26)
        endtext += weirdtext
    randtext = a[1::2]
    print(endtext)
    print(randtext)
    xored = xor("aaaaaaaaaaaaaaa", randtext)
    hex_xored = xored.encode("utf-8").hex()

    return endtext + hex_xored



def decrypt(msg):
    l = len(msg)//3
    w = msg[:l]
    w1 = msg[l:]
    randnum = 14
    endtext = ""
    for i in range(1, l + 1):
        weirdtext = w[i - 1]
        if weirdtext >= "a" and weirdtext <= "z":
            weirdtext = chr(ord(weirdtext) - randnum)
            if weirdtext < "a":
                weirdtext = chr(ord(weirdtext) + 26)
        endtext += weirdtext

    randtext = bytes.fromhex(w1).decode('utf-8')

    xored = xor("aaaaaaaaaaaaaaa", randtext)
    return ''.join([a+b for a, b in zip(endtext, xored)])

# ftju4j0d05a2ooo020f1a0f063e3e515050540000001c
# decrypt('fqtbjfub4uj_0_d00151a52523e510f3e50521814141c')
# print(encrypt('rcfnv{gn4gv_0_p00151m52aaaaaa}'))

# fqtbjfub4uj_0_d 00151a52523e510f3e50521814141c
# def main():
#     opt = input("Would you like to [E]ncrypt or [D]ecrypt? ")
#     if opt[:1].lower() == "e":
#         msg = input("Enter message to encrypt: ")
#         print(f"Encrypted message: {encrypt(msg)}")
#     elif opt[:1].lower() == "d":
#         msg = input("Enter message to decrypt: ")
#         print(f"Decrypted message: {decrypt(msg)}")

# if __name__ == "__main__":
#     main()

# ractf{n3v3r_g0nn4_g1v3_y0u_up}


print(decrypt('fqtbjfub4uj_0_d 00151a52523e510f3e50521814141c'))
