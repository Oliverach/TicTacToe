import object.Board;
import object.Game;
import object.Player;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            Board board = new Board();
            Player player1 = new Player(new Scanner(System.in));
            Player player2 = new Player(new Scanner(System.in));
            Game game = new Game(board,new Scanner(System.in), player1, player2);
            game.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
