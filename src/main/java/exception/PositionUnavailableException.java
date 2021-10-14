package exception;

public class PositionUnavailableException extends Exception{
    public PositionUnavailableException(){
        super("Position taken!");
    }
}
