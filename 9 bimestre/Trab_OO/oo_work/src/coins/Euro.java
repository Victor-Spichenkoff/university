package coins;

public class Euro extends Coin {
    public Euro(double value) {
        super(value);
        this.typeName = "Euro";
    }


    @Override
    public double convertToReal() {
        return getValue() * 6.28;
    }
}
