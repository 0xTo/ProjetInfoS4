from utils.board import SudokuBoard

def solve(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    # Essayer de placer un chiffre de 1 à 9 dans la cellule vide
    for num in range(1, 10):
        # Vérifier si le chiffre peut être placé dans la cellule
        if check_valid_move(board, row, col, num):
            board.grid[row][col].changeValue(num)

            # Récursivement résoudre le reste de la grille (backtracking)
            if solve(board): # Si il n'y a plus de case vide
                return True

            # Si la grille n'est pas résolue, annuler le chiffre placé
            board.grid[row][col].changeValue(0)

    return False

# Retourner les coordonnées de la première cellule vide trouvée
def find_empty_cell(board):
    for x in range(9):
        for y in range(9):
            if board.grid[x][y].value == 0:
                return (x, y)
    return None

# Retourne True si le chiffre peut être placé dans la cellule (row, col)
def check_valid_move(board, row, col, num):
    # Vérifier si le chiffre est déjà présent dans la ligne ou la colonne
    for i in range(9):
        if board.grid[row][i].value == num or board.grid[i][col].value == num:
            return False

    # Vérifier si le chiffre est déjà présent dans le carré 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board.grid[i + start_row][j + start_col].value == num:
                return False

    return True

# Afficher la grille résolue
def print_resolved_board(board):
    # Cloner la grille pour éviter de modifier la grille originale
    cloned_board = clone_board(board)

    # Résoudre la grille clonée
    solve(cloned_board)

    # Afficher la grille résolue
    print(cloned_board)

# Cloner la grille et la retourner
def clone_board(board):
    # Cloner la grille
    cloned_board = SudokuBoard()
    for i in range(9):
        for j in range(9):
            cloned_board.grid[i][j].changeValue(board.grid[i][j].value)
    return cloned_board
