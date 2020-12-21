// nasm -felf64 fun.nasm -o fun.o
// gcc -o solver.o -c solver.c 
// gcc fun.o solver.o -o solver
// ./solver
// Flag: shellmates{fpU_as$emb1y_s_ea5ier_than_pe0ple_th1nk}

#include <stdio.h>

int  buf[] = {0x4a856f35, 0x4a8d10ca, 0x4a8f1369, 0x4a9cef82, 0x4a9af2dc, 0x4a81adfa,
    0x4a456e0a, 0x4a7034e9, 0x495c0e39, 0x4a8f05ae, 0x49ad8381, 0x4a693752, 0x4a692156,
     0x4a704b1d, 0x4a86e3a2, 0x4a98f05a, 0x4a9ceb77, 0x4a705637, 0x4a690f05, 0x4a7f68f3,
      0x4a9488c7, 0x4a7f59d7, 0x4a9ceb77, 0x49ada321, 0x4a8b2fb1, 0x44aeb15c};

int fun(int a); 

int main(void){
    int i;
    int a,b = 0;
    char tmp[53];
    for(a=0;a<26;a++){
        i = 1;
        while(1){
            if(fun(i) == buf[a]){
                tmp[b] = i & 0xff;
                tmp[b+1] = i >> 8;
                b += 2;
                break;
            }
            i++;
        }
    }
    printf("Flag: %s",tmp);
    return 0;
}
