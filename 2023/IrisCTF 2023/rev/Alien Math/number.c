
#include <stdio.h>
#include <string.h>

void trof_pripew(char *a1)
{
  char *s; // [rsp+8h] [rbp-18h]
  char *i; // [rsp+18h] [rbp-8h]

  s = (char *)a1;
  if ( a1 )
  {
    for ( i = (char *)&a1[strlen(a1) - 1]; s < i; --i )
    {
      *s ^= *i;
      *i ^= *s;
      *s++ ^= *i;
    }
  }
}

int main(int argc, char const *argv[])
{
    char tmp[100] = {0};
    int x;

    scanf("%d", &x);

    sprintf(tmp, "%o", x);

    trof_pripew(tmp);
    printf("%s", tmp);

    return 0;
}
