package object;

import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class Game {
    private final Board board;
    private final Scanner scanner;
    private final Player player1;
    private final Player player2;
    private boolean player1GoesFirst;

    public Game(Board board, Scanner scanner, Player player1, Player player2) {
        this.board = board;
        this.scanner = scanner;
        this.player1 = player1;
        this.player2 = player2;
    }

    private void choseCharacter() {
        System.out.println("Chose your Character:");
        String character = scanner.nextLine();
        if (!character.equals("x") && !character.equals("X") && !character.equals("o") && !character.equals("O")) {
            choseCharacter();
        } else {
            if (character.equals("x") || character.equals("X")) {
                player1.setCharacter("X");
                player2.setCharacter("O");
                this.player1GoesFirst = true;
                System.out.println("Player 1 = X\nPlayer 2 = O");
            } else {
                player2.setCharacter("X");
                player1.setCharacter("O");
                this.player1GoesFirst = false;
                System.out.println("Player 1 = O\nPlayer 2 = X");
            }
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }


    public void start() {
        choseCharacter();
        while (!playerHasWon()) {
            startNewRound();
        }
        scanner.close();
    }

    private void startNewRound() {
        //clearTerminal();
        board.displayBoard();
        if (player1GoesFirst) {
            letPlayerTakeTurn(player1);
            letPlayerTakeTurn(player2);
        } else {
            letPlayerTakeTurn(player2);
            letPlayerTakeTurn(player1);
        }
    }

    private void letPlayerTakeTurn(Player player) {
        int wantedPosition = player.takeTurn() - 1;
        if (board.getBoard()[wantedPosition] != null) {
            letPlayerTakeTurn(player);
        } else {
            board.updateBoardValue(wantedPosition, player.getCharacter());
        }
    }

    private void clearTerminal() {
        try {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows")) {
                Runtime.getRuntime().exec("cls");
            } else {
                Runtime.getRuntime().exec("clear");
            }
        } catch (final Exception e) {
            e.printStackTrace();
        }
    }

    private boolean playerHasWon() {
        // TODO
        return false;
    }

}
