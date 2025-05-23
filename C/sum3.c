#include <stdio.h>

struct complex {
    int real;
    int imaginary;
};

struct complex sum(struct complex x, struct complex y);

int main(void) {
    struct complex complex1 = {1, 2};
    struct complex complex2;

    printf("Enter real part of second complex number: ");
    scanf("%d", &complex2.real);
    
    printf("Enter imaginary part of second complex number: ");
    scanf("%d", &complex2.imaginary);

    struct complex result = sum(complex1, complex2);
    printf("result complex number is %d + %di", result.real, result.imaginary);

    return 0;
}


struct complex sum(struct complex x, struct complex y) {
    struct complex result;
    result.real = x.real + y.real;
    result.imaginary = x.imaginary + y.imaginary;
    return result;
}