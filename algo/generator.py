import random
import sys

from algo.solver import solve
from utils.board import SudokuBoard


def generate(board, initial_numbers):
    sys.setrecursionlimit(10000)
    generate_random_board(board)

    cells_to_keep = random.sample(range(81), initial_numbers)

    for i in range(9):
        for j in range(9):
            index = i * 9 + j
            if index not in cells_to_keep:
                board.grid[i][j].changeValue(0)

    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        for cell_index in cells_to_keep:
            row = cell_index // 9
            col = cell_index % 9

            original_value = board.grid[row][col].value
            board.grid[row][col].changeValue(0)

            unique_solution = has_unique_solution(board)

            if not unique_solution:
                board.grid[row][col].changeValue(original_value)

            attempts += 1
            break  # sortir de la boucle après une tentative

        if attempts == max_attempts and sum(
                sum(board.grid[i][j].value != 0 for j in range(9)) for i in range(9)) < initial_numbers:
            generate_random_board(board)
            cells_to_keep = random.sample(range(81), initial_numbers)
            attempts = 0


def generate_random_board(board):
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells:
        possible_nums = get_possible_nums(board, i, j)

        if not possible_nums:
            return False

        num = random.choice(possible_nums)
        board.grid[i][j].changeValue(num)

    return True


def has_unique_solution(board):
    cloned_board = clone_board(board)
    solve(cloned_board)
    return is_solution_unique(cloned_board, board)


def clone_board(board):
    cloned_board = SudokuBoard()
    for i in range(9):
        for j in range(9):
            cloned_board.grid[i][j].changeValue(board.grid[i][j].value)
    return cloned_board


def is_solution_unique(board1, board2):
    for i in range(9):
        for j in range(9):
            if board1.grid[i][j].value != board2.grid[i][j].value:
                return False
    return True


def get_possible_nums(board, row, col):
    possible_nums = [num for num in range(1, 10)]

    for i in range(9):
        if board.grid[row][i].value in possible_nums:
            possible_nums.remove(board.grid[row][i].value)
        if board.grid[i][col].value in possible_nums:
            possible_nums.remove(board.grid[i][col].value)

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board.grid[i + start_row][j + start_col].value in possible_nums:
                possible_nums.remove(board.grid[i + start_row][j + start_col].value)

    return possible_nums
