#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    char c[2];
    unsigned char b;
    while (read(0, c, 2) == 2) {
        b = 0;
        if (c[0] >= '0' && c[0] <= '9')
            b += (c[0] - '0') << 4;
        else if (c[0] >= 'a' && c[0] <= 'f')
            b += (c[0] - 'a' + 10) << 4;
        else if (c[0] >= 'A' && c[0] <= 'F')
            b += (c[0] - 'A' + 10) << 4;
        else {
            fprintf(stderr, "char [%c][%d] is not hex code.\n", c[0], (int)c[0]);
            return 1;
        }

        if (c[1] >= '0' && c[1] <= '9')
            b += c[1] - '0';
        else if (c[1] >= 'a' && c[1] <= 'f')
            b += c[1] - 'a' + 10;
        else if (c[1] >= 'A' && c[1] <= 'F')
            b += c[1] - 'A' + 10;
        else {
            fprintf(stderr, "char [%c][%d] is not hex code.\n", c[1], (int)c[1]);
            return 1;
        }
        write(1, &b, 1);
    }

    return 0;
}

