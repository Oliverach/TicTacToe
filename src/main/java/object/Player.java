package object;

import exception.InvalidNumberException;
import exception.PositionUnavailableException;

import java.util.Scanner;

/**
 * The type Player.
 */
public class Player implements IPlayer{
    private String character;
    private final Scanner scanner;

    /**
     * Instantiates a new Player.
     *
     * @param scanner the scanner
     */
    public Player(Scanner scanner){
        this.scanner = scanner;
    }


    @Override
    public int takeTurn(String[] board){
        int position = 0;
        boolean valid = false;
        do{
            try{
                System.out.println("\nChose position to place your character("+character+"): ");
                position = Integer.parseInt(scanner.nextLine());
                if(position > 0 && position <= 9){
                    if (board[position-1] == null) {

                        valid = true;
                    } else {
                        throw new PositionUnavailableException();
                    }

                } else{
                    throw new InvalidNumberException();
                }
            }catch (NumberFormatException e){
                System.out.println("(Invalid Input)");
            }catch (InvalidNumberException | PositionUnavailableException e) {
                System.out.println(e.getMessage());
            }
        }while(!valid);
        return position-1;
    }


    public void setCharacter(String character) {
        this.character = character;
    }

    public String getCharacter() {
        return character;
    }
}
