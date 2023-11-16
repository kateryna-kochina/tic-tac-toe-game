def print_board(board):
    '''
    Print the tic-tac-toe board.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.

    Returns:
    None
    '''
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i < len(board) - 1:
            print('---' * 3)


# Check a winner
def is_winner(board) -> bool:
    '''
    Check if there is a winner on the tic-tac-toe board.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.

    Returns:
    bool: True if there is a winner, False otherwise.
    '''
    # Check rows
    for row in board:
        # check if 1st cell in a row is not blank
        # and all following cells in a row equal the 1st cell
        if row[0] != ' ' and all(i == row[0] for i in row):
            return True

    # Check columns
    for col in range(3):
        ## Check if 1st cell in a column is not blank and all following cells in a column equal the 1st cell
        if board[0][col] != ' ' and all(board[row][col] == board[0][col] for row in range(3)):
            return True

    # Check two diagonals
    ## Check if 1st cell in 1st column is not blank and all following cells by diagonal equal the 1st cell
    if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(3)):
        return True

    ## Check if 1st cell in last column is not blank and all following cells by diagonal equal the 1st cell
    if board[0][2] != ' ' and all(board[i][2 - i] == board[0][2] for i in range(3)):
        return True

    return False


# Check a move is still possible
def is_full_board(board) -> bool:
    '''
    Check if the tic-tac-toe board is full, indicating that no more moves are possible.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.

    Returns:
    bool: True if the board is full, False otherwise.
    '''
    return all(cell != ' ' for row in board for cell in row)
