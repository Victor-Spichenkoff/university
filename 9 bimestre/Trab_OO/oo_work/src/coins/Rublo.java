package coins;

public class Rublo extends Coin {
    public Rublo(double value) {
        super(value);
        this.typeName = "Rublo";
    }


    @Override
    public double convertToReal() {
        return value * 0.064;
    }
}
