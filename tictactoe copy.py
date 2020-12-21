import random
import time


gameboard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def showGameboard():
    print("")
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] + "                  1 | 2 | 3"+"       X's Punktzahl:",  punktzahlX)
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] + "                  4 | 5 | 6")
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8] + "                  7 | 8 | 9"+"       O's Punktzahl:",  punktzahlO)


# -----------------------------------------------------Spielbrett------------------------------------------------------------------
X = "X"
x = "x"
O = "O"
o = "o"
dash = "-"
player1 = ("")
player2 = ("")


# ----------------------------------------------------- Var----------------------------------------------------------------------------
def choseChar():
    global player1Char
    player1Char = input("Möchtest du X oder O sein:")
    while player1Char != X or player1Char != x or player1Char != O or player1Char != o:
        if player1Char == X or player1Char == x:
            player1 = X
            player2 = O
            print("")
            print("Du bist " + player1 + " und spielst gegen " + player2)
            break
        elif player1Char == O or player1Char == o:
            player1 = O
            player2 = X
            print("")
            print("Du bist " + player1 + " und spielst gegen " + player2)
            break
        player1Char = input("Gebe bitte entweder X oder O ein:")


# -----------------------------------------------------Character Auswahl-------------------------------------------------------------
validNumbers = ["1","2","3","4","5","6","7","8","9"]

def spielerRundeX():
    eingabe = input("Wähle ein Feld:")
    while True:
        if eingabe not in validNumbers:
            eingabe = input("Wähle ein anderes Feld:")
            continue
        elif gameboard[int(eingabe) - 1] != dash:
            eingabe = input("Wähle ein anderes Feld:")
            continue
        elif gameboard[int(eingabe) - 1] == dash:
            for i in range(1, 10):
                if int(eingabe) == i:
                    gameboard[i-1] = X
                    break
                elif eingabe != i :
                    continue
            break
    showGameboard()



def spielerRundeO():
    eingabe = input("Wähle ein Feld:")
    while True:
        if eingabe not in validNumbers:
            eingabe = input("Wähle ein anderes Feld:")
            continue
        elif gameboard[int(eingabe) - 1] != dash:
            eingabe = input("Wähle ein anderes Feld:")
            continue
        elif gameboard[int(eingabe) - 1] == dash:
            for i in range(1, 10):
                if int(eingabe) == i:
                    gameboard[i-1] = O
                    break
                elif eingabe != i :
                    continue
            break
    showGameboard()

# -----------------------------------------------------players Turn------------------------------------------------------------------
def computerRundeX():
    which = random.randint(1,5)
    while winner == False or tie == False:
        if which == 1 or which == 2 or which == 3 or which == 4:
            executeLogicX()
            break
        elif which == 5:
            randomZahl = random.randint(1, 9)
            if gameboard[randomZahl - 1] == "-":
                gameboard[randomZahl - 1] = X
                print("Computer wählt....")
                time.sleep(1)
                print(randomZahl)
                break
            elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
                randomZahl = random.randint(1,9)
                continue
    showGameboard()
        
        


def computerRundeO():
    while winner == False or tie == False:
        if which == 1 or which == 2 or which == 3 or which == 4:
            executeLogicO()
            break
        elif which == 5:
            randomZahl = random.randint(1, 9)
            if gameboard[randomZahl - 1] == "-":
                gameboard[randomZahl - 1] = O
                print("Computer wählt....")
                time.sleep(1)
                print(randomZahl)
                break
            elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
                randomZahl = random.randint(1,9)
                continue
    showGameboard()
        
        



# -----------------------------------------------------Computers Turn------------------------------------------------------------------
def zeilenLogicPlacingO():
    if gameboard[0] == X and gameboard[1] == X and gameboard[2] == dash:
        gameboard[2] = O
    elif gameboard[0] == X and gameboard[1] == dash and gameboard[2] == X:
        gameboard[1] = O
    elif gameboard[0] == dash and gameboard[1] == X and gameboard[2] == X:
        gameboard[0] = O
    elif gameboard[3] == X and gameboard[4] == X and gameboard[5] == dash:
        gameboard[5] = O
    elif gameboard[3] == X and gameboard[4] == dash and gameboard[5] == X:
        gameboard[4] = O
    elif gameboard[3] == dash and gameboard[4] == X and gameboard[5] == X:
        gameboard[3] = O
    elif gameboard[6] == X and gameboard[7] == X and gameboard[8] == dash:
        gameboard[8] = O
    elif gameboard[6] == X and gameboard[7] == dash and gameboard[8] == X:
        gameboard[7] == O
    elif gameboard[6] == dash and gameboard[7] == X and gameboard[8] == X:
        gameboard[6] = O
    else:
        randomZahl = random.randint(1, 9)
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
    time.sleep(1)
    showGameboard()        


