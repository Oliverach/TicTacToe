# TicTacToe

## Dokumentation

Mein erstes Programmierprojekt war ebenfalls Tic-Tac-Toe gewesen, nur war es in Python geschrieben. Daher wusste ich bereits, wie das Projekt ungefähr strukturiert werden soll. Über das Design musste ich nicht viel Gedanken machen, denn es sollte eine Konsole Applikation werden. Daher gab es sowieso nicht so viel Spielraum dafür. Ich habe die Funktionalität des Spiels festgelegt und begann mit Programmieren. Die Darstellung und die Aktualisierung des Brettes sowie die Spieler Aktionen konnte ich ohne Problem anfertigen. Mühe hatte ich erst dann, als ich mit der Logik des Gewinnens begonnen habe. Jedoch habe ich online gute Inspirationen gefunden und konnte damit weiterarbeiten. Nachdem ich das Multiplayer fertig programmiert habe, entschied ich Singleplayer noch zu implementieren. Dafür benötigte ich aber nicht zu lange.

## Testing

[Getestet](https://github.com/Oliverach/TicTacToe/blob/main/src/test/java/GameTest.java) habe ich die Logik des Gewinnens, indem ich ein Brett mit bestimmtem Pattern übergebe. Einmal stehen 3 Zeichen in einer Reihe damit der Spieler gewinnt und einmal nur 2, damit das Spiel weiter geht.
Da es in diesem Spiel oft zum Gleichstand kommt habe ich das auch getestet. 

(Klassendiagramm, Sequenzdiagramm, Use Case Diagramm siehe unten)

## Class Diagram

![Class Diagram](/doc/cd.jpg)

## Sequence Diagram

![Sequence Diagram](/doc/sd.png)

## Usecases

![Usecases](/doc/usecase.jpg)
