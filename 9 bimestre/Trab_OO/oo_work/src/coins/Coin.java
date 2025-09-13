package coins;

import utils.C;

import java.util.Objects;

public abstract class Coin {
    protected double value;
    public String typeName;

    Coin(double value) {
        this.value = value;
    }
    
    public void info() {
        C.log(typeName + " - " + value);
    }

    public abstract double convertToReal();
}
