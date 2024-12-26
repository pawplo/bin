#include <unistd.h>
#include <stdint.h>

int main()
{
    static uint8_t buf[4096];
    uint8_t last_char = '\n';

    while (1) {
        int r = read(0, buf, 4096);
        if (r > 0) {
            write(1, buf, r);
            last_char = buf[r-1];
            continue;
        }
        if (r < 0) {
            return 1;
        }

        if (last_char != '\n') {
            write(1, "\n", 1);
        }

        break;
    }

    return 0;
}
