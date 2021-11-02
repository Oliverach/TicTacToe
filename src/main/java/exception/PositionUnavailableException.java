package exception;

/**
 * The type Position unavailable exception.
 */
public class PositionUnavailableException extends Exception{
    /**
     * Instantiates a new Position unavailable exception.
     */
    public PositionUnavailableException(){
        super("Position taken!");
    }
}
