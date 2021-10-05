package object;

public class Board {
    private final String[] board = new String[9];

    public void displayBoard(){
        System.out.println(getBoardValue(0)+" | "+getBoardValue(1)+" | "+getBoardValue(2)+"   (1)|(2)|(3)");
        System.out.println("---------   -----------");
        System.out.println(getBoardValue(3)+" | "+getBoardValue(4)+" | "+getBoardValue(5)+"   (4)|(5)|(6)");
        System.out.println("---------   -----------");
        System.out.println(getBoardValue(6)+" | "+getBoardValue(7)+" | "+getBoardValue(8)+"   (7)|(8)|(9)");
    }

    public String getBoardValue(int position){
        if(board[position] == null){
            return "-";
        }else{
            return board[position];
        }
    }

    public String[] getBoard() {
        return board;
    }
    public void updateBoardValue(int position, String value){
        board[position] = value;
    }
}
