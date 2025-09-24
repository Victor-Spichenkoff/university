package coins;

public class CoinFactory {
    public static Coin create(CoinType type, double value) {

        return switch (type){
            case Real -> new Real(value);
            case Dollar -> new Dollar(value);
            case Euro -> new Euro(value);
            case ArgentinePeso -> new ArgentinePeso(value);
            case Rublo -> new Rublo(value);
        };
    }
}
