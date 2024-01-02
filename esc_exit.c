#include <unistd.h>
#include <termios.h>

int main()
{
    static struct termios original_termios;

    tcgetattr(0, &original_termios);

    struct termios tmp_termios = original_termios;

    tmp_termios.c_cc[VMIN] = 0;
    tmp_termios.c_cc[VTIME] = 255;
    tmp_termios.c_lflag &= ~(ECHO | ICANON);

    tcsetattr(0, TCSAFLUSH, &tmp_termios);

    char byte;
    while (1) {
        if (read(0, &byte, 1) == 1) {
            if (byte == '\x1b')
                break;
        }
    }

    tcsetattr(0, TCSAFLUSH, &original_termios);
}
