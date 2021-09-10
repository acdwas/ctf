
#include <stdio.h>

char array2[30];
char array3[30];

int fun(char array3[], char array2[], int x)
{
    int num = 0;
	int flag5;
	int flag6;
	int flag7;
	int flag8;
	int flag9;
	int flag10;
	int flag11;
	int flag12;
	int flag13;
	int flag14;
	int flag15;
	int flag16;
	int flag17;
	int flag18;
	int flag19;
	int flag20;
	int flag21;
	int flag22;
	int flag23;
	int flag24;
	int flag25;
	int flag26;
	int flag27;
	int flag28;
	int flag29;
	int flag30;
	int flag31;
	int flag32;
	int flag33;
	int flag34;
	int flag35;
	int flag36;
	int flag37;
	int flag38;
	int flag39;
	int flag40;
	int flag41;
	int flag42;
	int flag43;
	int flag44;
	int flag45;
	int flag46;
	int flag47;
	int flag48;
	int flag49;
	int flag50;
	int flag51;
	int flag52;
	int flag53;
	int flag54;
	int flag55;
	int flag56;
	int flag57;
	int flag58;
	int flag59;
	int flag60;
	int flag61;
	int flag62;
	int flag63;
	int flag64;


	int j = x;
	int kk = 0;
	while (kk < 1)
	{
		flag5 = j % 2 == 0 && array3[j] >= 65 && array3[j] < 78;
		if (!flag5)
		{
			goto IL_109;
		}
		flag6 = array2[j] == (char)(array3[j] + j);
		if (!flag6)
		{
			num++;
			goto IL_109;
		}
		IL_82F:
		kk++;
		continue;
		IL_109:
		flag7 = j % 2 == 0 && array3[j] >= 78 && array3[j] < 91;
		if (flag7)
		{
			flag8 = array2[j] == (char)(array3[j] + j - 4);
			if (flag8)
			{
				goto IL_82F;
			}
			num++;
		}
		flag9 = j % 2 == 0 && array3[j] >= 97 && array3[j] < 110;
		if (flag9)
		{
			flag10 = array2[j] == (char)(array3[j] - j + 8);
			if (flag10)
			{
				goto IL_82F;
			}
			num++;
		}
		flag11 = j % 2 == 0 && array3[j] >= 110 && array3[j] < 123;
		if (flag11)
		{
			flag12 = array2[j] == (char)(array3[j] - j - 5);
			if (flag12)
			{
				goto IL_82F;
			}
			num++;
		}
		flag13 = j % 3 == 0 && array3[j] >= 65 && array3[j] < 78;
		if (flag13)
		{
			flag14 = array2[j] == (char)(array3[j] + j + 1);
			if (flag14)
			{
				goto IL_82F;
			}
			num++;
		}
		flag15 = j % 3 == 0 && array3[j] >= 78 && array3[j] < 91;
		if (flag15)
		{
			flag16 = array2[j] == (char)(array3[j] + j - 7);
			if (flag16)
			{
				goto IL_82F;
			}
			num++;
		}
		flag17 = j % 3 == 0 && array3[j] >= 97 && array3[j] < 110;
		if (flag17)
		{
			flag18 = array2[j] == (char)(array3[j] - j + 6);
			if (flag18)
			{
				goto IL_82F;
			}
			num++;
		}
		flag19 = j % 3 == 0 && array3[j] >= 110 && array3[j] < 123;
		if (flag19)
		{
			flag20 = array2[j] == (char)(array3[j] - j - 11);
			if (flag20)
			{
				goto IL_82F;
			}
			num++;
		}
		flag21 = j % 5 == 0 && array3[j] >= 65 && array3[j] < 78;
		if (flag21)
		{
			flag22 = array2[j] == (char)(array3[j] + j - 2);
			if (flag22)
			{
				goto IL_82F;
			}
			num++;
		}
		flag23 = j % 5 == 0 && array3[j] >= 78 && array3[j] < 91;
		if (flag23)
		{
			flag24 = array2[j] == (char)(array3[j] + j - 9);
			if (flag24)
			{
				goto IL_82F;
			}
			num++;
		}
		flag25 = j % 5 == 0 && array3[j] >= 97 && array3[j] < 110;
		if (flag25)
		{
			flag26 = array2[j] == (char)(array3[j] - j + 3);
			if (flag26)
			{
				goto IL_82F;
			}
			num++;
		}
		flag27 = j % 5 == 0 && array3[j] >= 110 && array3[j] < 123;
		if (flag27)
		{
			flag28 = array2[j] == (char)(array3[j] - j - 15);
			if (flag28)
			{
				goto IL_82F;
			}
			num++;
		}
		flag29 = j % 7 == 0 && array3[j] >= 65 && array3[j] < 78;
		if (flag29)
		{
			flag30 = array2[j] == (char)(array3[j] + j - 5);
			if (flag30)
			{
				goto IL_82F;
			}
			num++;
		}
		flag31 = j % 7 == 0 && array3[j] >= 78 && array3[j] < 91;
		if (flag31)
		{
			flag32 = array2[j] == (char)(array3[j] + j - 14);
			if (flag32)
			{
				goto IL_82F;
			}
			num++;
		}
		flag33 = j % 7 == 0 && array3[j] >= 97 && array3[j] < 110;
		if (flag33)
		{
			flag34 = array2[j] == (char)(array3[j] - j + 4);
			if (flag34)
			{
				goto IL_82F;
			}
			num++;
		}
		flag35 = j % 7 == 0 && array3[j] >= 110 && array3[j] < 123;
		if (flag35)
		{
			flag36 = array2[j] == (char)(array3[j] - j - 25);
			if (flag36)
			{
				goto IL_82F;
			}
			num++;
		}
		flag37 = j % 11 == 0 && array3[j] >= 65 && array3[j] < 78;
		if (flag37)
		{
			flag38 = array2[j] == (char)(array3[j] + j - 10);
			if (flag38)
			{
				goto IL_82F;
			}
			num++;
		}
		flag39 = j % 11 == 0 && array3[j] >= 78 && array3[j] < 91;
		if (flag39)
		{
			flag40 = array2[j] == (char)(array3[j] + j + 2);
			if (flag40)
			{
				goto IL_82F;
			}
			num++;
		}
		flag41 = j % 11 == 0 && array3[j] >= 97 && array3[j] < 110;
		if (flag41)
		{
			flag42 = array2[j] == (char)(array3[j] - j + 8);
			if (flag42)
			{
				goto IL_82F;
			}
			num++;
		}
		flag43 = j % 11 == 0 && array3[j] >= 110 && array3[j] < 123;
		if (flag43)
		{
			flag44 = array2[j] == (char)(array3[j] - j - 5);
			if (flag44)
			{
				goto IL_82F;
			}
			num++;
		}
		flag45 = j % 13 == 0 && array3[j] >= 65 && array3[j] < 78;
		if (flag45)
		{
			flag46 = array2[j] == (char)(array3[j] + j + 1);
			if (flag46)
			{
				goto IL_82F;
			}
			num++;
		}
		flag47 = j % 13 == 0 && array3[j] >= 78 && array3[j] < 91;
		if (flag47)
		{
			flag48 = array2[j] == (char)(array3[j] + j - 10);
			if (flag48)
			{
				goto IL_82F;
			}
			num++;
		}
		flag49 = j % 13 == 0 && array3[j] >= 97 && array3[j] < 110;
		if (flag49)
		{
			flag50 = array2[j] == (char)(array3[j] - j + 6);
			if (flag50)
			{
				goto IL_82F;
			}
			num++;
		}
		flag51 = j % 13 == 0 && array3[j] >= 110 && array3[j] < 123;
		if (flag51)
		{
			flag52 = array2[j] == (char)(array3[j] - j - 22);
			if (flag52)
			{
				goto IL_82F;
			}
			num++;
		}
		flag53 = j % 2 == 1 && array3[j] >= 65 && array3[j] < 78;
		if (flag53)
		{
			flag54 = array2[j] == (char)(array3[j] + j + 3);
			if (flag54)
			{
				goto IL_82F;
			}
			num++;
		}
		flag55 = j % 2 == 1 && array3[j] >= 78 && array3[j] < 91;
		if (flag55)
		{
			flag56 = array2[j] == (char)(array3[j] + j - 3);
			if (flag56)
			{
				goto IL_82F;
			}
			num++;
		}
		flag57 = j % 2 == 1 && array3[j] >= 97 && array3[j] < 110;
		if (flag57)
		{
			flag58 = array2[j] == (char)(array3[j] - j + 5);
			if (flag58)
			{
				goto IL_82F;
			}
			num++;
		}
		flag59 = j % 2 == 1 && array3[j] >= 110 && array3[j] < 123;
		if (flag59)
		{
			flag60 = array2[j] == (char)(array3[j] - j - 2);
			if (!flag60)
			{
				num++;
			}
		}
		else
		{
			num++;
		}
		goto IL_82F;
	}
	flag61 = num == 0;
	return flag61;

}

char nap[100][20];
char nap1[100][20];

int main(void)
{

	int i,j;
	int x = 0, A;

	while(x <16)
	{
		A = 0;
		for(i = 0x20; i< 0x7f; i++)
		{
			for(j=0x20;j<0x7f;j++)
			{
				array2[x] = i;
				array3[x] = j;
				if(fun(array2, array3, x) == 1)
				{
					nap[A][x] = array2[x];
					nap1[A][x] = array3[x];
					A += 1;
				}
			}
		}
		x += 1;
	}
	for(i=0;i<52;i++)
	{
		// printf("--------------------------\n");
		printf("[ '%s', '%s' ],\n",nap[i], nap1[i]);
	}
    return 0;
}