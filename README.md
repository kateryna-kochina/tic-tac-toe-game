# Tic-Tac-Toe Game

This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns entering their moves until there is a winner or a tie.

## How to Play

Run the main.py file.
Players take turns entering their moves by specifying the row and column numbers (both ranging from 1 to 3).
The game continues until a player wins or the board is full, resulting in a tie.

## Game Mechanics

The game board is displayed after each move.
Players are prompted to enter their moves with input validation and error handling.
The program checks for a winner after each move and displays the result.
If the board is full and no winner is determined, the game ends in a tie.

## Code Structure

The main game logic is implemented in the main.py file. It uses functions from game_utils.py for printing the board, checking for a winner, and determining if the board is full.

## How to Run Tests

The unittest module is used to test the functions in game_utils.py. To run the tests, execute the following command:

`
python -m unittest discover -s tests -p 'test_*.py'
`

The tests cover the functionality of printing the board, checking for a winner, and determining if the board is full.

Feel free to explore and enjoy this simple yet classic game!