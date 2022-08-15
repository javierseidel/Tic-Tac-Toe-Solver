"""
Implimentation of the minimax algorithm in a game of tic-tac-toe
Author: Javier Seidel
"""

# we initialize a board as a list that is filled with the "-" symbol to represent a blank spot
# we have a player and opponent variable as X and O, and a gameState to act as the boolean that allows the game function to loop
from cmath import inf


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
player = "X"
opponent = "O"
gameState = True

# print board function, which gives the player a visual representation of the tic-tac-toe game
def printBoard():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")

# validMove function, which confirms that the input given by the player and computer are valid. If the spot that the user is trying to fill in has already been filled, it will ask them to choose a new position
def validMove(input):
    if board[input] == "-":
        return input
    else:
        print("Invalid input, position is already taken, try again")
        return False

# validRange function, makes sure that the option being passed into the game is within the range of the board. ie if someone types 11, it will ask them to try a different input
def validRange(input):
    if input > 0 and input < 10:
        return input
    else:
        print("Invalid input, input out of range, try again")
        return False

# playerInput function takes the input from the player, and verifies that they are valid and within the acceptable range, then updates the board with the new information
def playerInput():
    print("Please choose a space on the board to put your X")
    choice = int(input()) - 1
    if validRange(choice) and validMove(choice):
        board[choice] = "X"
    else:
        printBoard()
        playerInput()

# computerInput function takes the computers input using the minimax algorithm, and updates the board with move made by the computer.
# 
def computerInput():
    bestScore = -inf
    choice = 0
    for key in range(9):
        if (board[key] == "-"):
            board[key] = "O"
            score = minimax(board, 0, -inf, inf, False)
            board[key] = '-'
            if (score > bestScore):
                bestScore = score
                choice = key
                
    board[choice] = "O"
    return

# minimax algorithm implimentation with ab pruning
def minimax(board, depth, alpha, beta, isMaximizing):
    if (checkWhichPlayerWon(opponent)):
        return 1
    elif (checkWhichPlayerWon(player)):
        return -1

    if (isMaximizing):
        bestScore = -inf
        for key in range(9):
            if (board[key] == '-'):
                board[key] = opponent
                score = minimax(board, depth -1, alpha, beta, False)
                board[key] = '-'
                bestScore = max(bestScore, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return bestScore

    else:
        minScore = inf
        for key in range(9):
            if (board[key] == '-'):
                board[key] = player
                score = minimax(board, depth - 1, alpha, beta, True)
                board[key] = '-'
                minScore = min(minScore, score)
                beta = min(beta, score)
        return minScore

# checkWhichMarkWon checks which player won, and returns either true or false based on who is being checked. 
# ie, if you are checking to see if the computer won, you pass in "opponent" to the function, and the function returns true
def checkWhichPlayerWon(sign):
    if board[0] == board[1] == board[2] == sign:
        return True
    elif board[3] == board[4] == board[5] == sign:
        return True
    elif (board[6] == board[7] == board[8] == sign):
        return True
    elif (board[0] == board[3] == board[6] == sign):
        return True
    elif (board[1] == board[4] == board[7] == sign):
        return True
    elif (board[2] == board[5] == board[8] == sign):
        return True
    elif (board[0] == board[4] == board[8] == sign):
        return True
    elif (board[6] == board[4] == board[2] == sign):
        return True
    else:
        return False

# checkWin checks to see if there is a winner. If there is, it will print to the screen which symbol won, as well as update the gameState to false to stop the game from looping
def checkWin():
    global gameState
    if board[0] == board[1] == board[2] != "-":
        print(str(board[0]) + " wins the game!")
        gameState = False
    elif board[3] == board[4] == board[5] != "-":
        print(str(board[3]) + " wins the game!")
        gameState = False
    elif board[6] == board[7] == board[8] != "-":
        print(str(board[6]) + " wins the game!")
        gameState = False
    elif board[0] == board[3] == board[6] != "-":
        print(str(board[0]) + " wins the game!")
        gameState = False
    elif board[1] == board[4] == board[7] != "-":
        print(str(board[1]) + " wins the game!")
        gameState = False
    elif board[2] == board[5] == board[8] != "-":
        print(str(board[2]) + " wins the game!")
        gameState = False  
    elif board[0] == board[4] == board[8] != "-":
        print(str(board[0]) + " wins the game!")
        gameState = False
    elif board[6] == board[4] == board[2] != "-":
        print(str(board[6]) + " wins the game!")
        gameState = False

# checkDraw checks the game to see if there has been a draw. If so, it ends the game
def checkDraw():
    global gameState
    for key in range(9):
        if board[key] == "-":
            return
        
    if checkWhichPlayerWon(opponent) == False and checkWhichPlayerWon(player) == False:
        print("DRAW!")
        gameState = False

# checkGameState checks to see if there has been a winner, or if there has been a draw, and ends the game if either is true
def checkGameState():
    checkWin()
    checkDraw()

# startGame is the game loop, which goes until one of our functions updates gameState to False to stop the game loop
def startGame():
    while gameState == True:
        computerInput()
        printBoard()
        checkGameState()
        if gameState == False:
            break
        playerInput()
        checkGameState()

# here is where we initialize the game
startGame()