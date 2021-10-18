package object;

public interface IPlayer {

    int takeTurn(String[] board) throws InterruptedException;

    void setCharacter(String character);

    String getCharacter();
}
