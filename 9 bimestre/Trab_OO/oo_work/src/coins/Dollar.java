package coins;

public class Dollar extends Coin {
    public Dollar(double value) {
        super(value);
        this.typeName = "Dólar";
    }


    @Override
    public double convertToReal() {
        return getValue() * 5.35;
    }
}
