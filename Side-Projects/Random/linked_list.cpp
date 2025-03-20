#include <iostream> 
using namespace std;

class Complex {
    private:
        int r; //real
        int i; //imaginary

    public:
        Complex(int r1, int i1) 
        {
            r = r1;
            i = i1;
        }

        int getReal() {
            return r;
        }

        void print()
        {
            std::cout << r << " + " << i << "i"; 
        }
};

// class LinkedList {
//     private:
//         int data;
//         LinkedList *next;
//     public:
// };


int main() {
    std::cout << "this is test";
    Complex c1(2,4) ,c2(4,-6);
    
    c1.print();

    c2.print();


    return 0;

    char ch = 'a';
    int i = ch;
    std::cout << i;
}