import coins.CoinFactory;
import coins.CoinType;
import coins.PiggyBank;
import utils.C;
import utils.Input;
import utils.Menu;

public class Main {
    public static void main(String[] args) {
        var piggyBank = new PiggyBank();

        while (true) {
            try {
                C.log("\n");
                Menu.mainMenu();

                var option = Input.Int("Escolha sua opcao: ");

                switch (option) {
                    case 1: // add
                        Menu.coinTypeMenu();
                        var type = Input.Int("digite o TIPO: ");
                        if (type < 0 || type > CoinType.values().length)
                            continue;

                        var value = Input.Double("Digite o VALOR: ");
                        if (value <= 0)
                            continue;

                        piggyBank.add(CoinFactory.create(CoinType.fromInt(type), value));
                        break;
                    case 2: // list
                        piggyBank.listCoins();
                        break;
                    case 3: // remove
                        var id = Input.Int("Digite o ID: ");
                        piggyBank.removeById(id);
                        break;
                    case 4:// total (R$)
                        piggyBank.totalInReal();
                        break;
                    case 0: // exit
                        C.log("Ate mais!");
                        return;
                    default:
                        C.log("Invalido! Tente novamente\n");
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