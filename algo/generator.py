import random

from algo.solver import solve
from utils.board import SudokuBoard


def generate(board, difficulté):

    # Solve the empty board
    solve(board)

    # Select 38 random cells to keep and put them in a list
    cells_to_keep = random.sample(range(81), 36//difficulté)

    # Reset values to 0 for cells not in cells_to_keep
    for i in range(9):
        for j in range(9):
            index = i * 9 + j
            if index not in cells_to_keep:
                board.grid[i][j].changeValue(0)

    # Randomly remove some cells until there's a unique solution
    for cell_index in cells_to_keep:
        row = cell_index // 9
        col = cell_index % 9

        # Backup the original value
        original_value = board.grid[row][col].value

        # Temporarily remove the value
        board.grid[row][col].changeValue(0)

        # Check if the board still has a unique solution
        unique_solution = has_unique_solution(board)

        if not unique_solution:
            # If removing the value makes the board unsolvable or has multiple solutions,
            # revert the cell to its original value
            board.grid[row][col].changeValue(original_value)


def has_unique_solution(board):
    # Clone the board to not affect the original
    cloned_board = clone_board(board)

    # Try to solve the cloned board
    solve(cloned_board)

    # Check if the cloned board has a unique solution
    return is_solution_unique(cloned_board, board)


# Create a new board and copy the values from the original board
def clone_board(board):
    cloned_board = SudokuBoard()
    for i in range(9):
        for j in range(9):
            cloned_board.grid[i][j].changeValue(board.grid[i][j].value)
    return cloned_board


def is_solution_unique(board1, board2):
    # Compare two boards to check if they are identical
    for i in range(9):
        for j in range(9):
            if board1.grid[i][j].value != board2.grid[i][j].value:
                return False
    return True
