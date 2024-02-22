#include <unistd.h>
#include <stdio.h>
#include <errno.h>

unsigned int sleep(unsigned int __seconds) {
    char flag[100];
    FILE *f = fopen("/home/chal/flag.txt", "r");
    if (f) {
        fgets(flag, sizeof(flag), f);
        printf("Flag: %s\n", flag);
        fclose(f);
    } else {
        printf("Failed to open file\n");
    }
    return 0;
}