package utils;

public class C {
    public static void log(String text) {
        System.out.println(text);
    }

    public static void logInLine(String text) {
        System.out.print(text);
    }

    public static void debug(String text) {
        log(text);
    }
}
