
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
          // r8 = xx;
          tab[b++] = j;
          // printf("%x - %d\n", j, i);
          // break;
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

// print(bytes.fromhex('43594245'))
// print(bytes.fromhex('52474f4e'))
// print(bytes.fromhex('5f435446'))
// print(bytes.fromhex('32303234'))
// print(bytes.fromhex('7b59534c'))
// print(bytes.fromhex('35455577'))
// print(bytes.fromhex('3384c53c'))
// print(bytes.fromhex('6140267b'))
// print(bytes.fromhex('5a536b79'))
// print(bytes.fromhex('2d772477'))
// print(bytes.fromhex('372b3155'))
// print(bytes.fromhex('7a34257d'))

// CYBERGON_CTF2024{YSL5EUw35<a@&{ZSky-w$w7+1Uz4%}

// CYBERGON_CTF2024{YSL5EUwe![Ha@&{ZSky-w$w7+1Uz4%}

// '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 'df49c07f', '43594245', '674ac855', 