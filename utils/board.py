from cell import SudokuCell

class SudokuBoard:
    def __init__(self):
        self.grid = [[SudokuCell() for _ in range(9)] for _ in range(9)]
        
    def getColsBoard(self,cols: int)->list:
        colonne = []
        for i in range(9):
            colonne.append(self.grid[i][cols])
        return colonne
    def getRowBoard(self, row: int)->list:
        ligne = []
        for i in range(9):
            ligne.append(self.grid[row][i])
        return ligne

