package coins;

import utils.C;


public abstract class Coin {
    private double value;
    public String typeName;
    
    Coin(double value) {
        setValue(value);
    }
    
    public void info() {
        C.log(typeName + " - " + value);
    }

    public abstract double convertToReal();

    // GETTERS SETTERS
    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        if(value < 0)
            this.value = 0;
        else
            this.value = value;
    }
}
