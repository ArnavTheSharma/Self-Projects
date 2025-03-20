package Random.shapes;
//package shapes;
import java.lang.Math;

public class PolygonTest {
    public static void main(String[] args) {
        Coordinate origin = new Coordinate(0, 0);
        Circle circle = new Circle(5.0f, origin);
        System.out.println("Circle area: " + circle.getArea());

        Coordinate c1 = new Coordinate(0, 0);
        Coordinate c2 = new Coordinate(1, 0);
        Coordinate c3 = new Coordinate(1, 1);
        Coordinate c4 = new Coordinate(0, 1);

        Line l1 = new Line(c1, c2);
        Line l2 = new Line(c2, c3);
        Line l3 = new Line(c3, c4);
        Line l4 = new Line(c4, c1);
        
        Rectangle rect = new Rectangle(l1, l2, l3, l4);
        System.out.println("Rectangle area: " + rect.getArea());

        Shape circle1 = new Circle();
        System.out.println("Area of " + circle1.getName() + " is " + circle1.getArea() );

        Shape line = new Line();
        System.out.println("Area of " + line.getName() + " is " + line.getArea() );

        Shape rectangle = new Rectangle();
        System.out.println("Area of " + rectangle.getName() + " is " + rectangle.getArea() );

        Shape square = new Square(); 
        System.out.println("Area of " + square.getName() + " is " + square.getArea() );
    }
}
/* 
abstract class Shape {
    protected String name;
    abstract public String getName();
}
*/

interface Shape {
    public String getName();
    public double getArea();
}

//class Circle extends Shape{
class Circle implements Shape {
    private float radius;
    private Coordinate center;

    public Circle() {
        radius = 0;
        center = null;
    }

    public Circle(float r, Coordinate c) {
        this.radius = r;
        this.center = c;
    }

    @Override
    public String getName() {
        return "Circle";
    }

    public double getArea() {
        return(3.14*(Math.pow(this.radius,2)));
    }
}

class Rectangle implements Shape {
    private Line line1, line2, line3, line4;

    //private static Rectangle instance = new Rectangle();

    // public static Rectangle getInstance() {
    //     return instance;
    // }

    public Rectangle() {
        this.line1 = null;
        this.line2 = null;
        this.line3 = null;
        this.line4 = null;
    }

    public Rectangle(Line line1, Line line2, Line line3, Line line4){
        this.line1 = line1;
        this.line2 = line2;
        this.line3 = line3;
        this.line4 = line4;
    }

    @Override
    public String getName() {
        return("Rectangle");
    }
    public double getArea() {
        if (this.line1 == null || this.line2 == null) {
            return(0);
        }
        else {
            return(this.line1.getArea() * this.line2.getArea());
        }
    }
}


//class Square implements Shape {
class Square extends Rectangle  {
    private float sideLength;

    public Square() {
        //this.sideLength = 0;
        super();
    }
    public Square(Line l){
        //this.sideLength = l;
        super(l, l, l, l);
    }

    @Override
    public String getName() {
        return("Square");
    }
    public double getArea() {
        return(this.sideLength * this.sideLength);
    }
}

class Line implements Shape {
    private Coordinate endpoint1;
    private Coordinate endpoint2;

    public Line() {
        this.endpoint1 = null;
        this.endpoint2 = null;
    }

    public Line(Coordinate p1, Coordinate p2) {
        this.endpoint1 = p1;
        this.endpoint2 = p2;
    }

    @Override
    public double getArea(){
        double changeInX = 0;
        double changeInY = 0;
        if(endpoint1 != null && endpoint2 != null) {
            changeInX = endpoint1.getX() - endpoint2.getX();
            changeInY = endpoint1.getY() - endpoint2.getY();
        }

        double changeInXSquared = Math.pow(changeInX, 2);
        double changeInYSquared = Math.pow(changeInY, 2);
        return(Math.pow(changeInXSquared + changeInYSquared, 0.5));
    }
    public String getName() {
        return("Line");
    }
}

class Coordinate {
    private float x, y;

    public Coordinate(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float getX() {
        return(this.x);
    }

    public float getY() {
        return(this.y);
    }
}

