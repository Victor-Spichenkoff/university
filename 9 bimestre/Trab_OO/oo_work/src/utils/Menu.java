package utils;

public class Menu {
    public static void MainMenu() {
        C.log("Escolha uma opção");
        C.log("[ 1 ] Adicionar");
        C.log("[ 2 ] Listar");
        C.log("[ 3 ] Remover");
        C.log("[ 4 ] Total em Real");
        C.log("[ 0 ] Sair");
    }

    public static void CoinTypeMenu() {
        C.log("Escolha um tipo de moeda");
        C.log("[ 1 ] Real");
        C.log("[ 2 ] Dólar");
        C.log("[ 3 ] Euro");
        C.log("[ 4 ] Peso Argentino");
        C.log("[ 5 ] Rublo");
    }
}
