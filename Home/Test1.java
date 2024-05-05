

class Complex {
    int r;
    int i;

    void setValue(int param1, int param2) {
        r = param1;
        i = param2;
    }

    void setReal(int real) {
        r = real;
    }

    void addReal(int real) {
        r = r + real;
    }

    void addImaginary(int img) {
        i = i + img;
    }

    public String toString() {
        return r + "+" + i + "i";
    }


}

class Date {
    int month;
    int date;
    int year;
    





    public String toString() {
        return "" + month + '/' + date + '/' + year;
    }
}


class Test1 {
    public static void main(String[] args) {
        int a = 10;
        System.out.println("value of a is " + a);
        
        Complex c1 = new Complex();
        c1.setValue(4, 3);
        c1.setReal(5);
        System.out.println("Value of c1 is " + c1);

        c1.addReal(4);
        System.out.println("Value of c1 is " + c1);

        c1.addImaginary(-4);
        
        System.out.println("Value of c1 is " + c1);
        Date dt = new Date();
        System.out.println(dt.toString());
    }
}