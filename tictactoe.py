import random

board = ["-","-","-","-","-","-","-","-","-",]
currentPlayer = "X"
winner = None
gameRunning = True
def printBoard(board):
    print("\n\nEMPTY TIC-TAC-TOE BOARD\n")
    print(board[0] + " | " + board[1] + " | " +  board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " +  board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " +  board[8])
#printBoard(board)
#take input to place ur choice
def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Player is already in the spot")

#check if rows are same
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[3]
        return True

#check if columns are same
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#check if diagonals are same
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]

#check is tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("IT IS A TIE")        
        gameRunning = False

def checkWin(board):
    global gameRunning
    global gameRunning
    if checkColumn(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False
    #if checkDiagonal(board) or checkRow(board) or checkColumn(board):
     #   print(f"THE WINNER IS {winner}")

#one chace to U and the other one to computer
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#asigning randomly in empty gaps
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)
    #switchPlayer(board)
