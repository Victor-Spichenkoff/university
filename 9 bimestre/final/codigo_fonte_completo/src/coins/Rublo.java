package coins;

public class Rublo extends Coin {
    public Rublo(double value) {
        super(value);
        this.typeName = "Rublo";
    }


    @Override
    public double convertToReal() {
        return getValue() * 0.064;
    }
}
