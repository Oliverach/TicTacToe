package exception;

public class InvalidNumberException extends Exception{

    public InvalidNumberException() {
        super("Number must be greater then 0 and lower then 10");
    }
}