def reiheLogicPlacingO():
    if gameboard[0] == X and gameboard[3] == X and gameboard[6] == dash:
        gameboard[6] = O
    elif gameboard[0] == X and gameboard[3] == dash and gameboard[6] == X:
        gameboard[3] = O
    elif gameboard[0] == dash and gameboard[3] == X and gameboard[6] == X:
        gameboard[0] = O
    elif gameboard[1] == X and gameboard[4] == X and gameboard[7] == dash:
        gameboard[7] = O
    elif gameboard[1] == X and gameboard[4] == dash and gameboard[7] == X:
        gameboard[4] = O
    elif gameboard[1] == dash and gameboard[4] == X and gameboard[7] == X:
        gameboard[1] = O
    elif gameboard[2] == X and gameboard[5] == X and gameboard[8] == dash:
        gameboard[8] = O
    elif gameboard[2] == X and gameboard[5] == dash and gameboard[8] == X:
        gameboard[5] = O
    elif gameboard[2] == dash and gameboard[5] == X and gameboard[8] == X:
        gameboard[2] = O
    else:
        randomZahl = random.randint(1, 9)
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
    time.sleep(1)
    showGameboard()       


def diagonalLogicPlacingO():
    if gameboard[0] == X and gameboard[4] == X and gameboard[8] == dash:
        gameboard[8] = O
    elif gameboard[0] == X and gameboard[4] == dash and gameboard[8] == X:
        gameboard[4] = O
    elif gameboard[2] == dash and gameboard[4] == X and gameboard[6] == X:
        gameboard[0] = O
    elif gameboard[2] == X and gameboard[4] == X and gameboard[6] == dash:
        gameboard[6] = O
    elif gameboard[2] == X and gameboard[4] == dash and gameboard[6] == X:
        gameboard[4] = O
    elif gameboard[2] == dash and gameboard[4] == X and gameboard[6] == X:
        gameboard[2] = O
    else:
        randomZahl = random.randint(1, 9)
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
    time.sleep(1)
    showGameboard()        

# -----------------------------------------------------O------------------------------------------------------------------
def zeilenLogicPlacingX():
    if gameboard[0] == O and gameboard[1] == O and gameboard[2] == dash:
        gameboard[2] = X
    elif gameboard[0] == O and gameboard[1] == dash and gameboard[2] == O:
        gameboard[1] = X
    elif gameboard[0] == dash and gameboard[1] == O and gameboard[2] == O:
        gameboard[0] = X
    elif gameboard[3] == O and gameboard[4] == O and gameboard[5] == dash:
        gameboard[5] = X
    elif gameboard[3] == O and gameboard[4] == dash and gameboard[5] == O:
        gameboard[4] = X
    elif gameboard[3] == dash and gameboard[4] == O and gameboard[5] == O:
        gameboard[3] = X
    elif gameboard[6] == O and gameboard[7] == O and gameboard[8] == dash:
        gameboard[8] = X
    elif gameboard[6] == O and gameboard[7] == dash and gameboard[8] == O:
        gameboard[7] = X
    elif gameboard[6] == dash and gameboard[7] == O and gameboard[8] == O:
        gameboard[6] = X
    else:
        randomZahl = random.randint(1, 9)
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
    time.sleep(1)
    showGameboard()       


