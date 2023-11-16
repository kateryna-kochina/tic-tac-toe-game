import unittest
from app.game_utils import print_board, is_winner, is_full_board


class TicTacToeTest(unittest.TestCase):
    def test_print_board(self):
        # Check that the function doesn't throw any exceptions
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        self.assertIsNone(print_board(board))

    def test_is_winner(self):
        # For test cases where there is a winner
        winner_board_1 = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', 'O']]
        winner_board_2 = [['O', ' ', 'X'], ['O', ' ', 'X'], ['O', 'X', ' ']]
        winner_board_3 = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]

        # For test cases where there is no winner
        no_winner_board_1 = [['X', 'O', ' '], ['O', 'X', ' '], ['X', ' ', 'O']]
        no_winner_board_2 = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', 'O', ' ']]

        self.assertTrue(is_winner(winner_board_1))
        self.assertTrue(is_winner(winner_board_2))
        self.assertTrue(is_winner(winner_board_3))
        self.assertFalse(is_winner(no_winner_board_1))
        self.assertFalse(is_winner(no_winner_board_2))

    def test_is_full_board(self):
        full_board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        not_full_board = [['X', 'O', ' '], ['O', ' ', 'X'], ['X', 'O', 'X']]

        self.assertTrue(is_full_board(full_board))
        self.assertFalse(is_full_board(not_full_board))
