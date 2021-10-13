package object;

import exception.InvalidNumberException;

import java.util.Scanner;

/**
 * The type Player.
 */
public class Player {
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

    /**
     * Take turn int.
     *
     * @return the int
     */
    public int takeTurn(){

        int position = 0;
        boolean valid = false;
        do{
            try{
                System.out.println("\nChose position to place your character("+character+"): ");
                position = Integer.parseInt(scanner.nextLine());
                if(position > 0 && position <= 9){
                    valid = true;
                } else{
                    throw new InvalidNumberException();
                }
            }catch (NumberFormatException e){
                System.out.println("(Invalid Input)");
            }catch (InvalidNumberException e) {
                System.out.println(e.getMessage());
            }
        }while(!valid);
        return position;
    }

    /**
     * Sets character.
     *
     * @param character the character
     */
    public void setCharacter(String character) {
        this.character = character;
    }

    /**
     * Gets character.
     *
     * @return the character
     */
    public String getCharacter() {
        return character;
    }
}
