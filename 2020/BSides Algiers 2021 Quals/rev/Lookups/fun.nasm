
BITS 64
section .text 

global fun
 
fun:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 10h
    mov     dword [rbp-0x0c], edi
    fild    dword [rbp-0x0c]
    fld     st0
    fsqrt
    fmulp       
    fstp    dword [rbp-0x0c]
    mov     eax, dword [rbp-0x0c]
    mov     rsp, rbp
    pop     rbp
    retn


