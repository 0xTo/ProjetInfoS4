def solve(board):
    # Find an empty cell in the board (value = 0)
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved successfully

    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if check_valid_move(board, row, col, num):
            # If the move is valid, place the number in the cell
            board.grid[row][col].changeValue(num)

            # Recursively try to solve the board
            if solve(board):
                return True  # Puzzle solved successfully

            # If placing the number leads to an invalid solution, backtrack
            board.grid[row][col].changeValue(0)

    # No valid number could be placed in the empty cell
    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board.grid[i][j].value == 0:
                return (i, j)  # Return row and column of the empty cell
    return None  # If no empty cell is found, return None


def check_valid_move(board, row, col, num):
    # Check if the number is not already in the same row or column
    for i in range(9):
        if board.grid[row][i].value == num or board.grid[i][col].value == num:
            return False

    # Check if the number is not already in the same 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board.grid[i + start_row][j + start_col].value == num:
                return False

    return True  # The move is valid
