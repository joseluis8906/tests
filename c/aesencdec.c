#include <stdio.h>
#include <time.h>

int main (void)
{
    time_t Now;
    time (&Now);
    Now += 120;
    printf ("%s\n", ctime(&Now));
    return 0;
}
