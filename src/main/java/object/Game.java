package object;
import java.util.Scanner;

public class Game {
    private final Board board;
    private final Scanner scanner;
    private final Player player1;
    private final Player player2;
    private boolean player1GoesFirst;
    private boolean end;

    public Game(Board board, Scanner scanner, Player player1, Player player2) {
        this.board = board;
        this.scanner = scanner;
        this.player1 = player1;
        this.player2 = player2;
    }


    private void choseCharacter() {
        System.out.println("Chose your Character(X/O):");
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
        }
    }

    public void start() {
        choseCharacter();
        board.displayBoard();
        while (!end) {
            startNewRound();
        }
        scanner.close();
    }

    private void startNewRound() {
//        clearTerminal();
        if (player1GoesFirst) {
            letPlayerTakeTurn(player1);
            if (!checkGameStatus()) {
                letPlayerTakeTurn(player2);
                checkGameStatus();
            }
        } else {
            letPlayerTakeTurn(player2);
            if (!checkGameStatus()) {
                letPlayerTakeTurn(player1);
                checkGameStatus();
            }
        }
    }

    private void letPlayerTakeTurn(Player player) {
        int wantedPosition = player.takeTurn()-1;
        if (board.getBoard()[wantedPosition] != null) {
            letPlayerTakeTurn(player);
        } else {
            board.updateBoardValue(wantedPosition, player.getCharacter());
        }
        board.displayBoard();
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

    public boolean checkIfPlayerWon() {
        String[] topRow = {board.getBoardValue(0), board.getBoardValue(1), board.getBoardValue(2)};
        String[] midRow = {board.getBoardValue(3), board.getBoardValue(4), board.getBoardValue(5)};
        String[] bottomRow = {board.getBoardValue(6), board.getBoardValue(7), board.getBoardValue(8)};
        String[] leftColumn = {board.getBoardValue(0), board.getBoardValue(3), board.getBoardValue(6)};
        String[] middleColumn = {board.getBoardValue(1), board.getBoardValue(4), board.getBoardValue(7)};
        String[] rightColumn = {board.getBoardValue(2), board.getBoardValue(5), board.getBoardValue(8)};
        String[] descendingDiagonal = {board.getBoardValue(0), board.getBoardValue(4), board.getBoardValue(8)};
        String[] ascendingDiagonal = {board.getBoardValue(6), board.getBoardValue(4), board.getBoardValue(2)};
        String[][] winningPatterns = {topRow, midRow, bottomRow, leftColumn, middleColumn, rightColumn, descendingDiagonal, ascendingDiagonal};
        String player1Char = player1.getCharacter();
        String player2Char = player2.getCharacter();
        for (String[] pattern : winningPatterns) {
            if (pattern[0].equals(player1Char) && pattern[1].equals(player1Char) && pattern[2].equals(player1Char)) {
                end = true;
                System.out.println(player1Char + " has won!");
                return true;
            }
            if (pattern[0].equals(player2Char) && pattern[1].equals(player2Char) && pattern[2].equals(player2Char)) {
                end = true;
                System.out.println(player2Char + " has won!");
                return true;
            }
        }
        return false;
    }

    public boolean checkGameStatus(){

        if(!checkIfPlayerWon()){
            if(board.checkIfBoardFull()){
                end = true;
                System.out.println("\nIt's a tie!");
                return true;
            }
            return false;
        } else{
            return true;
        }
    }

    public Board getBoard() {
        return board;
    }

    public Scanner getScanner() {
        return scanner;
    }

    public Player getPlayer1() {
        return player1;
    }

    public Player getPlayer2() {
        return player2;
    }

    public boolean isPlayer1GoesFirst() {
        return player1GoesFirst;
    }

    public void setPlayer1GoesFirst(boolean player1GoesFirst) {
        this.player1GoesFirst = player1GoesFirst;
    }

    public boolean isEnd() {
        return end;
    }

    public void setEnd(boolean end) {
        this.end = end;
    }
}
