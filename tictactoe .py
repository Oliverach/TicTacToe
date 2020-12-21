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
    while True:
        logicBlockingX()
        if logicBlockingX() == None:
            logicPlacingX()
            if logicPlacingX() == None:
                randomPlacingX()
            else:
                logicPlacingX() == None
                break
        else:
            logicBlockingX() == None
            break
    showGameboard()
        

        


def computerRundeO():
    while True:
        logicBlockingO()
        if logicBlockingO() == None:
            logicPlacingO()
            if logicPlacingO() == None:
                randomPlacingO()
            else:
                logicPlacingO() == None
                break
        else:
            logicBlockingO() == None
            break
    showGameboard()
        
        



# -----------------------------------------------------Computers Turn------------------------------------------------------------------
def randomPlacingO():
    randomZahl = random.randint(1, 9)
    while True:
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = O
            print("Computer wählt....")
            time.sleep(1)
            print(randomZahl)
            break
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
            continue


def randomPlacingX():
    randomZahl = random.randint(1, 9)
    while True:
        if gameboard[randomZahl - 1] == "-":
            gameboard[randomZahl - 1] = X
            print("Computer wählt....")
            time.sleep(1)
            print(randomZahl)
            break
        elif gameboard[randomZahl - 1] == X or gameboard[randomZahl - 1] == O:
            randomZahl = random.randint(1,9)
            continue





def zeileLogicBlockingO():
    if gameboard[0] == X and gameboard[1] == X and gameboard[2] == dash:
        gameboard[2] = O
        return 3
    elif gameboard[0] == X and gameboard[1] == dash and gameboard[2] == X:
        gameboard[1] = O
        return 2
    elif gameboard[0] == dash and gameboard[1] == X and gameboard[2] == X:
        gameboard[0] = O
        return 1
    elif gameboard[3] == X and gameboard[4] == X and gameboard[5] == dash:
        gameboard[5] = O
        return 6
    elif gameboard[3] == X and gameboard[4] == dash and gameboard[5] == X:
        gameboard[4] = O
        return 5
    elif gameboard[3] == dash and gameboard[4] == X and gameboard[5] == X:
        gameboard[3] = O
        return 4
    elif gameboard[6] == X and gameboard[7] == X and gameboard[8] == dash:
        gameboard[8] = O
        return 9
    elif gameboard[6] == X and gameboard[7] == dash and gameboard[8] == X:
        gameboard[7] == O
        return 8
    elif gameboard[6] == dash and gameboard[7] == X and gameboard[8] == X:
        gameboard[6] = O
        return 7
    print("Computer wählt...")
    time.sleep(1)
    print(zeileLogicBlockingO())
 

print("De Gregor isch voll krass!!")

def reiheLogicBlockingO():
    if gameboard[0] == X and gameboard[3] == X and gameboard[6] == dash:
        gameboard[6] = O
        return 7
    elif gameboard[0] == X and gameboard[3] == dash and gameboard[6] == X:
        gameboard[3] = O
        return 4
    elif gameboard[0] == dash and gameboard[3] == X and gameboard[6] == X:
        gameboard[0] = O
        return 1
    elif gameboard[1] == X and gameboard[4] == X and gameboard[7] == dash:
        gameboard[7] = O
        return 8
    elif gameboard[1] == X and gameboard[4] == dash and gameboard[7] == X:
        gameboard[4] = O
        return 5
    elif gameboard[1] == dash and gameboard[4] == X and gameboard[7] == X:
        gameboard[1] = O
        return 2
    elif gameboard[2] == X and gameboard[5] == X and gameboard[8] == dash:
        gameboard[8] = O
        return 9
    elif gameboard[2] == X and gameboard[5] == dash and gameboard[8] == X:
        gameboard[5] = O
        return 6
    elif gameboard[2] == dash and gameboard[5] == X and gameboard[8] == X:
        gameboard[2] = O
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(reiheLogicBlockingO())
 


