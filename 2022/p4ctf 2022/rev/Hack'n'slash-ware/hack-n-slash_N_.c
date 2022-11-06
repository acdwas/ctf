
#include <emmintrin.h>
#include <stdio.h>

char xmmword_294E70[] = {0x1d, 0x12, 0x19, 0x12, 0x4c, 0x1f, 0x12, 0x48, 0x18, 0x4b, 0x48, 0x1d, 0x49, 0x4b, 0x1b, 0x4f}; 
char xmmword_294E80[] = {0x19, 0x1f, 0x4b, 0x1f, 0x4b, 0x1a, 0x4e, 0x1f, 0x19, 0x1d, 0x1b, 0x4c, 0x19, 0x13, 0x1b, 0x1d}; 
char xmmword_294E90[] = {0x5f, 0x0a, 0x5e, 0x0b, 0x0d, 0x5c, 0x5c, 0x50, 0x51, 0x5c, 0x08, 0x51, 0x0f, 0x0b, 0x59, 0x50}; 
char xmmword_294EA0[] = {0x50, 0x58, 0x0c, 0x59, 0x5e, 0x08, 0x50, 0x5d, 0x5e, 0x0d, 0x0d, 0x5a, 0x50, 0x0d, 0x5b, 0x50}; 

int main(void){
    __m128i t0, t1, t2;
    __m128i t00, t11, t22;
    char modul[33] = {0};
    char modul1[33] = {0};

    t0 = _mm_cvtsi32_si128(105);

    t1 = _mm_unpacklo_epi8(t0, t0);

    t2 = _mm_shuffle_epi32(_mm_unpacklo_epi16(t1, t1), 0);

    *(__m128i *)modul = _mm_xor_si128(_mm_load_si128((const __m128i *)&xmmword_294E90), t2);
    *(__m128i *)&modul[16] = _mm_xor_si128(_mm_load_si128((const __m128i *)&xmmword_294EA0), t2);

    printf("hack  -> n = 0x%s\n", modul);

    t00 = _mm_cvtsi32_si128(42);

    t11 = _mm_unpacklo_epi8(t00, t00);

    t22 = _mm_shuffle_epi32(_mm_unpacklo_epi16(t11, t11), 0);

    *(__m128i *)modul1 = _mm_xor_si128(_mm_load_si128((const __m128i *)&xmmword_294E70), t22);
    *(__m128i *)&modul1[16] = _mm_xor_si128(t22, _mm_load_si128((const __m128i *)&xmmword_294E80));

    printf("slash -> n = 0x%s", modul1);

    return 0;
}

// hack  -> n = 0x6c7bd55985a8fb0991e07a947dd39d29
// slash -> n = 0x7838f58b2ab7ca1e35a5a0d5371f3917
 
 

