package utils;

public class IdManager {
    private static int currentId = 0;

    public static int getNewId() {
        currentId++;
        return currentId;
    }
}
