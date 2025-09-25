package coins;

import utils.C;
import utils.IdManager;


public abstract class Coin {
    private double value;
    public String typeName = "Moeda";
    private int id;
    
    Coin(double value) {
        setId(IdManager.getNewId());
        setValue(value);
    }


    public void info() {
        C.log(id + " | " + typeName + " - " + value);
    }


    // to override
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

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
