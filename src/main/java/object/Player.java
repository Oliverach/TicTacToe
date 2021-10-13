package object;

import exception.InvalidNumberException;

import java.util.Scanner;

public class Player {
    private String character;
    private final Scanner scanner;

    public Player(Scanner scanner){
        this.scanner = scanner;
    }

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

    public void setCharacter(String character) {
        this.character = character;
    }

    public String getCharacter() {
        return character;
    }
}
