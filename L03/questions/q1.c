#include<stdio.h>
#include<math.h>

int main() {
    int m, n, x;

    for (n = 1; n <= 83; n++) {
        x = n * n + 168;
        if (sqrt(x) == (int) sqrt(x)) {
            m = sqrt(x);
            printf("%d\n", m * m - 268);
        }
    }

    return 0;
}