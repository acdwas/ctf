
#include <stdio.h>

int fun(char *);

int main(void){
    char nap[9];
    scanf("%s", nap);
    if(fun(nap)){
        printf("OK\n");
    }
    return 0;
}

