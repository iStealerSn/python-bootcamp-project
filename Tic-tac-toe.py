# Below is the script for Tic Tac Toe game built using the walkthrough shared by Jose Portilla


def game_board(board): # This will display the game board
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')

def player_input(): # Player input and marker selection
    selection = ''

    while selection != 'X' or 'O':
        selection = input('Please chose your marker from X or O - ').upper()
        if selection == 'X':
            return ('X','O')
        elif selection == 'O':
            return ('O','X')


def place_marker(board, marker, position): # Helps to place the marker on the board
    board[position] = marker

def win_check(board, mark): # Validates the board to check who is the winner
    return (board[7] == mark and board[8] == mark and board[9] == mark) or \
    (board[4] == mark and board[5] == mark and board[6] == mark) or \
    (board[1] == mark and board[2] == mark and board[3] == mark) or \
    (board[7] == mark and board[5] == mark and board[3] == mark) or \
    (board[9] == mark and board[5] == mark and board[1] == mark) or \
    (board[8] == mark and board[5] == mark and board[2] == mark) or \
    (board[7] == mark and board[4] == mark and board[1] == mark)    


import random
""" In built function imported to choose between Player 1 and Player 2 randomly """

def choose_player(): # Returns a random value between 1 and 2
    return random.randint(1,2)

def space_check(board,position): # Checks if the position is empty
    return board[position] == ' '

def board_check(board):
    for char in range(1,10):
        if space_check(board,char):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board,position):
        try:
            position = int(input('Please select your position between 1 to 9 - '))
        except:
            print('Please enter numbers only')

    return position

def game_replay():
    replay = input('Do you want to play the game again "Yes" or "No" - ').lower().startswith('y')
    return replay == 'y'


print('Welcome to the game - TIC TAC TOE')

while True:
    
    gameboard = [' '] * 10
    
    player1, player2 = player_input()
    
    print(f'Player 1 has chosen the marker {player1}')
    print(f'Player 2 has chosen the marker {player2}')

    turn = choose_player()

    if turn == 1:
        print(f'Player 1 with his marker {player1}, will go first')
    else:
        print(f'Player 2 with his marker {player2}, will go first')

    game_on = input('Are you ready to play the game Player ' + str(turn) + '  ?, say "Yes" or "No" - ').lower()

    if game_on[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == 1:
            game_board(gameboard)
            
            position = player_choice(gameboard)

            place_marker(gameboard, player1, position)

            if win_check(gameboard,player1):
                game_board(gameboard)
                print('Congratulations! You have won the game')
                game_on = False
            else:
                if board_check(gameboard):
                    game_board(gameboard)
                    print('Draw game')
                    break
                else:
                    turn = 2
        
        else:
            game_board(gameboard)
            
            position = player_choice(gameboard)

            place_marker(gameboard, player2, position)

            if win_check(gameboard, player2):
                game_board(gameboard)
                print('Congratulations! You have won the game')
                game_on = False
            else:
                if board_check(gameboard):
                    game_board(gameboard)
                    print('Draw game')
                    break
                else:
                    turn = 1

    if not game_replay():
        break




    




