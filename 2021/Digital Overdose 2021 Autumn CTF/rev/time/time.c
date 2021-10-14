
// https://github.com/kokke/tiny-AES-c.git

// make

// gcc aes.o time.c


#include "aes.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void decrypt_cbc(uint8_t key[16])
{
    uint8_t iv[]  = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10 };

    uint8_t in[]  = { 0xa8, 0x37, 0xf4, 0xc7, 0x52, 0x3c, 0x28, 0x11,
                        0x69, 0x76, 0xec, 0x98, 0x0d, 0x12, 0x92, 0xda,
                        0xc8, 0x48, 0xbc, 0x02, 0xfa, 0xfa, 0xd2, 0x7b,
                        0x9c, 0x47, 0xdb, 0x82, 0x69, 0xcf, 0xb0, 0x8f };

    uint8_t out[] = { 0x44, 0x4f, 0x7b};

    struct AES_ctx ctx;

    AES_init_ctx_iv(&ctx, key, iv);

    AES_CBC_decrypt_buffer(&ctx, in, 32);

    if (0 == memcmp((char*) out, (char*) in, 3)) {
        int i;
        for(i=0;i<10;i++)
            printf("%c",key[i]);
        putchar('\n');
        for(i=0;i<32;i++)
            printf("%c",in[i]);
        putchar('\n');
        printf("SUCCESS!\n");
	    exit(0);
    } 
}

int main(void)
{
    long j = time(0), i;
    int x;

    while(1){
        uint8_t key[16] = {0};
        i = j;
        x = 9;
        while(i){
            key[x--] = (uint8_t)((i % 10) + 0x30);
            i /= 10;
        }
        decrypt_cbc(key);
        j--;
    }
    return 0;
}


// 1613606400
// DO{V3ry_n1Ce_t1MInG5_!1}
// SUCCESS!