def reiheLogicPlacingX():
    if gameboard[0] == O and gameboard[3] == O and gameboard[6] == dash:
        gameboard[6] = X
    elif gameboard[0] == O and gameboard[3] == dash and gameboard[6] == O:
        gameboard[3] = X
    elif gameboard[0] == dash and gameboard[3] == O and gameboard[6] == O:
        gameboard[0] = X
    elif gameboard[1] == O and gameboard[4] == O and gameboard[7] == dash:
        gameboard[7] = X
    elif gameboard[1] == O and gameboard[4] == dash and gameboard[7] == O:
        gameboard[4] = X
    elif gameboard[1] == dash and gameboard[4] == O and gameboard[7] == O:
        gameboard[1] = X
    elif gameboard[2] == O and gameboard[5] == O and gameboard[8] == dash:
        gameboard[8] = X
    elif gameboard[2] == O and gameboard[5] == dash and gameboard[8] == O:
        gameboard[5] = X
    elif gameboard[2] == dash and gameboard[5] == O and gameboard[8] == O:
        gameboard[2] = X
    else:
        randomZahl = random.randint(1, 9)
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
    time.sleep(1)
    showGameboard()    


def diagonalLogicPlacingX():
    if gameboard[0] == O and gameboard[4] == O and gameboard[8] == dash:
        gameboard[8] = x
    elif gameboard[0] == O and gameboard[4] == dash and gameboard[8] == O:
        gameboard[4] = X
    elif gameboard[2] == dash and gameboard[4] == O and gameboard[6] == O:
        gameboard[0] = X
    elif gameboard[2] == O and gameboard[4] == O and gameboard[6] == dash:
        gameboard[6] = X
    elif gameboard[2] == O and gameboard[4] == dash and gameboard[6] == O:
        gameboard[4] = X
    elif gameboard[2] == dash and gameboard[4] == O and gameboard[6] == O:
        gameboard[2] = X
    else:
        randomZahl = random.randint(1, 9)
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
    time.sleep(1)
    showGameboard()     


# def computerRundeO():
#         zeilenLogicPlacingO()
#         reiheLogicPlacingO()
#         diagonalLogicPlacingO()



# def computerRundeX():
#     while True:
#         if zeilenLogicPlacingX() == True:
#             break
#         elif reiheLogicPlacingX() == True:
#             break
#         elif diagonalLogicPlacingX() == True:
#             break

# -----------------------------------------------------Computers SpielLogic------------------------------------------------------------------
reiheWinnerX = False
reiheWinnerO = False
columnWinnerX = False
columnWinnerO = False
diagonalWinnerX = False.conjugate
diagonalWinnerO = False
winner = False
tie = False


def zeileCheck():
    global winner
    global reiheWinnerX
    global reiheWinnerO
    if gameboard[0] == X and gameboard[1] == X and gameboard[2] == X:
        reiheWinnerX = True
        winner = True
    elif gameboard[0] == O and gameboard[1] == O and gameboard[2] == O:
        reiheWinnerO = True
        winner = True
    elif gameboard[3] == X and gameboard[4] == X and gameboard[5] == X:
        reiheWinnerX = True
        winner = True
    elif gameboard[3] == O and gameboard[4] == O and gameboard[5] == O:
        reiheWinnerO = True
        winner = True
    elif gameboard[6] == X and gameboard[7] == X and gameboard[8] == X:
        reiheWinnerX = True
        winner = True
    elif gameboard[6] == O and gameboard[7] == O and gameboard[8] == O:
        reiheWinnerO = True
        winner = True


def reiheCheck():
    global winner
    global columnWinnerX
    global columnWinnerO
    if gameboard[0] == X and gameboard[3] == X and gameboard[6] == X:
        columnWinnerX = True
        winner = True
    elif gameboard[0] == O and gameboard[3] == O and gameboard[6] == O:
        columnWinnerO = True
        winner = True
    elif gameboard[1] == X and gameboard[4] == X and gameboard[7] == X:
        columnWinnerX = True
        winner = True
    elif gameboard[1] == O and gameboard[4] == O and gameboard[7] == O:
        columnWinnerO = True
        winner = True
    elif gameboard[2] == X and gameboard[5] == X and gameboard[8] == X:
        columnWinnerX = True
        winner = True
    elif gameboard[2] == O and gameboard[5] == O and gameboard[8] == O:
        columnWinnerO = True
        winner = True


