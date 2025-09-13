package coins;

public class Real extends Coin {
    public Real(double value) {
        super(value);
        this.typeName = "Real";
    }


    @Override
    public double convertToReal() {
        return value;
    }
}
