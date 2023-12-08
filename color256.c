#include <stdio.h>

int main()
{
    for (int i = 0; i < 256; i++) {
        printf("\033[48;5;%dm\033[38;5;15m %03d ", i, i);
        printf("\033[33;5;0m\033[38;5;%dm %03d ", i, i);
        if (((i + 1)  % 16) == 0) {
            printf("\033[0m\n");
        }
    }

    return 0;
}