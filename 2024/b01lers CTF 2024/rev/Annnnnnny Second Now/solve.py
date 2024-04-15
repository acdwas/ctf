
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m

def solve_modular_equations(moduli, remainders):
    N = 1
    for m in moduli:
        N *= m

    result = 0
    for i in range(len(moduli)):
        mi = moduli[i]
        Ni = N // mi
        xi = mod_inverse(Ni, mi)
        result += remainders[i] * Ni * xi

    return result % N


moduli = [35831, 143, 1061, 877, 29463179]
remainders = [98, 99, 116, 102, 123]

solution = solve_modular_equations(moduli, remainders)

print("Number:", solution)

l = [0] * 25

l[0] = 35831
l[1] = 143
l[2] = 1061
l[3] = 877
l[4] = 29463179
l[5] = 229
l[6] = 112
l[7] = 337
l[8] = 1061
l[9] = 47
l[10] = 29599
l[11] = 145
l[12] = 127
l[13] = 271639
l[14] = 127
l[15] = 353
l[16] = 193
l[17] = 191
l[18] = 337
l[19] = 1061
l[20] = 193
l[21] = 353
l[22] = 269
l[23] = 487
l[24] = 245

w = ''

for i in range(25):
    w += chr(solution % l[i])

print()
print(f'Flag: {w}')
