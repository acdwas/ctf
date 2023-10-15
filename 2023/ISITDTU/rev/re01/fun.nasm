BITS 64
section .text 

global fun

fun:
        push   rbp
        mov    rbp, rsp
        sub    rsp, 0x20
        mov    DWORD [rbp-0x4], edi
        mov    DWORD [rbp-0x8], esi
        mov    QWORD [rbp-0x10], rdx
        mov    DWORD [rbp-0x14], ecx
        mov    DWORD [rbp-0x18], r8d
        mov    QWORD [rbp-0x20], r9
        mov    eax, DWORD [a1]
        cmp    DWORD [rbp-0x4], eax
        jle    L1
        mov    eax, DWORD [a2]
        cmp    DWORD [rbp-0x18], eax
        jle    L2
        mov    eax, DWORD [a3]
        cmp    DWORD [rbp-0x8], eax
        jle    L3
        mov    eax, DWORD [a1]
        movsxd rdx, eax
        mov    rax, rdx
        shl    rax, 0x2
        add    rax, rdx
        shl    rax, 0x2
        mov    rdx, rax
        mov    rax, QWORD [rbp+0x10]
        add    rdx, rax
        mov    eax, DWORD [a2]
        cdqe
        mov    esi, DWORD [rdx+rax*4]
        mov    eax, DWORD [a1]
        movsxd rdx, eax
        mov    rax, rdx
        shl    rax, 0x2
        add    rax, rdx
        shl    rax, 0x2
        mov    rdx, rax
        mov    rax, QWORD [rbp-0x10]
        add    rdx, rax
        mov    eax, DWORD [a3]
        cdqe
        mov    ecx, DWORD [rdx+rax*4]
        mov    eax, DWORD [a3]
        movsxd rdx, eax
        mov    rax, rdx
        shl    rax, 0x2
        add    rax, rdx
        shl    rax, 0x2
        mov    rdx, rax
        mov    rax, QWORD [rbp-0x20]
        add    rdx, rax
        mov    eax, DWORD [a2]
        cdqe
        mov    eax, DWORD [rdx+rax*4]
        imul   ecx, eax
        mov    eax, DWORD [a1]
        movsxd rdx, eax
        mov    rax, rdx
        shl    rax, 0x2
        add    rax, rdx
        shl    rax, 0x2
        mov    rdx, rax
        mov    rax, QWORD [rbp+0x10]
        add    rdx, rax
        mov    eax, DWORD [a2]
        add    ecx, esi
        cdqe
        mov    DWORD [rdx+rax*4], ecx
        mov    eax, DWORD [a3]
        add    eax, 0x1
        mov    DWORD [a3], eax
        mov    r8, QWORD [rbp-0x20]
        mov    edi, DWORD [rbp-0x18]
        mov    ecx, DWORD [rbp-0x14]
        mov    rdx, QWORD [rbp-0x10]
        mov    esi, DWORD [rbp-0x8]
        mov    eax, DWORD [rbp-0x4]
        sub    rsp, 0x8
        push   QWORD [rbp+0x10]
        mov    r9, r8
        mov    r8d, edi
        mov    edi, eax
        call   fun
        add    rsp, 0x10
L3:	    mov    DWORD [a3], 0x0
        mov    eax, DWORD [a2]
        add    eax, 0x1
        mov    DWORD [a2], eax
        mov    r8, QWORD [rbp-0x20]
        mov    edi, DWORD [rbp-0x18]
        mov    ecx, DWORD [rbp-0x14]
        mov    rdx, QWORD [rbp-0x10]
        mov    esi, DWORD [rbp-0x8]
        mov    eax, DWORD [rbp-0x4]
        sub    rsp, 0x8
        push   QWORD [rbp+0x10]
        mov    r9, r8
        mov    r8d, edi
        mov    edi, eax
        call   fun
        add    rsp,0x10
L2:	    mov    DWORD [a2], 0x0
        mov    eax, DWORD [a1]
        add    eax, 0x1
        mov    DWORD [a1], eax
        mov    r8, QWORD [rbp-0x20]
        mov    edi, DWORD [rbp-0x18]
        mov    ecx, DWORD [rbp-0x14]
        mov    rdx, QWORD [rbp-0x10]
        mov    esi, DWORD [rbp-0x8]
        mov    eax, DWORD [rbp-0x4]
        sub    rsp, 0x8
        push   QWORD [rbp+0x10]
        mov    r9, r8
        mov    r8d, edi
        mov    edi, eax
        call   fun
        add    rsp, 0x10
        jmp    L4
L1:	    nop
L4:	    leave
        ret

section .data
a1  dd   0
a2  dd   0
a3  dd   0

section .note.GNU-stack
