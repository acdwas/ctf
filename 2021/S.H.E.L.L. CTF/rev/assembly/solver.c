
// nasm -felf32 fun.nasm -o fun.o
// gcc -m32 -o solver.o -c solver.c
// gcc -m32 fun.o solver.o -o solver
// ./solver                         
// SHELL{0x117}

#include <stdio.h>

extern int fun1(int a, int b);

int main(void){
    printf("SHELL{0x%x}\n", fun1(0x74,0x6f) + fun1(0x62,0x69));
    return 0;
}