def diagonalCheck():
    global winner
    global diagonalWinnerX
    global diagonalWinnerO
    if gameboard[0] == X and gameboard[4] == X and gameboard[8] == X:
        diagonalWinnerX = True
        winner = True
    elif gameboard[0] == O and gameboard[4] == O and gameboard[8] == O:
        diagonalWinnerO = True
        winner = True
    elif gameboard[2] == X and gameboard[4] == X and gameboard[6] == X:
        diagonalWinnerX = True
        winner = True
    elif gameboard[2] == O and gameboard[4] == O and gameboard[6] == O:
        diagonalWinnerO = True
        winner = True


def tieCheck():
    if gameboard[0] != dash and gameboard[1] != dash and gameboard[2] != dash and gameboard[3] != dash and gameboard[4] != dash and gameboard[5] != dash and gameboard[6] != dash and gameboard[7] != dash and gameboard[8] != dash and winner == False:
        tie == True


def winnerCheck():
    zeileCheck()
    reiheCheck()
    diagonalCheck()
    tieCheck()


# -----------------------------------------------------Win check------------------------------------------------------------------
won = "hat gewonnen!"

def winnerAnnouncement():
    if reiheWinnerX == True:
        print("")
        print(X, won)
    elif reiheWinnerO == True:
        print("")
        print(O, won)
    elif columnWinnerX == True:
        print("")
        print(X, won)
    elif columnWinnerO == True:
        print("")
        print(O, won)
    elif diagonalWinnerX == True:
        print("")
        print(X, won)
    elif diagonalWinnerO == True:
        print("")
        print(O, won)
    elif tie == True:
        print("")
        print("Niemand hat gewonnen...")


# -----------------------------------------------------Winner announcement------------------------------------------------------------------


def playAndCheck():
    if player1Char == X or player1Char == x:
        while winner == False or tie == False:
            spielerRundeX()
            winnerCheck()
            winnerAnnouncement()
            if winner == True or tie == True:
                break
            computerRundeO()
            winnerCheck()
            winnerAnnouncement()
            if winner == True or tie == True:
                break
    elif player1Char == O or player1Char == o:
        while winner == False:
            spielerRundeO()
            winnerCheck()
            winnerAnnouncement()
            if winner == True or tie == True:
                break
            computerRundeX()
            winnerCheck()
            winnerAnnouncement()
            if winner == True or tie == True:
                break



# -----------------------------------------------------StartSpieler------------------------------------------------------------------
punktzahlX = 0
punktzahlO = 0

def pointCount():
    global punktzahlX
    global punktzahlO
    if reiheWinnerX == True:
        punktzahlX += 1    
    elif reiheWinnerO == True:
        punktzahlO += 1        
    elif columnWinnerX == True:
        punktzahlX += 1      
    elif columnWinnerO == True:
        punktzahlO += 1          
    elif diagonalWinnerX == True:
        punktzahlX += 1         
    elif diagonalWinnerO == True:
        punktzahlO += 1        
        

# -----------------------------------------------------Punktzahl Rechner------------------------------------------------------------------
def resetGame():
    global gameboard
    global reiheWinnerX
    global reiheWinnerO
    global columnWinnerX
    global columnWinnerO
    global diagonalWinnerX
    global diagonalWinnerO
    global winner
    global tie
    gameboard[0] = dash
    gameboard[1] = dash
    gameboard[2] = dash
    gameboard[3] = dash
    gameboard[4] = dash
    gameboard[5] = dash
    gameboard[6] = dash
    gameboard[7] = dash
    gameboard[8] = dash
    reiheWinnerX = False
    reiheWinnerO = False
    columnWinnerX = False
    columnWinnerO = False
    diagonalWinnerX = False
    diagonalWinnerO = False
    winner = False
    tie = False
# -----------------------------------------------------Game Reseter------------------------------------------------------------------


def playGame():
    showGameboard()
    playAndCheck()
    pointCount()
        

def startGame():
    choseChar()
    playGame()
    restart = input("Möchtest du wiederholen?(Ja/Nein):")
    while restart != "Ja" or restart != "ja" or restart == "Nein" or restart == "nein":
        if restart == "Ja" or restart == "ja":
            resetGame()
            playGame()
            continue
        elif restart == "Nein" or restart == "nein":
            print("Das Spiel ist vorbei.")
            break
        else:
            restart = input("Ja/Nein?:")
    



startGame()
    
    








