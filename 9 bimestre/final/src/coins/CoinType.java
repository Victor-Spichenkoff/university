package coins;

public enum CoinType {
    Real(1),
    Dollar(2),
    Euro(3),
    ArgentinePeso(4),
    Rublo(5);


    private final int code;

    CoinType(int code) {
        this.code = code;
    }

    public int getCode() {
        return code;
    }

    public static CoinType fromInt(int code) {
        for (CoinType type : CoinType.values()) {
            if (type.getCode() == code) {
                return type;
            }
        }
        throw new IllegalArgumentException("Código inválido para CoinType: " + code);
    }
}
