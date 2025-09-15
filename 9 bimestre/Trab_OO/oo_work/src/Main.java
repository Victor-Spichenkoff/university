import coins.CoinFactory;
import coins.CoinType;
import coins.PiggyBank;
import utils.C;
import utils.Input;
import utils.Menu;

public class Main {
    public static void main(String[] args) {
        var piggyBank = new PiggyBank();
        //TODO: REMOVE THIS IF WANT REAL TESTING FROM ZERO
        var c1 = CoinFactory.create(CoinType.fromInt(1), 14);
        var c2 = CoinFactory.create(CoinType.fromInt(2), 14);
        var c3 = CoinFactory.create(CoinType.fromInt(3), 14);
        var c4 = CoinFactory.create(CoinType.fromInt(4), 14);
        var c5 = CoinFactory.create(CoinType.fromInt(5), 14);

        piggyBank.add(c1);
        piggyBank.add(c2);
        piggyBank.add(c3);
        piggyBank.add(c4);
        piggyBank.add(c5);

        piggyBank.list();
        piggyBank.totalInReal();

        piggyBank.removeById(2);

        piggyBank.list();

        while (true) {
            try {
                C.log("\n");
                Menu.MainMenu();

                var option = Input.Int("Escolha sua opção: ");

                switch (option) {
                    case 1:
                        Menu.CoinTypeMenu();
                        var type = Input.Int("digite o TIPO: ");
                        if (type < 0 || type > CoinType.values().length)
                            continue;

                        var value = Input.Double("Digite o VALOR: ");
                        if (value < 0)
                            continue;

                        piggyBank.add(CoinFactory.create(CoinType.fromInt(type), value));
                        break;
                    case 2:
                        piggyBank.list();
                        break;
                    case 3:
                        piggyBank.totalInReal();
                        break;
                    case 4:
                        //TODO FAZER
                        var id = Input.Int("Digite o ID: ");
                    piggyBank.removeById(id);
                        break;
                    case 0:
                        C.log("Até mais!");
                        return;
                    default:
                        C.log("Inválido! Tente novamente\n");
                        break;
                }
            } catch (Exception e) {
                C.log("\n=================");
                C.log("ERRO INESPERADO!");
                C.log("\n=================");
            }
        }
    }
}