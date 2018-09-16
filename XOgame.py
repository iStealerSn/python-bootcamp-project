"""
---------------------------------------------------------------------------------------------------------------------
Welcome to Tic Tac Toe (revised code) project, made an attempt to concise the codebase and produce the same result.
Any suggestions or improvisations are welcome, please share these information on sj.nadar@live.com or in github (istealersn)
---------------------------------------------------------------------------------------------------------------------

----- -----  ----     -----  ----  ----     -----  ----  -----
  |     |    |          |    |  |  |          |    |  |  |
  |     |    |          |    |--|  |          |    |  |  |---
  |   __|__  |___       |    |  |  |___       |    |__|  |____


I have broken down the game into 8 STEPS for better understanding (beginners only)

"""

# All global imports should be defined at the beginning
import random

# STEP 1 - Setup the game board following the Numpad approach on the keyboard
def gameBoard_display(board):
    print('-----------------------------------------------')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('-----------------------------------------------')

# STEP 2 - Player selection setup, ask the player to choose a marker from X and O
def marker_selection():
    selection = ''

    while selection!= 'X' or 'O':
        selection = input('Please choose your marker from X or O: ').upper()
        if selection == 'X':
            return 'X','O'
        elif selection == 'O':
            return 'O','X'


# STEP 3 - Setup the function to place the marker on the board
def place_marker(board, marker, position):
    board[position] = marker


# STEP 4 - Setup the winCheck module that validates the final board following the rules of Tic Tac Toe game
def winCheck(board, mark):
    return board[1] == mark and board[2] == mark and board[3] == mark or \
    board[4] == mark and board[5] == mark and board[6] == mark or \
    board[7] == mark and board[8] == mark and board[9] == mark or \
    board[1] == mark and board[4] == mark and board[7] == mark or \
    board[2] == mark and board[5] == mark and board[8] == mark or \
    board[3] == mark and board[6] == mark and board[9] == mark or \
    board[7] == mark and board[5] == mark and board[3] == mark or \
    board[9] == mark and board[5] == mark and board[1] == mark


# STEP 5 - Function flip the coin in the air
def gameToss():
    return random.randint(1,2)

# STEP 6 - Setup a module to check if any of the position on the board is empty before wrapping the game
def gameBoardCheck_position(board, position):
    return board[position] == ' '

# STEP 7 - Validate the board to see if all positions are filled in and if not ask the player for their next position
def gameBoardCheck(board):
    for pos in range(1,10):
        if gameBoardCheck_position(board, pos):
            return False
    return True


# STEP 8 - Ask player for his next move
def posPlayer(board):
    position = 0

    while position not in range(1, 10) and not gameBoardCheck_position(board, position):
        try:
            position = int(input('Please enter a number between 1 to 9: '))
            break
        except:
            print('Please enter a valid number')
            continue

    return position


# STEP 9 - Replay module
def gameReplay():
    try:
        replay = input('Do you want to play again Y or N: ').lower()
        return replay == 'y' or replay.startswith('y')
    except:
        print('Please enter either Y or N')


#STEP 10 - Setup the gameplay here using all the above defined functions and modules
print('WELCOME TO TIC TAC TOE GAME - One of the best game ever invented or developed.\n'
      'This version of the game is coded by __ Stanley J Nadar (iStealerSn)')
print('\n')

while True:
    gameBoard = [' '] * 10  # Creates a list with ten strings as blank space

    player1, player2 = marker_selection() # X and O assigned to individual players
    print(f'Player1 has chosen the marker {player1} and Player2 gets the marker {player2}')

    toss = gameToss() # Game toss initiated and based on result its kicked off
    if toss == 1:
        print(f'Player 1 has won the toss and will go first with the marker {player1}')
    else:
        print(f'Player 2 has won the toss and will go first with the marker {player2}')

    # Final acknowledgement from the players

    gameOn = input('Are you ready to play Player' + str(toss) + ' , Enter Y or N: ').lower()
    if gameOn == 'y':
        gameOn = True
    else:
        gameOn = False

    while gameOn:
        if toss == 1:
            gameBoard_display(gameBoard)
            position = posPlayer(gameBoard)
            place_marker(gameBoard, player1, position)

            if winCheck(gameBoard, player1):
                gameBoard_display(gameBoard)
                print('----------------------------------------------------------')
                print(f'Congratulations! Player1 with {player1} hs WON the game')
                print('----------------------------------------------------------')
                gameOn = False
            else:
                if gameBoardCheck(gameBoard):
                    gameBoard_display(gameBoard)
                    print('--------------------')
                    print('The game is a DRAW')
                    print('--------------------')
                    break
                else:
                    toss = 2
        else:
            gameBoard_display(gameBoard)
            position = posPlayer(gameBoard)
            place_marker(gameBoard, player2, position)

            if winCheck(gameBoard, player2):
                gameBoard_display(gameBoard)
                print(f'Congratulations! Player1 with {player2} hs WON the game')
                gameOn = False
            else:
                if gameBoardCheck(gameBoard):
                    gameBoard_display(gameBoard)
                    print('The game is a DRAW')
                    break
                else:
                    toss = 1

    if not gameReplay():
        break