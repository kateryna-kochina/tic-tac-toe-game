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


def get_player_input(board, current_player):
    '''
    Get valid player input for the tic-tac-toe game.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.
    current_player (str): The symbol ('X' or 'O') of the current player.

    Returns:
    tuple: A tuple containing the selected row and column on the board.
    '''
    while True:
        try:
            row = int(
                input(f'Player {current_player}, please enter row number: 1, 2, or 3: ')) - 1
            column = int(
                input(f'Player {current_player}, please enter column number: 1, 2, or 3: ')) - 1

            # Validate the input
            if is_valid_input(board, row, column):
                return row, column

        except ValueError as e:
            print(f'Invalid input: {e}.')


def is_valid_input(board, row, column):
    '''
    Validate if the entered row and column values are within the valid range and
    if the selected cell is not already taken.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.
    row (int): The selected row.
    column (int): The selected column.

    Returns:
    bool: True if the input is valid, False otherwise.
    '''
    if not (0 <= row < 3 and 0 <= column < 3):
        print('Row and column values must be between 1 and 3.')
        return False

    if board[row][column] != ' ':
        print('Cell is already taken, please select another one.')
        return False

    return True


def update_board(board, row, column, current_player):
    '''
    Update the tic-tac-toe board with the player's move.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.
    row (int): The selected row (0-indexed) on the board.
    column (int): The selected column (0-indexed) on the board.
    current_player (str): The symbol ('X' or 'O') of the current player.

    Returns:
    bool: True if the update is successful, False if the cell is already taken.
    '''
    if board[row][column] == ' ':
        board[row][column] = current_player
        return True
    else:
        print('Cell is already taken, please select another one.')
        return False


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
        # Check if 1st cell in a column is not blank and all following cells in a column equal the 1st cell
        if board[0][col] != ' ' and all(board[row][col] == board[0][col] for row in range(3)):
            return True

    # Check two diagonals
    # Check if 1st cell in 1st column is not blank and all following cells by diagonal equal the 1st cell
    if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(3)):
        return True

    # Check if 1st cell in last column is not blank and all following cells by diagonal equal the 1st cell
    if board[0][2] != ' ' and all(board[i][2 - i] == board[0][2] for i in range(3)):
        return True

    return False


def is_full_board(board) -> bool:
    '''
    Check if the tic-tac-toe board is full, indicating that no more moves are possible.

    Parameters:
    board (list): The 3x3 tic-tac-toe board represented as a list of lists.

    Returns:
    bool: True if the board is full, False otherwise.
    '''
    return all(cell != ' ' for row in board for cell in row)


def switch_player(current_player):
    '''
    Switch the current player in the tic-tac-toe game.

    Parameters:
    current_player (str): The symbol ('X' or 'O') of the current player.

    Returns:
    str: The symbol of the other player ('O' if the current player is 'X', and vice versa).
    '''
    return 'O' if current_player == 'X' else 'X'
