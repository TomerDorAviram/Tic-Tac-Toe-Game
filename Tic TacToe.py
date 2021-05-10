import random
import time


def boardGame():
    print("\n")
    print("\t___________________")
    print("\t|     |     |     |")
    print("\t|  1  |  2  |  3  |")
    print("\t|_____|_____|_____|")
    print("\t|     |     |     |")
    print("\t|  4  |  5  |  6  |")
    print("\t|_____|_____|_____|")
    print("\t|     |     |     |")
    print("\t|  7  |  8  |  9  |")
    print("\t|     |     |     |")
    print("\t___________________")
    return


def boardGame1(values):
    print("\n")
    print("\t___________________")
    print("\t|     |     |     |")
    print("\t|  {}  |  {}  |  {}  |".format(values[1], values[2], values[3]))
    print("\t|_____|_____|_____|")

    print("\t|     |     |     |")
    print("\t|  {}  |  {}  |  {}  |".format(values[4], values[5], values[6]))
    print("\t|_____|_____|_____|")

    print("\t|     |     |     |")
    print("\t|  {}  |  {}  |  {}  |".format(values[7], values[8], values[9]))
    print("\t|     |     |     |")
    print("\t___________________")


GameOpener = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

global PlayerNum1
global PlayerNum2
global MyRandom1
global MyRandom2


def randomPlayer():
    myRandom = random.randint(0, 1)
    global PlayerNum1
    global PlayerNum2
    global MyRandom1
    global MyRandom2
    PlayerNum1 = str(input("Name of Player1:"))
    PlayerNum2 = str(input("Name of Player2:"))
    while True:
        if PlayerNum1 == PlayerNum2:
            print("name already taken please choose another one:")
            PlayerNum2 = str(input("Name of Player2:"))
        else:
            break
    print("\n")
    time.sleep(0.5)
    print("Who Will Start?...\n")
    time.sleep(0.5)
    if myRandom == 0:
        MyRandom1 = PlayerNum1
        MyRandom2 = PlayerNum2
        print(PlayerNum1 + " " + "starts first with an X!")
        time.sleep(0.5)
    else:
        print(PlayerNum2 + " " + "starts first with an X!\n ")
        time.sleep(1)
    if myRandom == 1:
        MyRandom1 = PlayerNum2
        MyRandom2 = PlayerNum1
        print(PlayerNum1 + " " + "starts second with an O!")
        time.sleep(0.5)
    else:
        print(PlayerNum2 + " " + "starts second with an O!\n ")
        time.sleep(1)
    boardGame()
    print("")
    Player1()


def Player1():
    print("")
    while True:
        try:
            UserInput1 = int(input("Please write the number you want to place your X:"))
            setPlayerMove(GameOpener, 1, UserInput1)
            boardGame1(GameOpener)
        except (ValueError, IndexError):
            print("")
            print("Option incorrect, try again!\n")
            continue
        Player2()


def Player2():
    print("")
    print("It's", "" + MyRandom2 + "'s", "turn!")
    while True:

        try:
            UserInput2 = int(input("Please write the number you want to place your O:"))
            if GameOpener[UserInput2] == "X" or GameOpener[UserInput2] == "O":
                print("Can't do that")
                continue
            else:
                setPlayerMove(GameOpener, 2, UserInput2)
                if GameOpener[1] == "O" and GameOpener[2] == "O" and GameOpener[3] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[4] == "O" and GameOpener[5] == "O" and GameOpener[6] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[7] == "O" and GameOpener[8] == "O" and GameOpener[9] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[1] == "O" and GameOpener[4] == "O" and GameOpener[7] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[3] == "O" and GameOpener[6] == "O" and GameOpener[9] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[1] == "O" and GameOpener[5] == "O" and GameOpener[9] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[1] == "O" and GameOpener[5] == "O" and GameOpener[9] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[3] == "O" and GameOpener[5] == "O" and GameOpener[7] == "O":
                    setPlayerMove(GameOpener, 1, UserInput2)
                    boardGame1(GameOpener)
                    Down2()
                boardGame1(GameOpener)
                Player11()
        except (ValueError, IndexError):
            print("")
            print("Option incorrect, try again!\n")
            continue


def Down():
    print(MyRandom2 + "", "Wins!")
    time.sleep(0.5)
    print("bye bye")
    del GameOpener
    Game()


def Clear():
    GameOpener[1] = " "
    GameOpener[2] = " "
    GameOpener[3] = " "
    GameOpener[4] = " "
    GameOpener[5] = " "
    GameOpener[6] = " "
    GameOpener[7] = " "
    GameOpener[8] = " "
    GameOpener[9] = " "


def Down2():
    print(MyRandom1 + "", "Wins!")
    time.sleep(0.5)
    print("")
    print("bye bye!")
    Clear()
    Game()


def Draw():
    print("It's A Draw")
    time.sleep(0.5)
    print("")
    print("bye bye!")
    Clear()
    Game()


def Player11():
    print("")
    print("It's'", "" + MyRandom1 + "'s", "turn!")
    while True:

        try:
            UserInput1 = int(input("Please write the number you want to place your X:"))
            if GameOpener[UserInput1] == "O" or GameOpener[UserInput1] == "X":
                print("Can't do that")
                continue
            else:
                setPlayerMove(GameOpener, 1, UserInput1)
                if GameOpener[1] == "X" and GameOpener[2] == "X" and GameOpener[3] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[4] == "X" and GameOpener[5] == "X" and GameOpener[6] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[7] == "X" and GameOpener[8] == "X" and GameOpener[9] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[2] == "X" and GameOpener[5] == "X" and GameOpener[8] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[1] == "X" and GameOpener[4] == "X" and GameOpener[7] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[3] == "X" and GameOpener[6] == "X" and GameOpener[9] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[1] == "X" and GameOpener[5] == "X" and GameOpener[9] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()
                if GameOpener[3] == "X" and GameOpener[5] == "X" and GameOpener[7] == "X":
                    setPlayerMove(GameOpener, 1, UserInput1)
                    boardGame1(GameOpener)
                    Down2()

                if GameOpener[1] != " " and GameOpener[2] != " " and GameOpener[3] != " " \
                        and GameOpener[4] != " " and GameOpener[5] != " " \
                        and GameOpener[6] != " " and GameOpener[7] != " " \
                        and GameOpener[8] != " " and GameOpener[9] != " ":
                    Draw()
                boardGame1(GameOpener)
                Player2()
        except (ValueError, IndexError):
            print("")
            print("Option incorrect, try again!\n")
            continue


def Menu():
    print("Welcome to Tic Tac Toe!!\n")
    print("1)New Game:")
    print("2)Exit:")
    print("Enter Option:")


def setPlayerMove(board, player, a):
    if player == 1:
        board[a] = "X"
    elif player == 2:
        board[a] = "O"


def Game():

    while True:

        boardGame()
        Menu()
        try:
            userOption = int(input())

        except ValueError:
            print("")
            print("Option incorrect, try again!\n")
            continue

        if userOption == 1:
            randomPlayer()

        if userOption == 2:
            print("bye bye")
            break

        if userOption > 2:
            print("Option incorrect, try again!\n")
            continue

        if userOption == "":
            print("Option incorrect, try again!\n")
            continue


Game()
