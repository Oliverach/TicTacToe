import java.util.InputMismatchException;
import java.util.Scanner;

import object.*;

/**
 * The type Main.
 */
public class Main {
    /**
     * The entry point of application.
     *
     * @param args the input arguments
     */
    public static void main(String[] args) {
        try {
            Board board = new Board();
            Scanner scanner = new Scanner(System.in);
            IPlayer player1 = new Player(scanner);
            IPlayer player2 = getSecondPlayerType(scanner);
            Game game = new Game(board, scanner, player1, player2);
            game.start();
            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static IPlayer getSecondPlayerType(Scanner scanner) {
        System.out.println("Singleplayer (1)");
        System.out.println("Multiplayer  (2)");
        System.out.println("Enter your choice:");
        int choice = 0;
        do {
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (InputMismatchException e) {
                System.out.println(e.getMessage());
            }
        } while (choice != 1 && choice != 2);

        if(choice == 1){
            return new Npc();
        }else{
            return new Player(scanner);
        }
    }
}
