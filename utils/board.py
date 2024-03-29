from cell import SudokuCell

class SudokuBoard:
    def __init__(self):
        self.grid = [[SudokuCell() for _ in range(9)] for _ in range(9)]
