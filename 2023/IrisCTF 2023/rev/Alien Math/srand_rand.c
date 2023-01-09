
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int bpafbz(int a1, int a2)
{
  return (unsigned int)(rand() % (a2 - a1) + a1);
}

int main(int argc, char const *argv[])
{
    int i, x;
    srand(time(0));
    int tab[1000] = {0x00};

    for ( i = 0; i <= 62; ++i )
        rand();
    
    x = 0;

    for ( i = 0; i <= 67; ++i ){
        tab[x++] = bpafbz(1, 6);
        tab[x++] = bpafbz(1, 511);
        tab[x++] = bpafbz(1, 511);
    }

    x = 0;

    for ( i = 0; i <= 67; ++i ){
        printf("%d %d %d\n", tab[x++], tab[x++], tab[x++]);
    }

    return 0;
}

