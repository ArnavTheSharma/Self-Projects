#include <stdio.h>


void merge(int a[], int b[], int c[]); // merges 2 sorted arrays (a and b) and puts into c
void mergeSort(int arr[], int size);


void print(int a[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d, ", a[i]);
    }
};

int main(void){
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);

    print(arr, size);
    return 0;
}