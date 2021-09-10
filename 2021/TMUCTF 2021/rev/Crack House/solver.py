
from pwn import *

r = remote('185.235.41.70', 6000)

l = [ [ 'AAAAAAAAAAAAAAAA', 'AECEEDGCIKKBMOOQ' ],
[ 'BBBBBBBBBBBBBBBB', 'BFDFFEHDJLLCNPPR' ],
[ 'CCCCCCCCCCCCCCCC', 'CGEGGFIEKMMDOQQS' ],
[ 'DDDDDDDDDDDDDDDD', 'DHFHHGJFLNNEPRRT' ],
[ 'EEEEEEEEEEEEEEEE', 'EIGIIHKGMOOFQSSU' ],
[ 'FFFFFFFFFFFFFFFF', 'FJHJJILHNPPGRTTV' ],
[ 'GGGGGGGGGGGGGGGG', 'GKIKKJMIOQQHSUUW' ],
[ 'HHHHHHHHHHHHHHHH', 'HLJLLKNJPRRITVVX' ],
[ 'IIIIIIIIIIIIIIII', 'IMKMMLOKQSSJUWWY' ],
[ 'JJJJJJJJJJJJJJJJ', 'JNLNNMPLRTTKVXXZ' ],
[ 'KKKKKKKKKKKKKKKK', 'KOMOONQMSUULWYY[' ],
[ 'LLLLLLLLLLLLLLLL', 'LPNPPORNTVVMXZZ\\' ],
[ 'MMMMMMMMMMMMMMMM', 'MQOQQPSOUWWNY[[]' ],
[ 'NNNNNNNNNNNNNNNN', 'JLLJNJPGRPT[VQXV' ],
[ 'OOOOOOOOOOOOOOOO', 'KMMKOKQHSQU\WRYW' ],
[ 'PPPPPPPPPPPPPPPP', 'LNNLPLRITRV]XSZX' ],
[ 'QQQQQQQQQQQQQQQQ', 'MOOMQMSJUSW^YT[Y' ],
[ 'RRRRRRRRRRRRRRRR', 'NPPNRNTKVTX_ZU\\Z' ],
[ 'SSSSSSSSSSSSSSSS', 'OQQOSOULWUY`[V][' ],
[ 'TTTTTTTTTTTTTTTT', 'PRRPTPVMXVZa\W^\\' ],
[ 'UUUUUUUUUUUUUUUU', 'QSSQUQWNYW[b]X_]' ],
[ 'VVVVVVVVVVVVVVVV', 'RTTRVRXOZX\\c^Y`^' ],
[ 'WWWWWWWWWWWWWWWW', 'SUUSWSYP[Y]d_Za_' ],
[ 'XXXXXXXXXXXXXXXX', 'TVVTXTZQ\\Z^e`[b`' ],
[ 'YYYYYYYYYYYYYYYY', 'UWWUYU[R][_fa\\ca' ],
[ 'ZZZZZZZZZZZZZZZZ', 'VXXVZV\\S^\\`gb]db' ],
[ 'aaaaaaaaaaaaaaaa', 'iegde_c^a^_^]Z[X' ],
[ 'bbbbbbbbbbbbbbbb', 'jfhef`d_b_`_^[\\Y' ],
[ 'cccccccccccccccc', 'kgifgae`c`a`_\\]Z' ],
[ 'dddddddddddddddd', 'lhjghbfadaba`]^[' ],
[ 'eeeeeeeeeeeeeeee', 'mikhicgbebcba^_\\' ],
[ 'ffffffffffffffff', 'njlijdhcfcdcb_`]' ],
[ 'gggggggggggggggg', 'okmjkeidgdedc`a^' ],
[ 'hhhhhhhhhhhhhhhh', 'plnklfjehefedab_' ],
[ 'iiiiiiiiiiiiiiii', 'qmolmgkfifgfebc`' ],
[ 'jjjjjjjjjjjjjjjj', 'rnpmnhlgjghgfcda' ],
[ 'kkkkkkkkkkkkkkkk', 'soqnoimhkhihgdeb' ],
[ 'llllllllllllllll', 'tpropjnilijihefc' ],
[ 'mmmmmmmmmmmmmmmm', 'uqspqkojmjkjifgd' ],
[ 'nnnnnnnnnnnnnnnn', 'ikg`eZcNaZ_^]K[T' ],
[ 'oooooooooooooooo', 'jlhaf[dOb[`_^L\\U' ],
[ 'pppppppppppppppp', 'kmibg\\ePc\\a`_M]V' ],
[ 'qqqqqqqqqqqqqqqq', 'lnjch]fQd]ba`N^W' ],
[ 'rrrrrrrrrrrrrrrr', 'mokdi^gRe^cbaO_X' ],
[ 'ssssssssssssssss', 'nplej_hSf_dcbP`Y' ],
[ 'tttttttttttttttt', 'oqmfk`iTg`edcQaZ' ],
[ 'uuuuuuuuuuuuuuuu', 'prnglajUhafedRb[' ],
[ 'vvvvvvvvvvvvvvvv', 'qsohmbkVibgfeSc\\' ],
[ 'wwwwwwwwwwwwwwww', 'rtpinclWjchgfTd]' ],
[ 'xxxxxxxxxxxxxxxx', 'suqjodmXkdihgUe^' ],
[ 'yyyyyyyyyyyyyyyy', 'tvrkpenYlejihVf_' ],
[ 'zzzzzzzzzzzzzzzz', 'uwslqfoZmfkjiWg`' ] ]

for i in range(25):
    r.recvuntil(f'Enter Username for License #{i+1}:\n'.encode())
    r.sendline(l[i][0].encode())
    r.recvuntil(f'Enter License Key for License #{i+1}:\n'.encode())
    r.sendline(l[i][1].encode())

print(r.readall().decode())

# TMUCTF{W0w_Y0u_Cr4ck3d_7h3_H0u53_L1k3_4_Ch4mp}

