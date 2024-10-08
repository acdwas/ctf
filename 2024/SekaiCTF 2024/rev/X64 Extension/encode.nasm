bits 64

section .text
global _start

_start:    
    movdqa xmm15, [dane]
    movdqa xmm1, [vars0]
    pxor   xmm15,xmm1
    
    movdqa xmm0, [vars10]
    movdqa xmm1, [vars10+0x10]
    movdqa xmm2, [vars10+0x20]
    movdqa xmm3, [vars10+0x30]
    movdqa xmm4, [vars10+0x40]
    movdqa xmm5, [vars10+0x50]
    movdqa xmm6, [vars10+0x60]
    movdqa xmm7, [vars10+0x70]
    movdqa xmm8, [vars10+0x80]
    movdqa xmm9, [vars10+0x90]
    movdqa xmm10, [vars10+0xa0]
    movdqa xmm11, [vars10+0xb0]
    movdqa xmm12, [vars10+0xc0]
    movdqa xmm13, [vars10+0xd0]
    movdqa xmm14, [vars10+0xe0]
    
    pxor   xmm15,xmm0
    aesenc xmm15,xmm1
    aesenc xmm15,xmm2
    aesenc xmm15,xmm3
    aesenc xmm15,xmm4
    aesenc xmm15,xmm5
    aesenc xmm15,xmm6
    aesenc xmm15,xmm7
    aesenc xmm15,xmm8
    aesenc xmm15,xmm9
    aesenc xmm15,xmm10
    aesenc xmm15,xmm11
    aesenc xmm15,xmm12
    aesenc xmm15,xmm13
    aesenclast xmm15,xmm14

section .data
    vars0 db 0xff, 0xfe, 0xfd, 0xfc, 0xfb, 0xfa, 0xf9, 0xf8, 0xf7, 0xf6, 0xf5, 0xf4, 0xf3, 0xf2, 0xf1, 0xf0
    vars10 db 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f, 0xb7, 0x73, 0xc2, 0x9f, 0xb3, 0x76, 0xc4, 0x98, 0xbb, 0x7f, 0xce, 0x93, 0xb7, 0x72, 0xc0, 0x9c, 0xb9, 0x51, 0xa8, 0xcd, 0xad, 0x44, 0xbe, 0xda, 0xb5, 0x5d, 0xa4, 0xc1, 0xa9, 0x40, 0xba, 0xde, 0x8d, 0x87, 0xdf, 0x4c, 0x3e, 0xf1, 0x1b, 0xd4, 0x85, 0x8e, 0xd5, 0x47, 0x32, 0xfc, 0x15, 0xdb, 0x9a, 0xe1, 0xf1, 0x74, 0x37, 0xa5, 0x4f, 0xae, 0x82, 0xf8, 0xeb, 0x6f, 0x2b, 0xb8, 0x51, 0xb1, 0xd6, 0x56, 0x17, 0xbd, 0xe8, 0xa7, 0x0c, 0x69, 0x6d, 0x29, 0xd9, 0x2e, 0x5f, 0xd5, 0xcc, 0xf5, 0x55, 0xe2, 0xba, 0x92, 0x62, 0x47, 0xf5, 0x3c, 0xe0, 0xbf, 0x1e, 0x53, 0xcb, 0x07, 0x4f, 0xe2, 0xa9, 0xd2, 0x8f, 0xa2, 0x41, 0x75, 0x83, 0xcb, 0x2c, 0x5c, 0x5a, 0xe5, 0x73, 0x89, 0x96, 0x10, 0xda, 0x45, 0x2a, 0x58, 0xb8, 0x02, 0xdf, 0x64, 0x58, 0xbd, 0xc1, 0x37, 0x93, 0xba, 0x8e, 0xd5, 0x87, 0xcb, 0x8c, 0x7e, 0xc6, 0xbe, 0x0f, 0xb5, 0xea, 0xe2, 0x55, 0x50, 0x99, 0x6b, 0xc3, 0x40, 0x34, 0x3a, 0x04, 0x51, 0x8c, 0x38, 0xdb, 0x35, 0xd4, 0x85, 0x1a, 0x02, 0x47, 0x3f, 0x94, 0xd7, 0xa7, 0xe9, 0x82, 0xde, 0x61, 0x57, 0x8d, 0x6b, 0x8b, 0xb5, 0xd8, 0x3b, 0x12, 0xde, 0x1b, 0x7b, 0xfd, 0x27, 0xab, 0x70, 0x71, 0x1f, 0x70, 0x45, 0xa5, 0x9a, 0x6a, 0x47, 0xe2, 0xa5, 0xfe, 0x90, 0xc7, 0x52, 0xe2, 0x46, 0xa6, 0x05, 0x6f, 0x2d, 0x2d, 0xb0, 0xb7, 0x16, 0x3f, 0x6e, 0xac, 0x6d

    dane db 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41



; X64 Extension