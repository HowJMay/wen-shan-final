from random import randrange

# the board status at beginning
board = """
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
"""

# to check who wins the game
def check_winner(board, sign):
    index_of_free_cell = list_of_free_cells(board)
    if index_of_free_cell == {}:
        print("The game ends with a tie !!")
        return True

    # The following is the index of the cell in the board_list string.
    # At the following index is the character of the sign
    #  57,  65,  73, 
    #  161, 169, 177, 
    #  265, 273, 281,
    
    board_list = convert_board_to_list(board)
    
    if (board_list[57] == sign and board_list[65] == sign and board_list[73] == sign):
        return print_result(sign)
    elif (board_list[161] == sign and board_list[169] == sign and board_list[177] == sign):
        return print_result(sign)
    elif (board_list[265] == sign and board_list[273] == sign and board_list[281] == sign):
        return print_result(sign)
    elif (board_list[57] == sign and board_list[161] == sign and board_list[265] == sign):
        return print_result(sign)
    elif (board_list[65] == sign and board_list[169] == sign and board_list[273] == sign):
        return print_result(sign)
    elif (board_list[73] == sign and board_list[177] == sign and board_list[281] == sign):
        return print_result(sign)
    elif (board_list[57] == sign and board_list[169] == sign and board_list[281] == sign):
        return print_result(sign)
    elif (board_list[73] == sign and board_list[169] == sign and board_list[265] == sign):
        return print_result(sign)
    
    return False


def print_result(sign):
    if sign == 'X':
        print("You lose the game! Shame on you!!")
    else:
        print("You won! I am just a dummy computer =^=!")
    return True

# The move that user enter would be marked as 'O'
# If character except '1-9' is entered, then user can enter 'q' again to quit the games
def enter_user_move(board):
    board_list = convert_board_to_list(board)
    user_move = input("Enter your move by index: ")
    index_of_free_cell = list_of_free_cells(board)
    
    while (user_move not in index_of_free_cell.keys()):
        user_move = input("Enter your move again or enter 'q' to exit: ")
        if (user_move == 'q'):
            return 'Exited!'
        
    board_list[index_of_free_cell[user_move]] = 'O'
    new_board = ''.join(board_list)
    print_board(new_board)
    
    return new_board

# computer AI enter its move with 'X'
def computer_move(board):
    board_list = convert_board_to_list(board)
    index_of_free_cell = list_of_free_cells(board)
    
    while(True):
        computer_move = str(randrange(1,10))
        if computer_move in index_of_free_cell.keys():
            board_list[index_of_free_cell[computer_move]] = 'X'
            new_board = ''.join(board_list)
            break
    print_board(new_board)
    
    return new_board

# convert board string to list
def convert_board_to_list(board):
    board_list = []
    for sign in board:
        board_list.append(sign)
    return board_list

# make a dict that stores numbers and their indexes
def list_of_free_cells(board):
    board_list = convert_board_to_list(board)   
    number_list = '12346789'
    index_of_free_cell = {}
    
    for i in number_list:
        if i in board_list:
            index_of_free_cell.update({i:board_list.index(i)})
            
    return index_of_free_cell

def print_board(board):
    print(board)


###################################################
######## The main program starts from here ########
###################################################
print_board(board)


while ((check_winner(board, 'X')) == False):
    board = enter_user_move(board)
    if board == 'Exited!':
        print(board)
        break
    elif check_winner(board, 'O') == True:
        break
    board = computer_move(board)