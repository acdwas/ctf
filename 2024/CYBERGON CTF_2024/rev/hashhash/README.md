
## solver.c

```c
#include <stdio.h>

extern int fun(int a1, int a2, int a3);

int main(void) {

    int key[] = { 0x0380bb5b, 0xce0acb02, 0x89f8db58, 0x47d24019, 0x560eefbe, 0x2e41d64e, 0x9e0e14eb, 0xeb33aba8, 0x67739ff5, 0x8c9a5b38, 0xeea329c8, 0xe97bc2e9 };
    int i, j, r8 = 0xc0ffee, xx, b = 0;
    int tab[100];
    char nap[4];

    for(i = 0; i < 12; i++){
      j = 1;
      while (j > 0)
      {
        xx = fun(j, r8, i * 4);
        if(key[i] == xx) {
          tab[b++] = j;
        }
        j++;
      }
      r8 = key[i];
    }

    for(i = 0;i < b;i++){
      j = 0;
      r8 = tab[i];
      while(r8) {
        xx = r8 & 0xff;
        if(xx >= 0x20 && xx < 0x7f){
          r8 >>= 8;
          j = 1;
        }
        else {
          j = 0;
          break;
        }
      }

      if(j) {
        r8 = tab[i];
        nap[3] = (char)(r8 & 0xff);
        r8 >>= 8;
        nap[2] = (char)(r8 & 0xff);
        r8 >>= 8;
        nap[1] = (char)(r8 & 0xff);
        r8 >>= 8;
        nap[0] = (char)(r8 & 0xff);
        printf("%s", nap);
      }
    }

    printf("\n");

    return 0;
}
```

## fun.nasm

```asm
BITS 64
section .text 

global fun

fun:
    mov    rbx, rdx
    mov    rcx, rdx
    mov    rax, rdi
    mov    rdx, rdi
    mov    r8,  rsi
    xor    edx,r8d
    rol    edx,cl
    movzx  ecx,bl
    mov    r9, key
    xor    edx, DWORD [r9+rcx*4]
    lea    rcx,[rbx+0x1]
    movzx  ecx,cl
    mov    r9, key
    mov    edi, DWORD [r9+rcx*4]
    mov    ecx,r8d
    rol    r8d,0xd
    and    ecx,0xf
    add    edi,eax
    ror    eax,0x7
    ror    edi,cl
    lea    rcx,[rbx+0x2]
    xor    eax,r8d
    movzx  ecx,cl
    imul   edx,edi
    mov    r9, key
    add    edx, DWORD [r9+rcx*4]
    xor    edx,eax
    mov    r8d,edx

    mov    rax, rdx
    ret

section .data
    key dd  0x983084a9, 0x5fb35e9d, 0x63ad8f63, 0x835b00aa, 0x84ef7e95, 0xb94c8fed, 0x545304ac, 0x3caf5ed3, 0x7b4d8d10, 0x445b1352, 0xbcefe14b, 0x0eb8d63a, 0x5327f267, 0x48ec2425, 0x69c6cdb0, \
            0xe66c9774, 0xcb9ab550, 0xb1b47926, 0x7e8af920, 0x2f1c2085, 0xfaf6f8bf, 0xa471c3b3, 0x7ab7aab5, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5, 0x89ba8623, 0x69656b2c, 0x1fca7808, \
            0x49849986, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5, 0x89ba8623, 0x69656b2c, 0x1fca7808, 0x49849986, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5, 0x89ba8623, 0x69656b2c, \
            0x1fca7808, 0x49849986, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5, 0x89ba8623, 0x69656b2c, 0x1fca7808, 0x49849986, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5, 0x89ba8623, \
            0x69656b2c, 0x1fca7808, 0x49849986, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5, 0x89ba8623, 0x69656b2c, 0x1fca7808, 0x49849986, 0xf6df87c7, 0x45333bf9, 0x11c9d95b, 0x620fe5a5

section .note.GNU-stack
```

## nasm -felf64 fun.nasm -o fun.o
## gcc -o solver.o -c solver.c
## gcc fun.o solver.o -o solver -no-pie

# FLAG

**`CYBERGON_CTF2024{YSL5EUwe![Ha@&{ZSky-w$w7+1Uz4%}`**





