#include <stdio.h>


int main(void) {
    _Bool boolVar = 0;
    int integer = 50; // 4 bytes, so max is 2^32 - 1
    long int longVar = 100L;

    float floarVar = 50.0f; // float 4 bytes, double 8 bytes
    double d;
    d = 12.9876543;
    d = 1.774e-5; // 1.774 = mantissa, -5 = exponent 
    char charVar = 'y';


    printf("bool: %i \n", boolVar);
    printf("int: %d, and it's octal is: %o (or if you want nice formatting, %#o) \n", integer, integer, integer);

    printf("floating point: %g", d);

    return 0;
}
