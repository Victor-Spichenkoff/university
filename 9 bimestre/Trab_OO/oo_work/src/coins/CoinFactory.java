package coins;

public class CoinFactory {
    public static Coin Create(CoinType type, double value) {

        return switch (type){
            case Real -> new Real(value);
            case Dollar -> new Dollar(value);
//            case Euro -> new Dollar(value);
            case ArgentinePeso -> new ArgentinePeso(value);
//            case Rublo -> new Dollar(value);
            default -> new Real(value);
        };
    }
}
