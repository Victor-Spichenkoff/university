package utils;

import java.io.Console;
import java.util.function.Function;


//To avoid errors with types, use Pascal
public class Input {
    private static final Console console = System.console();

    public static String String(String label) {
        C.logInLine(label);
        return console.readLine();
    }

    public static int Int(String label) {
        return retryParse(label, Integer::parseInt);
    }

    public static double Double(String label) {
        return retryParse(label, Double::parseDouble);
    }

    private static <T> T retryParse(String label, Function<String, T> parser) {
        while (true) {
            try {
                String input = String(label);
                return parser.apply(input);
            } catch (Exception e) {
                System.out.println("Entrada inválida. Tente novamente.");
            }
        }
    }
}