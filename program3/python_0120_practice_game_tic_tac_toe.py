'''
Requirement:
Implement Game: tic-tac-toe

Key Logic:
If we analysis the process of the game, we know the game is composed of the following steps.
'''

'''
step 1) Prepare the data.
Create an empty chess board.
tic-tac-toe game chess board is composed of 9 space - 3 * 3
So we can use a nested list to represent the chess board.
'''

chess_board = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

'''
Step 2) Print chess board to the console.
I define a function to print the chessboard nicely.
And this function will be called many times.
'''

def print_chessboard(chess_board):
    '''
    This function prints the chess board.
    :param chess_board:
    :return: nothing
    '''


    for row in chess_board:

        # Solution 1)
        # for place in row:
        #     print(place, end = ' ')
        # print('') # python will automaticaly add a '\n' character for you

        # Solution 2)
        print(*row) # equals to print('_','_','_')



# code for a while, test for a while
# print_chessboard(chess_board)


'''
Step 3) Player places a piece.
    We define a new function. The function will accpet 2 parameters - chess_board, piece (being either 'X' or 'O')
    def place_piece(chess_board, piece):
        pass

And inside the function body, it should do the following steps.


Step 3.1) we ask player to input the coordinates x and y.
    We define a new function, we let the function return a list, we call it coordinates, which contains coordinates x and y
    def get_user_coordinates():
        pass


Step 3.2) we check the coordinates x and y, with the below conditions:
    Condition check 1) x and y should be in range [0, 2]. 
    Condition check 2) chess_board[x][y] should be '_', meaning it is not taken by player 1 or 2.
    If any condition fail, then we need to repeat step 3.1 and step 3.2
    
    We define a new function, we let the function return a bool value, 
    true -> valid coordinates
    false -> invalid coordinates
    def check_coordinates(chess_board, coordinates):
        pass
    
So, step 3.1 and step 3.2 should be put inside a loop.    


Step 3.3) update the chess_board, very simple
    chess_board[x][y] = piece
    
    
Step 3.4) print chessboard, very simple, we call function: print_chessboard(chess_board)


Step 3.5) Check win
     For the new coordinates which the player has placed the piece on, we check whether he wins or not.
     if he wins: program exit.
     if he doesn't win: does nothing.
     we define a new function:
     def check_win(chess_board, coordinates):
        pass

'''

# Step 3.1) we ask player to input the coordinates x and y.
def get_user_coordinates():
    '''
    We ask user to input the coordinates.

    :return: a list which contains 2 int, being x and y.
    '''

    input_value = input("New coordinates:")
    # we hope user can give me a value like this: 1 2
    x_y_list = input_value.split(" ") # if user inputs '1 2', x_y_list will become list ['1', '2']
    x = int(x_y_list[0])
    y = int(x_y_list[1])
    return [x, y]



# Step 3.2) we check the coordinates x and y
def check_coordinates(chess_board, coordinates):
    '''
    Check whether the coordinates is valid for the chess_board or not

    :param chess_board: the chess_board which 2 players are playing on
    :param coordinates: is a list, which contains 2 int x and y
    :return: True if both x and y are within range[0,2] and chess_board[x][y] has not been taken by any player
    '''
    # Condition check no.1
    x = coordinates[0]
    y = coordinates[1]

    if x < 0 or x > 2: # invalid x
        print(f"Coordinates x is wrong: {x}. Valid value is in range[0,2]. Please try again.")
        return False

    if y < 0 or y > 2: # invalid y
        print(f"Coordinates y is wrong: {y}. Valid value is in range[0,2]. Please try again.")
        return False

    #Condition check no.2
    if chess_board[x][y] != '_':
        print(f"chess board [{x}][{y}] has value {chess_board[x][y]}. Please try again.")
        return False

    return True



# Step 3.5) Check win
# How to check win?
# I just need to check the row / the column / the 2 cross lines (if the coordinates is on the cross line), that's it!

def check_win(chess_board, coordinates):
    '''
    This function checks whether the coordinates will cause a win in the chess board
    if somebody wins, the program exits.

    :param chess_board:
    :param coordinates:
    :return: nothing.
    '''

    x = coordinates[0]
    y = coordinates[1]

    # row win
    if chess_board[x][0] == chess_board[x][1] and chess_board[x][0] == chess_board[x][2]:
        print("Win!")
        exit()

    # column win
    if chess_board[0][y] == chess_board[1][y] and chess_board[0][y] == chess_board[2][y]:
        print("Win!")
        exit()

    # cross line win
    if x == 0 and y == 0 or x == 1 and y == 1 or x == 2 and y == 2:
        if chess_board[0][0] == chess_board[1][1] and chess_board[0][0] == chess_board[2][2]:
            print("Win!")
            exit()

    if x == 0 and y == 2 or x == 1 and y == 1 or x == 2 and y == 0:
        if chess_board[2][0] == chess_board[1][1] and chess_board[2][0] == chess_board[0][2]:
            print("Win!")
            exit()




# Step 3) Player places a piece.

def place_piece(chess_board, piece):
    '''
    This function will place a piece on the chess board

    :param chess_board:
    :param piece: it can either 'X' or 'O'
    :return: nothing
    '''

    # Because sometimes player can give us wrong coordinates, so we need to loop until he gives us a correct one.
    while True:

        # Step 3.1) we ask player to input the coordinate x and y
        coordinates = get_user_coordinates()

        # Step 3.2) we check the coordinates x and y
        is_valid_coordinates = check_coordinates(chess_board, coordinates)

        if is_valid_coordinates:
            break
        else:
            print("Please try again.")

    x = coordinates[0]
    y = coordinates[1]

    # Step 3.3) update the chess board
    chess_board[x][y] = piece

    # Step 3.4) print chess board
    print_chessboard(chess_board)

    # Step 3.5) check wins
    check_win(chess_board, coordinates)

    print('-' * 20)


# code for a while, test for a while
# place_piece(chess_board, 'X')
# place_piece(chess_board, 'O')


# ------------------------------
# MAIN PROGRAM BEGIN
# ------------------------------

welcome_msg = '''Tic Tac Toe Game Starts
---------------------------------------------
'''

print(welcome_msg)

print_chessboard(chess_board)

# Define 2 players

player1 = ["PLAYER 1", 'O']
player2 = ["PLAYER 2", 'X']
players = [player1, player2]

# So I loop 9 times to call function - place_piece

for turn in range(9):
    player = players[turn % 2]
    print(f"{player[0]}'s turn:")
    place_piece(chess_board, player[1])

print("Draw!")



