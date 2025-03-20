// Practice OOP
//package shapes;
import java.util.LinkedList;
import java.lang.Math;

public class Polygon {
    private LinkedList<Line> edges;

    public Polygon(LinkedList<Line> edges) {
        this.edges = edges;
    }
}

class Line {
    private Coordinate endpoint1;
    private Coordinate endpoint2;

    public Line(Coordinate p1, Coordinate p2) {
        this.endpoint1 = p1;
        this.endpoint2 = p2;
    }

    public double getLength(){
        double changeInX = endpoint1.getX() - endpoint2.getX();
        double changeInY = endpoint1.getY() - endpoint2.getY();
        double changeInXSquared = Math.pow(changeInX, 2);
        double changeInYSquared = Math.pow(changeInY, 2);
        return(Math.pow(changeInXSquared + changeInYSquared, 0.5));
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

