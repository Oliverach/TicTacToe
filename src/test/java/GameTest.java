import object.Board;
import object.Game;
import object.Player;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import java.util.Scanner;

/**
 * The type Game test.
 */
public class GameTest {
    private static Game underTest;

    /**
     * Init.
     */
    @BeforeEach
    public void init() {
        Board board = new Board();
        Scanner scanner = new Scanner(System.in);
        Player player1 = new Player(scanner);
        Player player2 = new Player(scanner);
        underTest = new Game(board, scanner, player1, player2);
    }

    /**
     * Check if player has won equals true.
     */
    @Test
    public void checkIfPlayerHasWonEqualsTrue() {
        String[] state = {"X", "X", "X", null, null, null, null, null, null};
        underTest.getPlayer1().setCharacter("X");
        underTest.getPlayer2().setCharacter("O");
        underTest.getBoard().setBoard(state);
        Assertions.assertTrue(underTest.checkIfPlayerWon());
    }

    /**
     * Check if player has won equals false.
     */
    @Test
    public void checkIfPlayerHasWonEqualsFalse(){
        String[] state = {"X", "X", null, null, null, null, null, null, null};
        underTest.getPlayer1().setCharacter("X");
        underTest.getPlayer2().setCharacter("O");
        underTest.getBoard().setBoard(state);
        Assertions.assertFalse(underTest.checkIfPlayerWon());
    }

    /**
     * Game is tied equals true.
     */
    @Test
    public void gameIsTiedEqualsTrue(){
        String[] state = {"X", "X", "O", "O", "O", "X", "X", "O", "X"};
        underTest.getPlayer1().setCharacter("X");
        underTest.getPlayer2().setCharacter("O");
        underTest.getBoard().setBoard(state);
        Assertions.assertTrue(underTest.checkGameStatus());
    }
}
