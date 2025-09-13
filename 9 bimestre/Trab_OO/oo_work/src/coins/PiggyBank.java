package coins;

import utils.C;

import java.util.ArrayList;

public class PiggyBank {
    private final ArrayList<Coin> coinsList = new ArrayList<Coin>();

    public void add(Coin c) {
        coinsList.add(c);
    }

    public void list() {
        C.log("\nLISTA DE MOEDAS");
        if(coinsList.isEmpty()) {
            C.log("VAZIA\n\n");
            return;
        }
        for(var c : coinsList) {
            c.info();
        }

        C.log("\n\n");
    }

    public void remove(Coin c) {
        coinsList.remove(c);
    }

    public void totalInReal() {
        double total = 0;
        for(var c:coinsList) {
            total += c.convertToReal();
        }
        System.out.printf("O total em real é: R$ %.2f", total);
    }

}
