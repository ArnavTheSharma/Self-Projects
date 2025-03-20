
public class CarExample {
    public static void main(String args[]) {
        int x = 3;
        boolean a = (x % 2);
        System.out.println(a);
        Car car1 = new Car("Tesla", "Model Y", "8YR329", 0);
        Car car2 = new Car("Honda", "Pilot", "8YR329", 40);
        System.out.println(car1);
        System.out.println(car2);
    }

}

class Car {
    // make, model, license plate, isRunning, speed, 
    // startEngine, stopEngine
    // accelerate, decelerate, 
    private String make;
    private String model;
    private String licensePlate; 
    private int speed = 0;

    public String getMake() {
        return make;
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public String getSpeedInfo() {
        if (this.speed == 0) {
            return("No, parked");
        }
        else {
            return("Yes, moving at " + this.speed + " mph");
        }
    }

    public Car(String make, String model, String licensePlate, int speed) {
        this.make = make;
        this.model = model;
        this.licensePlate = licensePlate;
        this.speed = speed;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        
        sb.append(make).append(" ").append(model).append(" ");
        sb.append(" [License plate: ").append(licensePlate).append("]");
        sb.append(" [Is it moving?: ").append(this.getSpeedInfo()).append("]");

        return sb.toString();
    }
}
