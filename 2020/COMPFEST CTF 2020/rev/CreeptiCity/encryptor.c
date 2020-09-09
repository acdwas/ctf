#include <stdio.h>
#include <stddef.h>
#include <stdint.h>

char tmp[0x80] = {'\x00'};
char tmp1[0x80] = {'\x00'};

int main(int argc, char **argv)
{

    size_t i, x, a, n;
    FILE *in = fopen(argv[1], "r");
    i = fread(tmp, sizeof(char), 0x80, in);
    fclose(in);
    n = 0x2a;
    for (x = 0; x < i; x++)
    {
        a = (n ^ tmp[x]) & 0xff;
        if (a >= 0x61)
            a -= 0x61;
        a = (a + 0x1e) & 0xff;
        tmp1[x] = a;
        a = (a ^ n) & 0xff;
        if (a >= 0x80)
            a -= 0x80;
        n = a;
    }
    tmp1[x++] = 0x20;
    a = (n ^ tmp1[0]) & 0xff;
    if (a >= 0x61)
        a -= 0x61;
    a = (a + 0x1e) & 0xff;
    tmp1[0] = a;
    a = (a ^ n) & 0xff;
    if (a >= 0x80)
        a -= 0x80;
    tmp1[x++] = a;
    tmp1[x] = 0x0a;
    printf("%s", tmp1);
    return 0;
}
