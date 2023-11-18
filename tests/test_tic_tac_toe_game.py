import unittest
from unittest.mock import patch

from app.tic_tac_toe_game import (get_player_input, is_full_board, is_valid_input, is_winner,
                                  print_board, switch_player, update_board)


class TestTicTacToeFunctions(unittest.TestCase):

    def test_print_board(self):
        # Check that the function doesn't throw any exceptions
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        self.assertIsNone(print_board(board))

    @patch('builtins.input', side_effect=['2', '1'])
    def test_get_player_input_valid_input(self, mock_input):
        # Check player input
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        current_player = 'X'
        result = get_player_input(board, current_player)
        # Assuming the user enters '2' and '1'
        self.assertEqual(result, (1, 0))

    def test_is_valid_input_valid_input(self):
        # Test a valid input scenario
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(is_valid_input(board, 1, 1))

    def test_is_valid_input_invalid_row_or_column(self):
        # Test invalid row or column values
        board = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        self.assertFalse(is_valid_input(board, 0, 2))
        self.assertFalse(is_valid_input(board, 4, 2))
        self.assertFalse(is_valid_input(board, 2, 0))
        self.assertFalse(is_valid_input(board, 2, 4))

    def test_is_valid_input_invalid_cell_taken(self):
        # Test invalid input where the cell is already taken
        board = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        self.assertFalse(is_valid_input(board, 1, 1))

    def test_is_valid_input_invalid_input_not_integer(self):
        # Test invalid input where non-integer values are provided
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertFalse(is_valid_input(board, 'a', 2))

    def test_invalid_is_valid_input_input_nonexistent_column(self):
        # Test invalid input where a nonexistent column is provided
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertFalse(is_valid_input(board, 2, 'b'))

    def test_update_board_valid(self):
        # Test valid update
        board = [['X', 'O', ' '], ['O', 'X', 'O'], ['X', ' ', 'X']]
        row, column = 2, 1
        current_player = 'X'
        self.assertTrue(update_board(board, row, column, current_player))
        self.assertEqual(board[2][1], 'X')

    def test_update_board_invalid(self):
        # Test invalid update
        board = [['X', 'O', ' '], ['O', 'X', 'O'], ['X', 'O', 'X']]
        row, column = 2, 1
        current_player = 'X'
        self.assertFalse(update_board(board, row, column, current_player))
        # Ensure the board is unchanged
        self.assertEqual(board[2][1], 'O')

    def test_is_winner(self):
        # For test cases where there is a winner
        winner_board_1 = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', 'O']]
        winner_board_2 = [['O', ' ', 'X'], ['O', ' ', 'X'], ['O', 'X', ' ']]
        winner_board_3 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]

        self.assertTrue(is_winner(winner_board_1))
        self.assertTrue(is_winner(winner_board_2))
        self.assertTrue(is_winner(winner_board_3))

    def test_is_not_winner(self):
        # For test cases where there is no winner
        no_winner_board_1 = [['X', 'O', ' '], ['O', 'X', ' '], ['X', ' ', 'O']]
        no_winner_board_2 = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', 'O', ' ']]

        self.assertFalse(is_winner(no_winner_board_1))
        self.assertFalse(is_winner(no_winner_board_2))

    def test_is_full_board(self):
        # Test a full board
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        self.assertTrue(is_full_board(board))

    def test_is_not_full_board(self):
        # Test a non-full board
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', ' ']]
        self.assertFalse(is_full_board(board))

    def test_switch_player(self):
        # Test switching players
        self.assertEqual(switch_player('X'), 'O')
        self.assertEqual(switch_player('O'), 'X')


if __name__ == '__main__':
    unittest.main()
