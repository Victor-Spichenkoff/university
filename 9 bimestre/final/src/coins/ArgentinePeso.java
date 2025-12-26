package coins;

public class ArgentinePeso extends Coin {
    public ArgentinePeso(double value) {
        super(value);
        this.typeName = "Peso Argentino";
    }


    @Override
    public double convertToReal() {
        return getValue() * 0.0037;
    }
}
