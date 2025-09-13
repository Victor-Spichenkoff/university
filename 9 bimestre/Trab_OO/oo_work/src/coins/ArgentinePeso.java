package coins;

public class ArgentinePeso extends Coin {
    public ArgentinePeso(double value) {
        super(value);
        this.typeName = "Peso Argentino";
    }


    @Override
    public double convertToReal() {
        return value * 0.0037;
    }
}
