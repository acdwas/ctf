
#include <stdio.h>
#include <stdlib.h>

long long test(int a1)
{
  int i; // [rsp+10h] [rbp-4h]

  if ( a1 == 1 )
    return 0;
  for ( i = 2; i < a1 - 1; ++i )
  {
    if ( !(a1 % i) )
      return 0;
  }
  return 1;
}

unsigned long long next(unsigned long long a1)
{
  int j; // [rsp+Ch] [rbp-1Ch]
  unsigned long long v4; // [rsp+10h] [rbp-18h]
  long long v5; // [rsp+18h] [rbp-10h]
  int i; // [rsp+24h] [rbp-4h]

  for ( i = 0; i <= 7; ++i )
  {
    v5 = 0LL;
    v4 = a1;
    for ( j = 0; j <= 7; ++j )
    {
      if ( (unsigned int)test((unsigned int)(j + 1)) )
        v5 ^= v4 & 1;
      v4 >>= 1;
    }
    a1 = (v5 << 7) + (a1 >> 1);
  }
  return a1;
}

int main(void)
{
    int i;
    unsigned long long val = 2;

    for(i=8;i<=95;i++)
    {
        val = next(val);
        printf("0x%x, ", val);
    }
    return 0;
}