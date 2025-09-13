package coins;

import utils.C;

import java.util.Objects;

public abstract class Coin {
    protected double value;

    public String typeName;

    Coin(double value) {
        this.value = value;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Coin coin = (Coin) o;
        return Double.compare(value, coin.value) == 0 && Objects.equals(typeName, coin.typeName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value, typeName);
    }

    public void info() {
        C.log(typeName + " - " + value);
    }

    public abstract double convertToReal();


}