def diagonalLogicBlockingO():
    if gameboard[0] == X and gameboard[4] == X and gameboard[8] == dash:
        gameboard[8] = O
        return 9
    elif gameboard[0] == X and gameboard[4] == dash and gameboard[8] == X:
        gameboard[4] = O
        return 5
    elif gameboard[2] == dash and gameboard[4] == X and gameboard[6] == X:
        gameboard[0] = O
        return 1
    elif gameboard[2] == X and gameboard[4] == X and gameboard[6] == dash:
        gameboard[6] = O
        return 7
    elif gameboard[2] == X and gameboard[4] == dash and gameboard[6] == X:
        gameboard[4] = O
        return 5
    elif gameboard[2] == dash and gameboard[4] == X and gameboard[6] == X:
        gameboard[2] = O
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(diagonalLogicBlockingO())



# -----------------------------------------------------O------------------------------------------------------------------
def zeilenLogicBlockingX():
    if gameboard[0] == O and gameboard[1] == O and gameboard[2] == dash:
        gameboard[2] = X
        return 3
    elif gameboard[0] == O and gameboard[1] == dash and gameboard[2] == O:
        gameboard[1] = X
        return 2
    elif gameboard[0] == dash and gameboard[1] == O and gameboard[2] == O:
        gameboard[0] = X
        return 1
    elif gameboard[3] == O and gameboard[4] == O and gameboard[5] == dash:
        gameboard[5] = X
        return 6
    elif gameboard[3] == O and gameboard[4] == dash and gameboard[5] == O:
        gameboard[4] = X
        return 5
    elif gameboard[3] == dash and gameboard[4] == O and gameboard[5] == O:
        gameboard[3] = X
        return 4
    elif gameboard[6] == O and gameboard[7] == O and gameboard[8] == dash:
        gameboard[8] = X
        return 9
    elif gameboard[6] == O and gameboard[7] == dash and gameboard[8] == O:
        gameboard[7] = X
        return 8
    elif gameboard[6] == dash and gameboard[7] == O and gameboard[8] == O:
        gameboard[6] = X
    print("Computer wählt...")
    time.sleep(1)
    print(zeilenLogicBlockingX())
 
   

def reiheLogicBlockingX():
    if gameboard[0] == O and gameboard[3] == O and gameboard[6] == dash:
        gameboard[6] = X
        return 7
    elif gameboard[0] == O and gameboard[3] == dash and gameboard[6] == O:
        gameboard[3] = X
        return 4
    elif gameboard[0] == dash and gameboard[3] == O and gameboard[6] == O:
        gameboard[0] = X
        return 1
    elif gameboard[1] == O and gameboard[4] == O and gameboard[7] == dash:
        gameboard[7] = X
        return 8
    elif gameboard[1] == O and gameboard[4] == dash and gameboard[7] == O:
        gameboard[4] = X
        return 5
    elif gameboard[1] == dash and gameboard[4] == O and gameboard[7] == O:
        gameboard[1] = X
        return 2
    elif gameboard[2] == O and gameboard[5] == O and gameboard[8] == dash:
        gameboard[8] = X
        return 9
    elif gameboard[2] == O and gameboard[5] == dash and gameboard[8] == O:
        gameboard[5] = X
        return 6
    elif gameboard[2] == dash and gameboard[5] == O and gameboard[8] == O:
        gameboard[2] = X
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(reiheLogicBlockingX())
 
     


def diagonalLogicBlockingX():
    if gameboard[0] == O and gameboard[4] == O and gameboard[8] == dash:
        gameboard[8] = x
        return 9
    elif gameboard[0] == O and gameboard[4] == dash and gameboard[8] == O:
        gameboard[4] = X
        return 5
    elif gameboard[2] == dash and gameboard[4] == O and gameboard[6] == O:
        gameboard[0] = X
        return 1
    elif gameboard[2] == O and gameboard[4] == O and gameboard[6] == dash:
        gameboard[6] = X
        return 7
    elif gameboard[2] == O and gameboard[4] == dash and gameboard[6] == O:
        gameboard[4] = X
        return 5
    elif gameboard[2] == dash and gameboard[4] == O and gameboard[6] == O:
        gameboard[2] = X
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(diagonalLogicBlockingX())
    

         
def logicBlockingO():
    zeileLogicBlockingO()
    reiheLogicPlacingO
    diagonalLogicBlockingO


def logicBlockingX():
    zeilenLogicBlockingX()
    reiheLogicBlockingX()
    diagonalLogicBlockingX()


