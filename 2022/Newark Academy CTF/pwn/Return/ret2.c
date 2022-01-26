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
