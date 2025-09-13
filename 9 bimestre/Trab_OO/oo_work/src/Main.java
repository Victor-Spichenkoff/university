import coins.CoinFactory;
import coins.CoinType;
import coins.PiggyBank;
import coins.Real;
import utils.C;
import utils.Input;
import utils.Menu;

public class Main {
    public static void main(String[] args) {
        var piggyBank = new PiggyBank();
        var c1 = CoinFactory.Create(CoinType.fromInt(4), 14);
        var c2 = CoinFactory.Create(CoinType.fromInt(1), 14);
        var c3 = CoinFactory.Create(CoinType.fromInt(2), 14);


        piggyBank.add(c1);
        piggyBank.add(c2);
        piggyBank.add(c3);

        piggyBank.list();
        piggyBank.totalInReal();

        piggyBank.remove(c1);

        piggyBank.list();

        while (true) {
            Menu.MainMenu();

            var option = Input.Int("Escolha sua opção: ");

            switch (option) {
                case 1:
                    //
                    break;
                case 0:
                    C.log("Até mais!");
                    return;
                default:
                    C.log("Inválido! Tente novamente\n");
            }
        }
    }
}