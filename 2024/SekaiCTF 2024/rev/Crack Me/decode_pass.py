from Crypto.Cipher import AES
from binascii import unhexlify

def decrypt_password(ciphertext_hex, key, iv):
    ciphertext = unhexlify(ciphertext_hex)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted = cipher.decrypt(ciphertext)
    decrypted = decrypted.rstrip(b"\0")
    
    return decrypted.decode('utf-8')

encrypted_password = '03afaa672ff078c63d5bdb0ea08be12b09ea53ea822cd2acef36da5b279b9524'
key = 'react_native_expo_version_47.0.0'
iv = '__sekaictf2023__'

decrypted_password = decrypt_password(encrypted_password, key, iv)
print(decrypted_password)
