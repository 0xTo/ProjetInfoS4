import random
import sys
import time

from algo.solver import solve
from utils.board import SudokuBoard


def generate(board, initial_numbers, timeout=5):
    sys.setrecursionlimit(10000)

    # Générer une grille valide
    generate_random_board(board)

    # Choisir aléatoirement les cellules à conserver
    cells_to_keep = random.sample(range(81), initial_numbers)

    # Copier la grille originale pour vérifier la solvabilité
    original_board = clone_board(board)

    # Vider les cellules qui ne sont pas dans la liste des cellules à conserver
    for i in range(9):
        for j in range(9):
            index = i * 9 + j
            if index not in cells_to_keep:
                # Si la cellule n'est pas dans la liste des cellules à conserver, la vider
                board.grid[i][j].changeValue(0)

    # Vérifier la solvabilité de la grille
    start_time = time.time()  # Enregistrer l'heure de début
    while True:
        if is_solvable(board):
            end_time = time.time()  # Enregistrer l'heure de fin
            print("Temps pour résoudre la grille :", end_time - start_time, "secondes")
            return True
        elif time.time() - start_time > timeout:
            # Si le temps de résolution dépasse le délai spécifié, réinitialiser et générer une nouvelle grille
            reset_board(board)
            return generate(board, initial_numbers, timeout)


# Genere une grille avec des numéros choisis aléatoirement, mais qui permettent une grille possible
def generate_random_board(board):
    # Générer une grille aléatoire
    cells = [(i, j) for i in range(9) for j in range(9)] # Liste de listes de tuples (x, y)
    random.shuffle(cells)
    for i, j in cells:
        possible_nums = get_possible_nums(board, i, j)

        if not possible_nums:
            return False

        num = random.choice(possible_nums)
        board.grid[i][j].changeValue(num)

    return True


# Vérifier si la grille est solvable
def is_solvable(board):
    # Vérifier si la grille est solvable
    cloned_board = clone_board(board)
    return solve(cloned_board)


def reset_board(board):
    # Réinitialiser la grille en supprimant tous les chiffres
    for i in range(9):
        for j in range(9):
            board.grid[i][j].changeValue(0)


def clone_board(board):
    # Cloner la grille
    cloned_board = SudokuBoard()
    for i in range(9):
        for j in range(9):
            cloned_board.grid[i][j].changeValue(board.grid[i][j].value)
    return cloned_board


# Retourner une liste de chiffres possibles pour une cellule donnée (row, col)
def get_possible_nums(board, row, col):
    possible_nums = [i for i in range(1, 10)]

    # Vérifier les chiffres déjà présents dans la ligne, la colonne et le carré et retirer de la liste des chiffres possibles
    for i in range(9):
        if board.grid[row][i].value in possible_nums:
            possible_nums.remove(board.grid[row][i].value)
        if board.grid[i][col].value in possible_nums:
            possible_nums.remove(board.grid[i][col].value)

    # Trouver le coin supérieur gauche du carré 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    # Parcourir le carré 3x3 et retirer les chiffres déjà présents
    for i in range(3):
        for j in range(3):
            if board.grid[i + start_row][j + start_col].value in possible_nums:
                possible_nums.remove(board.grid[i + start_row][j + start_col].value)

    return possible_nums
