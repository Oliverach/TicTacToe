package exception;

/**
 * The type Invalid number exception.
 */
public class InvalidNumberException extends Exception{

    /**
     * Instantiates a new Invalid number exception.
     */
    public InvalidNumberException() {
        super("Number must be greater then 0 and lower then 10");
    }
}
