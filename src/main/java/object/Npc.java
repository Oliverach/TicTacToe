package object;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class Npc implements IPlayer {

    private String character;


    @Override
    public int takeTurn(String[] board) {
        System.out.println("NPC choosing position...");
        int[] topRow = {0, 1, 2};
        int[] midRow = {3, 4, 5};
        int[] bottomRow = {6, 7, 8};
        int[] leftColumn = {0, 3, 6};
        int[] middleColumn = {1, 4, 7};
        int[] rightColumn = {2, 5, 8};
        int[] descendingDiagonal = {0, 4, 8};
        int[] ascendingDiagonal = {6, 4, 2};
        int[][] allPattern = {topRow, midRow, bottomRow, leftColumn, middleColumn, rightColumn, descendingDiagonal, ascendingDiagonal};

        if(board[4] == null){
            return 4;
        }

        for (int[] pattern: allPattern){
            int counter = 0;
            for(int i: pattern){
                if (board[i]!= null && board[i].equals(getCharacter())){
                    counter++;
                    if(counter==2){
                        for (int k : pattern) {
                            if (board[k] == null) {
                                return k;
                            }
                        }
                    }
                }
            }
        }

        for (int[] pattern: allPattern){
            int counter = 0;
            for(int i: pattern){
                if (board[i]!= null && board[i].equals(getOpponentCharacter())){
                    counter++;
                    if(counter==2){
                        for (int k : pattern) {
                            if (board[k] == null) {
                                return k;
                            }
                        }
                    }
                }
            }
        }

        Random rand = new Random();
        int randNumb = rand.nextInt(9);
        while (board[randNumb] != null){
            randNumb = rand.nextInt(9);
        }
        try{
            TimeUnit.SECONDS.sleep(1);
        }catch (InterruptedException e){
            System.out.println(e.getMessage());
        }

        return randNumb;
    }


    @Override
    public void setCharacter(String character) {
        this.character = character;
    }

    @Override
    public String getCharacter() {
        return character;
    }

    private String getOpponentCharacter(){
        if(character.equals("X")){
            return "O";
        }else{
            return "X";
        }
    }
}
