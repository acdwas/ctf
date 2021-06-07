
BITS 32
section .text 

global fun1

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
		