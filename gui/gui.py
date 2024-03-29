import tkinter as tk
from utils.board import SudokuBoard

class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.board = SudokuBoard()
        # Créez la grille de Sudoku et les autres éléments de l'interface graphique.

    def run(self):
        self.window.mainloop()

board = SudokuBoard()