# -----------------------------------------------------ComputersblockLogic------------------------------------------------------------------
def zeileLogicPlacingX():
    if gameboard[0] == X and gameboard[1] == X and gameboard[2] == dash:
        gameboard[2] = X
        return 3
    elif gameboard[0] == X and gameboard[1] == dash and gameboard[2] == X:
        gameboard[1] = X
        return 2
    elif gameboard[0] == dash and gameboard[1] == X and gameboard[2] == X:
        gameboard[0] = X
        return 1
    elif gameboard[3] == X and gameboard[4] == X and gameboard[5] == dash:
        gameboard[5] = X
        return 6
    elif gameboard[3] == X and gameboard[4] == dash and gameboard[5] == X:
        gameboard[4] = X
        return 5
    elif gameboard[3] == dash and gameboard[4] == X and gameboard[5] == X:
        gameboard[3] = X
        return 4
    elif gameboard[6] == X and gameboard[7] == X and gameboard[8] == dash:
        gameboard[8] = X
        return 9
    elif gameboard[6] == X and gameboard[7] == dash and gameboard[8] == X:
        gameboard[7] == X
        return 8
    elif gameboard[6] == dash and gameboard[7] == X and gameboard[8] == X:
        gameboard[6] = X
        return 7
    print("Computer wählt...")
    time.sleep(1)
    print(zeileLogicPlacingX())
    
 


def reiheLogicPlacingX():
    if gameboard[0] == X and gameboard[3] == X and gameboard[6] == dash:
        gameboard[6] = X
        return 7
    elif gameboard[0] == X and gameboard[3] == dash and gameboard[6] == X:
        gameboard[3] = X
        return 7
    elif gameboard[0] == dash and gameboard[3] == X and gameboard[6] == X:
        gameboard[0] = X
        return 7
    elif gameboard[1] == X and gameboard[4] == X and gameboard[7] == dash:
        gameboard[7] = X
        return 7
    elif gameboard[1] == X and gameboard[4] == dash and gameboard[7] == X:
        gameboard[4] = X
        return 7
    elif gameboard[1] == dash and gameboard[4] == X and gameboard[7] == X:
        gameboard[1] = X
        return 7
    elif gameboard[2] == X and gameboard[5] == X and gameboard[8] == dash:
        gameboard[8] = X
        return 7
    elif gameboard[2] == X and gameboard[5] == dash and gameboard[8] == X:
        gameboard[5] = X
        return 7
    elif gameboard[2] == dash and gameboard[5] == X and gameboard[8] == X:
        gameboard[2] = X
        return 7
    print("Computer wählt...")
    time.sleep(1)
    print(reiheLogicPlacingX())
    
    


def diagonalLogicPlacingX():
    if gameboard[0] == X and gameboard[4] == X and gameboard[8] == dash:
        gameboard[8] = X
        return 9
    elif gameboard[0] == X and gameboard[4] == dash and gameboard[8] == X:
        gameboard[4] = X
        return 5
    elif gameboard[2] == dash and gameboard[4] == X and gameboard[6] == X:
        gameboard[0] = X
        return 1
    elif gameboard[2] == X and gameboard[4] == X and gameboard[6] == dash:
        gameboard[6] = X
        return 7
    elif gameboard[2] == X and gameboard[4] == dash and gameboard[6] == X:
        gameboard[4] = X
        return 5
    elif gameboard[2] == dash and gameboard[4] == X and gameboard[6] == X:
        gameboard[2] = X
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(diagonalLogicPlacingX())
       

# -----------------------------------------------------O------------------------------------------------------------------
def zeileLogicPlacingO():
    if gameboard[0] == O and gameboard[1] == O and gameboard[2] == dash:
        gameboard[2] = O
        return 3
    elif gameboard[0] == O and gameboard[1] == dash and gameboard[2] == O:
        gameboard[1] = O
        return 2
    elif gameboard[0] == dash and gameboard[1] == O and gameboard[2] == O:
        gameboard[0] = O
        return 1
    elif gameboard[3] == O and gameboard[4] == O and gameboard[5] == dash:
        gameboard[5] = O
        return 6
    elif gameboard[3] == O and gameboard[4] == dash and gameboard[5] == O:
        gameboard[4] = O
        return 5
    elif gameboard[3] == dash and gameboard[4] == O and gameboard[5] == O:
        gameboard[3] = O
        return 4
    elif gameboard[6] == O and gameboard[7] == O and gameboard[8] == dash:
        gameboard[8] = O
        return 9
    elif gameboard[6] == O and gameboard[7] == dash and gameboard[8] == O:
        gameboard[7] = O
        return 8
    elif gameboard[6] == dash and gameboard[7] == O and gameboard[8] == O:
        gameboard[6] = O
        return 7
    print("Computer wählt...")
    time.sleep(1)
    print(zeileLogicPlacingO())
       
    
   

