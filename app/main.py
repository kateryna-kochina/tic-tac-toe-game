from tic_tac_toe_game import (get_player_input, is_full_board,
                              is_winner, print_board, switch_player,
                              update_board)

game_on = True
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

while game_on:
    print_board(board)

    # Get and validate player input
    row, column = get_player_input(board, current_player)

    # Update the board with the current player's symbol
    if update_board(board, row, column, current_player):

        # Check if the current player is a winner
        if is_winner(board):
            print_board(board)
            print(f'{current_player} is a winner!')
            game_on = False

        # Check if the board is full, resulting in a tie
        elif is_full_board(board):
            print_board(board)
            print(f'It\'s a tie!')
            game_on = False

        # Switch to the other player for the next turn
        current_player = switch_player(current_player)
