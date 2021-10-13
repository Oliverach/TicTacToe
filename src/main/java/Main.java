import java.util.Scanner;
import object.*;

public class Main {
    public static void main(String[] args) {
        try {
            Board board = new Board();
            Scanner scanner = new Scanner(System.in);
            Player player1 = new Player(scanner);
            Player player2 = new Player(scanner);
            Game game = new Game(board,scanner, player1, player2);
            game.start();
            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
