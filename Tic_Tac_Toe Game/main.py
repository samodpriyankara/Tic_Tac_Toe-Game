import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentPlayer = "X"
winner = None
gameRunning = "True"


# Print the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Take a player input

def playerInput(board):
    inp = int(input("Enter a number 1 - 9 : "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
        board[inp - 1] = currentPlayer
    else:
        print("Ooops player is already in that spot !")


# Check win conditions

def checkHorisontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[5] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "_":
        winner = board[7]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[6] != "_":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "_":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "_":
        winner = board[5]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "_":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "_":
        winner = board[4]
        return True


# Check the win

def checkWin():
    global gameRunning
    if checkvertical(board) or checkdiagonal(board) or checkhorisontal(board):
        print(f"Congratulations !...The winner is {winner}")
        gameRunning = False


# Change the current player

def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# Auto play partner

def autoPlay(board):
    global currentPlayer
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            changeplayer()


# Check tie

def checktie(board):
    global gameRunning
    if "_" not in board:
        print("Game is tie !")
        gameRunning = False


# Run thw game

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checktie(board)
    if gameRunning == False:
        break
    changeplayer()
    autoplay(board)
    checkWin()
    checktie(board)
    if gameRunning == False:
        break
