package coins;

public class Euro extends Coin {
    public Euro(double value) {
        super(value);
        this.typeName = "Euro";
    }


    @Override
    public double convertToReal() {
        return value * 6.28;
    }
}
