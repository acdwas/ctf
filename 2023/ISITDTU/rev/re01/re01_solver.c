
#include <stdio.h>

extern int fun(int a1, int a2, int *a3, int a4, int a5, int *a6, int *a7);

int v12[] = {17325, 19708, 21160, 23202, 25884, 18561, 20995, 22495, 24643, 27473, 18886, 21391, 22901, 25137, 28011, 17116, 19472, 20908, 22968, 25672, 8035, 9333, 10185, 11405, 13119};
int v14[] = {0x02, 0x03, 0x05, 0x07, 0x0b, 0x0d, 0x11, 0x13, 0x17, 0x1d, 0x1f, 0x25, 0x29, 0x2b, 0x2f, 0x35, 0x3b, 0x3d, 0x43, 0x47, 0x49, 0x4f, 0x53, 0x59, 0x61};

int main(void)
{
    int i;
    int a, b, c, d, e, x = 0;

    unsigned long long a1 = 0x404030;
    unsigned long long a2 = 0x404034;
    unsigned long long a3 = 0x404038;

    int alf[] = {0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7a, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x21, 0x5f};

run:
    if (x > 25)
        return 0;
    for (a = 0; a < 38; a++)
    {
        for (b = 0; b < 38; b++)
        {
            for (c = 0; c < 38; c++)
            {
                for (d = 0; d < 38; d++)
                {
                    for (e = 0; e < 38; e++)
                    {
                        int tmp[26] = {0};
                        int v18[26] = {0};
                        tmp[0 + x] = alf[a];
                        tmp[1 + x] = alf[b];
                        tmp[2 + x] = alf[c];
                        tmp[3 + x] = alf[d];
                        tmp[4 + x] = alf[e];

                        asm volatile(
                            "movq $0, %0\n\t" // Wyzerowanie a1
                            "movq $0, %1\n\t" // Wyzerowanie a2
                            "movq $0, %2"     // Wyzerowanie a3
                            :
                            : "m"(*(unsigned long long *)a1), "m"(*(unsigned long long *)a2), "m"(*(unsigned long long *)a3)
                            : "memory");

                        fun(5, 5, tmp, 5, 5, v14, v18);

                        if (v18[0 + x] == v12[0 + x])
                            if (v18[1 + x] == v12[1 + x])
                                if (v18[2 + x] == v12[2 + x])
                                    if (v18[3 + x] == v12[3 + x])
                                        if (v18[4 + x] == v12[4 + x])

                                        {
                                            printf("%c%c%c%c%c", alf[a], alf[b], alf[c], alf[d], alf[e]);
                                            x += 5;
                                            goto run;
                                        }
                    }
                }
            }
        }
    }
    return 0;
}

// good_job_you_solved_re01!