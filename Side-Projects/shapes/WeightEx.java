package Random.shapes;
// package shapes;

public class WeightEx {
    public static void main(String[] args) {
        Weight w = new Weight(); // LB
        Weight w1 = new Weight(Weight.KG);
    }    
}

enum WeightUom {
    KG, LB;
}
class Weight {
    public static final String KG = "kg";
    public static final String LB = "lb";
    
    //private String uom;
    private WeightUom uom;

    public Weight() {
        //uom = LB;
        uom = WeightUom.LB;
    }

    public Weight(String uom) {
        this.uom = uom;
    }

    public String getUnitOfMeasure() {
        return uom;
    }
}

