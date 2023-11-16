from game_utils import print_board, is_winner, is_full_board


game_on = True
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

while game_on:
    print_board(board)

    # Get player input
    row = int(
        input(f'Player {current_player}, please enter row number: 1, 2, or 3: ')) - 1
    column = int(
        input(f'Player {current_player}, please enter column number: 1, 2, or 3: ')) - 1

    if board[row][column] == ' ':

        # Update the board with the current player's symbol
        board[row][column] = current_player

        # Check if the current player is a winner
        if is_winner(board):
            print_board(board)
            print(f'{current_player} is a winner!')
            game_on = False

        # Check if the board is full, resulting in a tie
        if is_full_board(board):
            print_board(board)
            print(f'It\'s a tie!')
            game_on = False

        # Switch to the other player for the next turn
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    else:
        print('Cell is already taken, please select another one.')
