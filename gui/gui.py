import tkinter as tk
# from utils.board import SudokuBoard

class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        # self.board = SudokuBoard()

        self.window.title("Sudoku")
        self.window.config(background='White')
        self.window.geometry("1920x1080")
        self.window.minsize(1920,1080)
        self.window.maxsize(1920,1080)

        titre = Label(self.window, text="SUDOKU", font="Calibri, 40", fg='Black')
        titre.pack(side=TOP)

    def run(self):
        self.window.mainloop()

gui = SudokuGUI()
gui.run()
