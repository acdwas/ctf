
# baby_rev.py

```py
from z3 import *

s = Solver()

a = [BitVec(f'a{i}', 8) for i in range(42)]

s.add(a[7] + a[13] + a[8] == 269)
s.add(a[0] - a[1] + a[14] + a[0] == 165)
s.add(a[34] + a[16] * a[21] + a[38] == 9482)
s.add(a[41] + a[8] * a[6] + a[23] == 5500)
s.add(-a[41] - a[21] == -223)
s.add(a[11] * a[4] * a[18] + a[19] == 639710)
s.add(a[23] + a[33] * a[34] == 6403)
s.add(a[18] * a[14] - a[33] == 5072)
s.add(a[24] - a[39] - a[30] - a[22] == -110)
s.add(a[10] + a[30] - a[19] + a[1] == 110)
s.add(a[15] - a[20] - a[41] == -169)
s.add(a[15] * a[35] - a[41] * a[8] == -10231)
s.add(a[36] + a[31] * a[11] - a[32] == 8428)
s.add(a[29] + a[25] + a[40] == 289)
s.add(a[7] - a[12] + a[24] == 100)
s.add(a[21] * a[30] - a[6] == 9262)
s.add(a[38] * a[33] * a[3] == 480244)
s.add(a[20] - a[31] * a[0] - a[2] == -5954)
s.add(a[27] + a[12] * a[21] == 5095)
s.add(a[6] + a[11] * a[8] - a[8] == 10938)
s.add(a[34] - a[5] + a[7] * a[24] == 5014)
s.add(a[40] - a[18] - a[2] == -83)
s.add(a[11] - a[31] + a[9] * a[24] == 10114)
s.add(a[41] == 125)
s.add(a[28] + a[30] - a[3] * a[16] == -6543)
s.add(a[18] * a[25] - a[11] == 5828)
s.add(a[8] * a[9] * a[11] == 1089000)
s.add(a[3] * a[25] - a[29] * a[6] == 2286)
s.add(a[36] - a[7] * a[33] == -3642)
s.add(a[32] - a[1] + a[20] == 73)
s.add(a[39] + a[5] * a[4] == 8307)
s.add(a[0] * a[39] * a[8] == 515460)
s.add(a[12] - a[13] + a[31] == 25)
s.add(a[18] + a[10] + a[41] + a[41] == 351)
s.add(a[7] + a[14] * a[1] + a[22] == 7624)
s.add(a[27] + a[24] * a[18] + a[14] == 5500)
s.add(a[20] - a[41] * a[6] + a[18] == -5853)
s.add(a[33] - a[2] - a[25] * a[31] == -9585)
s.add(a[18] * a[11] * a[37] == 353600)
s.add(a[17] + a[8] + a[7] - a[39] == 192)
s.add(a[11] - a[35] - a[9] * a[31] == -8285)
s.add(a[23] - a[29] + a[39] == 40)
s.add(a[28] + a[10] * a[25] * a[20] == 530777)
s.add(a[32] * a[29] * a[3] == 463914)
s.add(a[32] - a[22] + a[30] == 98)
s.add(a[0] - a[13] + a[40] - a[38] == -74)
s.add(a[17] + a[21] - a[38] == 108)
s.add(a[0] - a[41] * a[23] == -11804)
s.add(a[2] * a[29] * a[27] == 997645)
s.add(a[25] - a[19] * a[35] == -7476)
s.add(a[16] - a[19] * a[7] == -5295)
s.add(a[33] + a[12] * a[26] + a[22] == 2728)
s.add(a[41] + a[24] + a[32] == 281)
s.add(a[23] * a[31] * a[14] == 790020)
s.add(a[35] - a[35] * a[6] - a[14] == -3342)
s.add(a[31] + a[40] - a[17] * a[25] == -11148)
s.add(a[36] * a[18] + a[13] * a[19] == 16364)
s.add(a[40] - a[5] + a[2] * a[18] == 4407)
s.add(a[21] - a[25] + a[3] == 55)
s.add(a[14] + a[14] + a[13] - a[2] == 223)
s.add(a[36] * a[35] - a[5] * a[29] == -2449)
s.add(a[41] - a[39] + a[1] == 135)
s.add(a[35] - a[0] * a[35] + a[0] == -4759)
s.add(a[8] - a[10] * a[21] - a[31] == -4776)
s.add(a[29] - a[24] + a[28] == 126)
s.add(a[0] * a[10] - a[32] - a[8] == 3315)
s.add(a[28] * a[32] + a[41] == 5903)
s.add(a[37] - a[24] + a[32] == 20)
s.add(a[20] * a[10] - a[15] + a[31] == 4688)
s.add(a[36] - a[9] - a[18] * a[18] == -2721)
s.add(a[9] * a[7] + a[16] * a[30] == 13876)
s.add(a[18] + a[34] + a[24] - a[7] == 188)
s.add(a[16] * a[27] + a[20] == 9310)
s.add(a[22] - a[30] - a[37] - a[9] == -211)
s.add(a[4] * a[41] * a[27] - a[38] == 1491286)
s.add(a[35] - a[29] * a[8] + a[13] == -13131)
s.add(a[23] - a[7] - a[24] - a[22] == -107)
s.add(a[37] * a[4] * a[5] == 560388)
s.add(a[17] * a[32] - a[15] == 5295)
s.add(a[32] + a[23] * a[18] - a[5] == 4927)
s.add(a[3] + a[8] * a[39] + a[39] == 7397)
s.add(a[7] * a[25] - a[3] + a[36] == 5597)
s.add(a[9] - a[24] - a[33] == -79)
s.add(a[30] + a[14] * a[36] == 8213)

s.check()

m = s.model()

w = ''

for i in range(42):
    w += chr(m[a[i]].as_long())

print(w)
```

# FLAG

**`GLUG{C01nc1d3nc3_c4n_b3_fr3aky_T6LSERDYB6}`**



