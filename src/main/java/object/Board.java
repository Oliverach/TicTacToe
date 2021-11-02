package object;

/**
 * The type Board.
 */
public class Board {
    private String[] board;

    public Board(){
        board = new String[9];
    }

    /**
     * Display board.
     */
    public void displayBoard(){
        System.out.println("\n");
        System.out.println(getBoardValue(0)+" | "+getBoardValue(1)+" | "+getBoardValue(2)+"   (1)|(2)|(3)");
        System.out.println("---------   -----------");
        System.out.println(getBoardValue(3)+" | "+getBoardValue(4)+" | "+getBoardValue(5)+"   (4)|(5)|(6)");
        System.out.println("---------   -----------");
        System.out.println(getBoardValue(6)+" | "+getBoardValue(7)+" | "+getBoardValue(8)+"   (7)|(8)|(9)");
    }

    /**
     * Get board value string.
     *
     * @param position the position
     * @return the string
     */
    public String getBoardValue(int position){
        if(board[position] == null){
            return "-";
        }else{
            return board[position];
        }
    }

    /**
     * Get board string [ ].
     *
     * @return the string [ ]
     */
    public String[] getBoard() {
        return board;
    }

    /**
     * Update board value.
     *
     * @param position the position
     * @param value    the value
     */
    public void updateBoardValue(int position, String value){
        board[position] = value;
    }

    /**
     * Check if board full boolean.
     *
     * @return the boolean
     */
    public boolean checkIfBoardFull(){
        boolean full = true;
        for (String i:board){
            if (i == null) {
                full = false;
                break;
            }
        }
        return full;
    }

    /**
     * Set board.
     *
     * @param board the board
     */
    public void setBoard(String[] board){
        this.board = board;
    }
}