def reiheLogicPlacingO():
    if gameboard[0] == O and gameboard[3] == O and gameboard[6] == dash:
        gameboard[6] = O
        return 7
    elif gameboard[0] == O and gameboard[3] == dash and gameboard[6] == O:
        gameboard[3] = O
        return 4
    elif gameboard[0] == dash and gameboard[3] == O and gameboard[6] == O:
        gameboard[0] = O
        return 1
    elif gameboard[1] == O and gameboard[4] == O and gameboard[7] == dash:
        gameboard[7] = O
        return 8
    elif gameboard[1] == O and gameboard[4] == dash and gameboard[7] == O:
        gameboard[4] = O
        return 5
    elif gameboard[1] == dash and gameboard[4] == O and gameboard[7] == O:
        gameboard[1] = O
        return 2
    elif gameboard[2] == O and gameboard[5] == O and gameboard[8] == dash:
        gameboard[8] = O
        return 9
    elif gameboard[2] == O and gameboard[5] == dash and gameboard[8] == O:
        gameboard[5] = O
        return 6
    elif gameboard[2] == dash and gameboard[5] == O and gameboard[8] == O:
        gameboard[2] = O
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(reiheLogicPlacingO())
       
     


def diagonalLogicPlacingO():
    if gameboard[0] == O and gameboard[4] == O and gameboard[8] == dash:
        gameboard[8] = O
        return 9
    elif gameboard[0] == O and gameboard[4] == dash and gameboard[8] == O:
        gameboard[4] = O
        return 5
    elif gameboard[2] == dash and gameboard[4] == O and gameboard[6] == O:
        gameboard[0] = O
        return 1
    elif gameboard[2] == O and gameboard[4] == O and gameboard[6] == dash:
        gameboard[6] = O
        return 7
    elif gameboard[2] == O and gameboard[4] == dash and gameboard[6] == O:
        gameboard[4] = O
        return 5
    elif gameboard[2] == dash and gameboard[4] == O and gameboard[6] == O:
        gameboard[2] = O
        return 3
    print("Computer wählt...")
    time.sleep(1)
    print(diagonalLogicPlacingO())



def logicPlacingO():
    zeileLogicPlacingO()
    reiheLogicPlacingO()
    diagonalLogicPlacingO()


def logicPlacingX():
    zeileLogicPlacingX()
    reiheLogicPlacingX()
    diagonalLogicPlacingX()


# -----------------------------------------------------Computerswinlogic------------------------------------------------------------------

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
    global tie
    if gameboard[0] != dash and gameboard[1] != dash and gameboard[2] != dash and gameboard[3] != dash and gameboard[4] != dash and gameboard[5] != dash and gameboard[6] != dash and gameboard[7] != dash and gameboard[8] != dash and winner == False:
        tie = True


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
            if winner == True or tie == True:
                winnerAnnouncement()
                break
            computerRundeO()
            winnerCheck()
            if winner == True or tie == True:
                winnerAnnouncement()
                break
    elif player1Char == O or player1Char == o:
        while winner == False:
            spielerRundeO()
            winnerCheck()
            if winner == True or tie == True:
                winnerAnnouncement()
                break
            computerRundeX()
            winnerCheck()
            if winner == True or tie == True:
                winnerAnnouncement()
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
    endgame = False
    choseChar()
    playGame()
    while endgame == False:
        if endgame == True:
            break
        restart = input("Möchtest du wiederholen?(Ja/Nein):")
        while restart != "Ja" or restart != "ja" or restart == "Nein" or restart == "nein":
            if restart == "Ja" or restart == "ja":
                resetGame()
                playGame()
                break
            elif restart == "Nein" or restart == "nein":
                endgame = True
                print("Das Spiel ist vorbei.")
                break
            else:
                restart = input("Ja/Nein?:")





startGame()
    
    








