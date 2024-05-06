import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
sys.path.append('..')
from algo import generator, solver
from utils.board import SudokuBoard

class SudokuGUI:

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Sudoku")
        self.main_window.config(background='White')
        self.main_window.geometry("1366x768")
        self.main_window.minsize(1366, 768)
        self.main_window.maxsize(1366, 768)

        self.create_menu()

    def select_cell(self, event):
        global selected_cell, rectangle, cell_x, cell_y, cell_width, cell_height
        if selected_cell:
            self.game_board_canvas.delete(rectangle)
        cell_x = event.x
        cell_y = event.y
        offset_x = cell_x % 60
        cell_x -= offset_x
        cell_width = cell_x + 60
        offset_y = cell_y % 60
        cell_y -= offset_y
        cell_height = cell_y + 60
        rectangle = self.game_board_canvas.create_rectangle(cell_x, cell_y, cell_width, cell_height, outline="blue", width=5)
        selected_cell = True

    def write_number(self, number, x, y):
        global player_board
        check = solver.check_valid_move(player_board, y, x, int(number))
        table_object = player_board.getGrid()
        table_object[y][x].changeValue(int(number))
        print(player_board)
        return check

    def select_number(self, event):
        global selected_number, rectangle_number, cell_x, cell_y, number_canvas, player_board, board
        if selected_number:
            self.number_canvas.delete(rectangle_number)
        number_x = event.x
        number_y = event.y
        offset_x = number_x % 60
        number_x -= offset_x
        number_width = number_x + 60
        offset_y = number_y % 60
        number_y -= offset_y
        number_height = number_y + 60
        rectangle_number = self.number_canvas.create_rectangle(number_x, number_y, number_width, number_height,
                                                               outline="red", width=5)
        selected_number = True
        selected_number = (number_y / 60) + 1
        cell_column = int(cell_x / 60)
        cell_row = int(cell_y / 60)
        cell_value = board.getColsBoard(cell_row)[cell_column]
        if cell_value == 0:
            cell_rectangle = self.game_board_canvas.create_rectangle(cell_x + 10, cell_y + 10, cell_width - 10,
                                                                     cell_height - 10, outline='', fill="white")

            correct_number = solution_board.getColsBoard(cell_row)[cell_column]  # Obtenir le nombre correct
            if selected_number == correct_number:
                cell_text = self.game_board_canvas.create_text(cell_x + 30, cell_y + 30, text=int(selected_number),
                                                               font=('Helvetica', 12, 'bold'), fill="green")
            else:
                cell_text = self.game_board_canvas.create_text(cell_x + 30, cell_y + 30, text=int(selected_number),
                                                               font=('Helvetica', 12, 'bold'), fill="red")
        else:
            messagebox.showinfo("Invalid Cell", "This cell is already completed")

    def next_page(self):
        global page_index
        page_index = 1
        global photo, image_label
        self.text1.destroy()
        self.text2.destroy()
        self.text3.destroy()
        self.text4.destroy()
        self.text5.destroy()
        self.text6.destroy()
        self.text7.destroy()
        self.text8.destroy()
        self.text9.destroy()
        self.text10.destroy()
        self.text11.destroy()
        self.back_button.destroy()
        self.next_button.destroy()
        self.image_label.destroy()

        # Create new page elements (same as before)

    def rules_page(self):
        # À faire
        pass

    def create_menu(self):
        global x, z, y, page_index
        if x == 1:
            self.title.destroy()
            self.text1.destroy()
            self.text2.destroy()
            self.text3.destroy()
            self.text4.destroy()
            self.text5.destroy()
            self.text6.destroy()
            self.text7.destroy()
            self.text8.destroy()
            self.back_button.destroy()
            self.next_button.destroy()
            self.image_label.destroy()
        elif x == 2:
            self.difficulty_title.destroy()
            self.difficult_button.destroy()
            self.medium_button.destroy()
            self.easy_button.destroy()
            self.back_button.destroy()
        z = 0
        y = 0
        page_index = 0

        self.title = Label(self.main_window, text="SUDOKU", font="Calibri, 40", fg='Black')
        self.title.pack(side=TOP)

        self.play_button = Button(self.main_window, text='  Jouer  ', command=self.play, font="Calibri, 20", bg='Black', fg='White')
        self.play_button.pack(side=TOP, pady=90)
        self.rules_button = Button(self.main_window, text=' Règles ', command=self.rules_page, font="Calibri, 20", bg='Black', fg='White')
        self.rules_button.pack(side=TOP, pady=90)
        self.quit_button = Button(self.main_window, text=' Quitter ', command=self.main_window.destroy, font="Calibri, 20", bg='Black', fg='White')
        self.quit_button.pack(side=TOP, pady=90)

    def create_game_board(self):
        self.game_board_canvas = Canvas(self.main_window, width=540, height=540, bg="white")
        self.game_board_canvas.pack(side=TOP, pady=20, padx=30)

        # Dessiner les lignes de la grille
        # Dessiner les lignes verticales
        for i in range(10):
            x = 60 * i
            if i % 3 == 0:
                self.game_board_canvas.create_line(x, 0, x, 540, fill="black", width=5)
            else:
                self.game_board_canvas.create_line(x, 0, x, 540, fill="black", width=2)

        # Dessiner les lignes horizontales
        for i in range(10):
            y = 60 * i
            if i % 3 == 0:
                self.game_board_canvas.create_line(0, y, 540, y, fill="black", width=5)
            else:
                self.game_board_canvas.create_line(0, y, 540, y, fill="black", width=2)

        # Lier l'événement de clic à la fonction select_cell
        self.game_board_canvas.bind('<Button-1>', self.select_cell)

    def create_number_canvas(self):
        self.number_canvas = Canvas(self.main_window, width=50, height=540)
        self.number_canvas.place(x=300, y=85)
        for i in range(9):
            self.number_canvas.create_text(25, i * 60 + 30, text=str(i + 1), width=100, font=('Helvetica', 12, 'bold'))
            self.number_canvas.create_line(0, 60 * i, 50, 60 * i)
        self.number_canvas.bind('<Button-1>', self.select_number)

    def place_number_in_row(self, row, col):
        for i, cell in enumerate(row):
            x = 60 * i + 30
            y = 60 * col + 30
            if cell != 0:
                self.game_board_canvas.create_text(x, y, text=cell, font=('Helvetica', 12, 'bold'))

    def start_game(self, difficulty):
        global y, board, player_board, solution_board
        y = 1
        self.difficulty_title.destroy()
        self.difficult_button.destroy()
        self.medium_button.destroy()
        self.easy_button.destroy()
        self.back_button.destroy()

        self.title = Label(self.main_window, text=difficulty, font="Calibri, 40", fg='Black')
        self.title.pack(side=TOP)

        self.loading_screen()  # Afficher l'écran de chargement

        self.create_game_board()
        self.create_number_canvas()
        # Board generation
        board = SudokuBoard()
        if difficulty == "Difficile":
            generator.generate(board, 30, timeout=1.5)
        elif difficulty == "Moyen":
            generator.generate(board, 45, timeout=1.5)
        elif difficulty == "Facile":
            generator.generate(board, 60, timeout=0.75)
        player_board = generator.clone_board(board) 
        solution_board = generator.clone_board(board)  # Stocker la grille résolue
        solver.solve(solution_board)  # Résoudre la grille
        print("Solution:")
        print(solution_board)  # Afficher la grille résolue dans la console
        for i in range(9):
            row = board.getColsBoard(i)
            self.place_number_in_row(row, i)

        self.loading.destroy()  # Fermer l'écran de chargement

        self.quit_button = Button(self.main_window, text=' Quit ', command=self.main_window.destroy, font="Calibri, 20",
                                  bg='Black', fg='White')
        self.quit_button.place(x=1240, y=715)
        self.back_button = Button(self.main_window, text=' Back ', command=self.play, font="Calibri, 20", bg='Black',
                                  fg='White')
        self.back_button.place(x=0, y=715)

    def draw_loading_circle(self, x, y, radius):
        self.canvas.delete("all")
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black', width=2)
        self.loading_animation(x, y, radius, 0)

    def loading_animation(self, x, y, radius, angle):
        self.canvas.delete("hole")
        angle_rad = math.radians(angle)
        hole_x = x + radius * math.cos(angle_rad)
        hole_y = y - radius * math.sin(angle_rad)
        hole = self.canvas.create_oval(hole_x - 35, hole_y - 35, hole_x + 7, hole_y + 7, fill="white", outline="white", tags="hole")
        angle += 10
        if angle >= 360:
            angle = angle - 360
        self.parent.after(50, lambda: self.loading_animation(x, y, radius, angle))

    def chargement(self):
        self.titre_difficulte.destroy()
        self.bt_difficile.destroy()
        self.bt_moyen.destroy()
        self.bt_facile.destroy()
        self.bt_retour.destroy()

        self.label = self.Label(parent, text="Chargement en cours...", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.canvas = self.Canvas(parent, width=100, height=100)
        self.canvas.pack()

        self.draw_loading_circle(50, 50, 30)
        
        time.sleep(10)
        partie()
        
    def jouer(self):
        global x, y, w
        if y == 0:
            self.title.destroy()
            self.play_button.destroy()
            self.quit_button.destroy()
            self.rules_button.destroy()
        elif y == 1:
            self.title.destroy()
            self.game_board_canvas.destroy()
            self.number_canvas.destroy()
            self.quit_button.destroy()
            self.back_button.destroy()

        self.difficulty_title = Label(self.main_window, text="DIFFICULTÉ", font="Calibri, 40", fg='Black')
        self.difficulty_title.pack(side=TOP)

        self.difficult_button = Button(self.main_window, text=' Difficile ', command=lambda: self.start_game("Difficile"), font="Calibri, 20", bg='Black', fg='White')
        self.difficult_button.pack(side=TOP, pady=90)
        self.medium_button = Button(self.main_window, text='  Moyen  ', command=lambda: self.start_game("Moyen"), font="Calibri, 20", bg='Black', fg='White')
        self.medium_button.pack(side=TOP, pady=90)
        self.easy_button = Button(self.main_window, text='  Facile  ', command=lambda: self.start_game("Facile"), font="Calibri, 20", bg='Black', fg='White')
        self.easy_button.pack(side=TOP, pady=90)

        self.back_button = Button(self.main_window, text=' Retour ', command=self.create_menu, font="Calibri, 20", bg='Black', fg='White')
        self.back_button.place(x=0, y=715)
        x = 2

    def loading_screen(self):
        self.loading = Toplevel(self.main_window)
        self.loading.title("Loading")
        self.loading.geometry("200x100")
        Label(self.loading, text="Loading Sudoku Grid...").pack()
        self.loading.update_idletasks()  # Mettre à jour l'interface utilisateur

    def run(self):
        self.main_window.mainloop()

x = 0
z = 0
y = 0
selected_cell = False
selected_number = False
page_index = 0
gui = SudokuGUI()
gui.run()