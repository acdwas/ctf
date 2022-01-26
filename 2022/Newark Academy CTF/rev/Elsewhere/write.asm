
; write

bits 64
mov rax, 1
mov rdi, 1
mov rdx, 0x40
mov rsi, rsp
syscall