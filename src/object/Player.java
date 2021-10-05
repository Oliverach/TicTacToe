package object;

import java.util.Scanner;

public class Player {
    private String character;
    private Scanner scanner;

    public Player(Scanner scanner){
        this.scanner = scanner;
    }

    public int takeTurn(){
        System.out.println("Chose position to place your character("+character+"): ");
        int position = scanner.nextInt();
        if (position>0 && position<=9){
            return position;
        }else{
            takeTurn();
        }
        return 0;
    }

    public void setCharacter(String character) {
        this.character = character;
    }

    public String getCharacter() {
        return character;
    }
}
