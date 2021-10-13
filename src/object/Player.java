package object;

import java.util.Scanner;

public class Player {
    private String character;
    private Scanner scanner;

    public Player(Scanner scanner){
        this.scanner = scanner;
    }

    public int takeTurn(){
        System.out.println("\nChose position to place your character("+character+"): ");
        int position = 0;
        boolean valid = false;
        do{
            try{
                position = Integer.parseInt(scanner.nextLine());
                if(position > 0 && position <= 9){
                    valid = true;
                }
            }catch (NumberFormatException e){
                System.out.println("(Invalid Input)");
            }catch (IllegalArgumentException e){
                System.out.println("(Number Invalid)");
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
