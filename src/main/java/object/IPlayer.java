package object;

/**
 * The interface Player.
 */
public interface IPlayer {

    /**
     * Take turn int.
     *
     * @param board the board
     * @return the int
     * @throws InterruptedException the interrupted exception
     */
    int takeTurn(String[] board) throws InterruptedException;

    /**
     * Sets character.
     *
     * @param character the character
     */
    void setCharacter(String character);

    /**
     * Gets character.
     *
     * @return the character
     */
    String getCharacter();
}
