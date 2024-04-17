def solve(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if check_valid_move(board, row, col, num):
            board.grid[row][col].changeValue(num)

            if solve(board):
                return True

            board.grid[row][col].changeValue(0)

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board.grid[i][j].value == 0:
                return (i, j)
    return None

def check_valid_move(board, row, col, num):
    for i in range(9):
        if board.grid[row][i].value == num or board.grid[i][col].value == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board.grid[i + start_row][j + start_col].value == num:
                return False

    return True
