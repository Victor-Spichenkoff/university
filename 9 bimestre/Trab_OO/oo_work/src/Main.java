import utils.C;
import utils.Input;
import utils.Menu;

public class Main {
    public static void main(String[] args) {
        while(true) {
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