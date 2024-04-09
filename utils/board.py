from utils.cell import SudokuCell


class SudokuBoard:
    def __init__(self):
        self.grid = [[SudokuCell() for _ in range(9)] for _ in range(9)]

    def getColsBoard(self, cols: int) -> list:
        colonne = []
        for i in range(9):
            colonne.append(self.grid[cols][i].value)
        return colonne

    def getRowBoard(self, row: int) -> list:
        ligne = []
        for i in range(9):
            ligne.append(self.grid[i][row].value)
        return ligne

    def getSquareBoard(self, row: int, cols: int) -> list:
        square = []
        row_start = (row // 3) * 3
        col_start = (cols // 3) * 3
        for i in range(3):
            for j in range(3):
                square.append(self.grid[i + row_start][j + col_start].value)
        return square

    def __str__(self):
        board = ""
        for i in range(9):
            for j in range(9):
                board += str(self.grid[i][j].value) + " "
                if (j + 1) % 3 == 0 and j != 8:
                    board += "| "
            board += "\n"
            if (i + 1) % 3 == 0 and i != 8:
                board += "-" * 21 + "\n"
        return board
