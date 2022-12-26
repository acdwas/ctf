
# solver.c

```c
#include <immintrin.h>
#include <stdio.h>

__m128i aeskeygenassist(__m128i xmm1, __m128i xmm5){

    __m128i xmm3;

    xmm3 = _mm_slli_si128(xmm1, 4);
    xmm1 = _mm_xor_si128(xmm1, xmm3);
    xmm3 = _mm_slli_si128(xmm1, 4);
    xmm1 = _mm_xor_si128(xmm1, xmm3);
    xmm3 = _mm_slli_si128(xmm1, 4);
    xmm1 = _mm_xor_si128(xmm1, xmm3);
    return _mm_xor_si128(xmm1, xmm5);
}

void key_gen(__m128i xmm5, __m128i key_schedule[]){

    __m128i xmm2;

    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x01);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[0] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x03);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[1] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x09);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[2] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x1b);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[3] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x51);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[4] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xf3);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[5] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xd9);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[6] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x8b);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[7] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xa1);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[8] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xe3);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[9] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xa9);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[10] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xfb);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[11] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xf1);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[12] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0xd3);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[13] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x79);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[14] = xmm5;
    xmm2 = _mm_aeskeygenassist_si128(xmm5, 0x6b);
    xmm2 = _mm_shuffle_epi32(xmm2, 0xff);
    xmm5 = aeskeygenassist(xmm5,xmm2);
    key_schedule[15] = xmm5;
}

void encode(__m128i xmm1, __m128i xmm2, char text[][16], __m128i cipher[], __m128i key_schedule[]){

    int i, j;
    __m128i xmm0;

    for(i=0;i<8;i++){

        xmm0 = _mm_loadu_si128((__m128i*)text[i]);

        xmm0 = _mm_xor_si128(xmm0, xmm2);
        xmm0 = _mm_xor_si128(xmm0, xmm1);

        for(j=0;j<15;j++){
            xmm0 = _mm_aesenc_si128(xmm0, key_schedule[j]);
        }

        xmm0 = _mm_aesenclast_si128(xmm0, key_schedule[15]);

        cipher[i] = xmm0;
        xmm2 = xmm0;
    }
}

void decode(__m128i xmm1, __m128i xmm2, __m128i cipher[], __m128i text[], __m128i key_schedule[]){

    int i,j;
    __m128i xmm0;
    
    for(j=0;j<8;j++){

        xmm0 = _mm_xor_si128(cipher[j], key_schedule[15]);

        for(i=14;i>=0;i--){
            xmm0 = _mm_aesdec_si128(xmm0, _mm_aesimc_si128(key_schedule[i]));
        }

        xmm0 = _mm_aesdeclast_si128(xmm0, xmm2);

        xmm0 = _mm_xor_si128(xmm0, xmm1);
        text[j] = xmm0;
        xmm2 = cipher[j];
    }
}

int main(void){

    char niteveryevilkeys[] = { 0x6e, 0x69, 0x74, 0x65, 0x76, 0x65, 0x72, 0x79, 0x65, 0x76, 0x69, 0x6c, 0x6b, 0x65, 0x79, 0x73 };
    char veryevilinitvect[] = { 0x76, 0x65, 0x72, 0x79, 0x65, 0x76, 0x69, 0x6c, 0x69, 0x6e, 0x69, 0x74, 0x76, 0x65, 0x63, 0x74 };

    char text[8][16] = { {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41},
                            {0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41} };

    unsigned char cipher_ctf[8][16] = { {0x53, 0x31, 0x94, 0x4D, 0x8F, 0x9F, 0x3F, 0x4E, 0xCB, 0x52, 0xF2, 0x45, 0x7C, 0x05, 0xE6, 0xB0},
                                        {0xF5, 0x46, 0x65, 0xA8, 0x6A, 0xAD, 0x18, 0xE1, 0x3B, 0x45, 0xD5, 0x47, 0xBB, 0x4F, 0xE8, 0x43},
                                        {0xD8, 0xFF, 0x92, 0x7F, 0x5F, 0x1C, 0xF8, 0x0B, 0x32, 0x5A, 0x13, 0x93, 0x6A, 0x56, 0x76, 0x0D},
                                        {0x43, 0xFA, 0x00, 0x38, 0x49, 0x5B, 0x6C, 0xE7, 0xE7, 0x1C, 0xED, 0xBB, 0x1A, 0x96, 0xCF, 0x5E},
                                        {0xFC, 0x35, 0xF2, 0x74, 0x58, 0x41, 0x8F, 0x5C, 0xF7, 0x02, 0x08, 0xC4, 0xAD, 0x52, 0xF4, 0xF9},
                                        {0x9E, 0x28, 0x99, 0x93, 0x6C, 0x12, 0xE9, 0x08, 0x3C, 0xC0, 0x89, 0x11, 0x11, 0x6F, 0xD7, 0xCC},
                                        {0xD5, 0xE1, 0xD4, 0x84, 0x02, 0xB0, 0x0C, 0x03, 0x23, 0x25, 0x3D, 0x36, 0x59, 0x8A, 0x2F, 0x41},
                                        {0x0D, 0x10, 0x40, 0xC8, 0x22, 0xAB, 0x80, 0xC6, 0x96, 0xB5, 0xB9, 0x21, 0xA0, 0x3E, 0x05, 0xC5} };

    __m128i xmm1, xmm2;
    __m128i key_schedule[16];
    __m128i cipher[8];
    __m128i text1[8];

    int i, j;
    char v[16];

    xmm1 = _mm_loadu_si128((__m128i*)niteveryevilkeys);
    xmm2 = _mm_loadu_si128((__m128i*)veryevilinitvect);

    key_gen(xmm1, key_schedule);

    // printf("---------------------------encode--------------------------\n");

    // encode(xmm1, xmm2, text, cipher, key_schedule);

    // for(j=0;j<8;j++){

    //     _mm_storeu_si128((__m128i*)v, cipher[j]);

    //     for(i=0;i<16;i++){
    //         printf("%.2x ", v[i]&0xff);
    //     }
    //     printf("\n");
    // }

    // printf("---------------------------decode--------------------------\n");

    // decode(xmm1, xmm2, cipher, text1, key_schedule);

    // for(j=0;j<8;j++){

    //     _mm_storeu_si128((__m128i*)v, text1[j]);

    //     for(i=0;i<16;i++){
    //         printf("%.2x ", v[i]&0xff);
    //     }
    //     printf("\n");
    // }

    // printf("---------------------------------------------------------\n");

    for(i=0;i<8;i++){
        cipher[i] = _mm_loadu_si128((__m128i*)cipher_ctf[i]);
    }

    decode(xmm1, xmm2, cipher, text1, key_schedule);

    for(j=0;j<8;j++){

        _mm_storeu_si128((__m128i*)v, text1[j]);

        for(i=0;i<16;i++){
            printf("%c", v[i]&0xff);
        }
    }

    return 0;
}
```

# FLAG

**`nite{a_t4st3_0f_g00dw4re_4n4lys1s_3112hd}`**

