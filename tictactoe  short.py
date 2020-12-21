import random
import time


gameboard = [ 
    ["-", "-", "-"] ,
    ["-", "-", "-"] , 
    ["-", "-", "-"]
    ]


def showGameboard():
    for row in gameboard:
        output = ""
        for field in row:
            output += field + " | "
        print(output[0:len(output)-2])
    output = ""
    for i in range(1,10):
        output += str(i) + " | "
        if i%3 == 0:
            print(output[0:len(output)-2])
            output = ""



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
            LogicBlockingX()
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

    logicBlockingO()
    logicPlacingO()
    randomPlacing()

    showGameboard()
    
        
        



# -----------------------------------------------------Computers Turn------------------------------------------------------------------
def randomPlacing():
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





       
# def zeileLogicBlockingO(board):
#     marks = 0
#     player = ""
#     for i in range(3):
#         for j in range(3):
#             if i%3 == 2:
#                 marks = 0
#             if board[i] != dash:
#                 if player == "":
#                     player = board[i]
#                     marks += 1
#                 elif player == board[i]:
#                     marks += 1
#                 else
        



        





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
    
    








