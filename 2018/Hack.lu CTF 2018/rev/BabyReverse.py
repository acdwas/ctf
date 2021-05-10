
from z3 import *

l = [0x0a, 0x0d, 0x06, 0x1c, 0x22, 0x38, 0x18, 0x26, 0x36, 0x0f, 0x39, 0x2b, 0x1c, 0x59, 0x42, 0x2c,
     0x36, 0x1a, 0x2c, 0x26, 0x1c, 0x17, 0x2d, 0x39, 0x57, 0x43, 0x01, 0x07, 0x2b, 0x38, 0x09, 0x07,
     0x1a, 0x01, 0x17, 0x13, 0x13, 0x17, 0x2d, 0x39, 0x0a, 0x0d, 0x06, 0x46, 0x5c, 0x7d, 0x00]

s = Solver()


def fun(a, b):
    return a ^ b


a = [BitVec('a%d' % i, 8) for i in range(46)]


for i in range(45):
    s.add(a[i] >= 0x21, a[i] <= 0x7d)
    s.add(fun(a[i], a[i + 1]) == l[i])

while s.check() == sat:
    m = s.model()
    w = ''
    for i in range(46):
        w += chr(m[a[i]].as_long())
    if 'flag' in w:
        print 'FLAG : ', w
        break
    s.add(Or(a[0] != s.model()[a[0]],
             a[1] != s.model()[a[1]],
             a[2] != s.model()[a[2]],
             a[3] != s.model()[a[3]],
             a[4] != s.model()[a[4]],
             a[5] != s.model()[a[5]],
             a[6] != s.model()[a[6]],
             a[7] != s.model()[a[7]],
             a[8] != s.model()[a[8]],
             a[9] != s.model()[a[9]],
             a[10] != s.model()[a[10]],
             a[11] != s.model()[a[11]],
             a[12] != s.model()[a[12]],
             a[13] != s.model()[a[13]],
             a[14] != s.model()[a[14]],
             a[15] != s.model()[a[15]],
             a[16] != s.model()[a[16]],
             a[17] != s.model()[a[17]],
             a[18] != s.model()[a[18]],
             a[19] != s.model()[a[19]],
             a[20] != s.model()[a[20]],
             a[21] != s.model()[a[21]],
             a[22] != s.model()[a[22]],
             a[23] != s.model()[a[23]],
             a[24] != s.model()[a[24]],
             a[25] != s.model()[a[25]],
             a[26] != s.model()[a[26]],
             a[27] != s.model()[a[27]],
             a[28] != s.model()[a[28]],
             a[29] != s.model()[a[29]],
             a[30] != s.model()[a[30]],
             a[31] != s.model()[a[31]],
             a[32] != s.model()[a[32]],
             a[33] != s.model()[a[33]],
             a[34] != s.model()[a[34]],
             a[35] != s.model()[a[35]],
             a[36] != s.model()[a[36]],
             a[37] != s.model()[a[37]],
             a[38] != s.model()[a[38]],
             a[39] != s.model()[a[39]],
             a[40] != s.model()[a[40]],
             a[41] != s.model()[a[41]],
             a[42] != s.model()[a[42]],
             a[43] != s.model()[a[43]],
             a[44] != s.model()[a[44]]
             ))
