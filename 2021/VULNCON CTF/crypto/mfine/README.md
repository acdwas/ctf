
# mfine.py

```py
key = 'RVWA6IIHTWAJH1VWEAH0A6AR 1WAFIA2FTF6G1V6XWRHJA0DX0RHRDRHFTAJH1VWEAQVWEWAW6JVAGWRRWEAHTA6TA6G1V6XWRAH0A2611W5ARFAHR0ATD2WEHJAWSDH#6GWTRAWTJE 1RW5AD0HT4A6A0H21GWA26RVW26RHJ6GAIDTJRHFTA6T5AJFT#WERW5AX6JUARFA6AGWRRWEARVWAIG64AIFEA FDAH0A#DGTJFTBM#ME RV9T4OJ8TOXMOXENUMTO9IO NDO6EMOZ28EROMTND4V_ARVWAIFE2DG6AD0W5A2W6T0ARV6RAW6JVAGWRRWEAWTJE 1R0ARFAFTWAFRVWEAGWRRWEA6T5AX6JUA646HTA2W6THT4ARVWAJH1VWEAH0AW00WTRH6GG A6A0R6T56E5A0DX0RHRDRHFTAJH1VWEAQHRVA6AEDGWA4F#WETHT4AQVHJVAGWRRWEA4FW0ARFAQVHJVA0HTJWARVWA6IIHTWAJH1VWEAH0A0RHGGA6A2FTF6G1V6XWRHJA0DX0RHRDRHFTAJH1VWEAHRAHTVWEHR0ARVWAQW6UTW00W0AFIARV6RAJG600AFIAJH1VWE0'

def search_a_b(plaintext):
    for a in range(m+1):
        for b in range(m+1):
            ciphertext = ''
            for letter in plaintext:
                i = ALPHA.index(letter)
                c = (a*i + b) % m
                ciphertext += ALPHA[c]
            if ciphertext in key:
                return a, b
    return a, b

def decrype(plaintext, a, b):
    ciphertext = ''
    for x in range(len(key)):
        for letter in plaintext:
            i = ALPHA.index(letter)
            c = (a*i + b) % m
            if key[x] == ALPHA[c]:
                ciphertext += letter
    return ciphertext



ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_ #"
m = len(ALPHA)

a, b = search_a_b('VULNCON')

print(decrype(ALPHA, a, b))
```

# FLAG

**`VULNCON{3V3RYTH1NG_C4N_B3_BR0K3N_1F_Y0U_AR3_5M4RT_3N0UGH}`**

