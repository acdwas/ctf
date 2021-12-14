
import hashlib
import sys

alf = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for a in alf:
    for b in alf:
        for c in alf:
            for d in alf:

                password2hash = f'{a}{b}{c}{d}'.encode()
                hashresult = hashlib.md5(password2hash).digest()
                sha1 = hashlib.sha1(hashresult)
                sha224 = hashlib.sha224(sha1.digest())
                for i in range(0, 10):
                    sha1 = hashlib.sha1(sha224.digest())
                    sha224 = hashlib.sha224(sha1.digest())
                output = sha224.hexdigest()
                if output == '9ee2275f8699c3146b65fabc390d83df5657a96c39ab58933f82d39b':
                    print('Passwd: ', f'{a}{b}{c}{d}')
                    sys.exit()

# idek{WDOb}

