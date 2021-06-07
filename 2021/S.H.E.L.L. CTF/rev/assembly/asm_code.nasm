
; nasm -f elf32 asm_code.nasm
; gcc -m32 -fPIE -no-pie -o asm_code asm_code.o

global main

extern	printf

section .text
main:
	push 0x6f
	push 0x74
	call fun1
	add esp, 0x8
	
	xor edx, edx
	mov edx, eax

	push 0x69
	push 0x62
	call fun1
	add esp, 0x8

	add edx, eax

	push	DWORD edx
	push	DWORD fmt
	call	printf
	add	esp,0x08

	xor eax, eax
	xor ebx, ebx
	add eax, 0x1
	int 0x80

fun1:
		push   ebp
		mov    ebp,esp
		sub    esp,0x10
		mov    eax,DWORD  [ebp+0xc]
		mov    DWORD  [ebp-0x4],eax
		mov    eax,DWORD  [ebp+0x8]
		mov    DWORD  [ebp-0x8],eax
		jmp    L28
L20:	add    DWORD  [ebp-0x4],0x7
		add    DWORD  [ebp-0x8],0x70
L28:	cmp    DWORD  [ebp-0x8],0x227
		jle    L20
		mov    eax,DWORD  [ebp-0x4]
		leave  
		ret  

section	.data
	fmt:		db	"SHELL{0x%x}", 0xa, 0x00

; SHELL{0x117}