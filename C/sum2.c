#include <stdio.h>

int sum(int x, int y);

int main(void) {
    int a;
    int b;
    int c;
    printf("Enter first number: ");
    scanf("%d", &a);

    printf("Enter second number: ");
    scanf("%d", &b);

    //c = a + b;
    c = sum(a, b);

    printf("Total is %d\n", c);
    printf("value of a: %d",a);

    return 0;
}

int sum(int x, int y) {
    return x + y;
}