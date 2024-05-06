import sys
import threading
from tkinter import *
from tkinter import messagebox

import math
from PIL import Image, ImageTk

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
        rectangle = self.game_board_canvas.create_rectangle(cell_x, cell_y, cell_width, cell_height, outline="blue",
                                                            width=5)
        selected_cell = True

    def write_number(self, number, x, y):
        global player_board
        check = solver.check_valid_move(player_board, y, x, int(number))
        table_object = player_board.getGrid()
        table_object[y][x].changeValue(int(number))
        print(player_board)
        return check

    def select_number(self, event):
        global selected_number, rectangle_number, cell_x, cell_y, number_canvas, player_board, board, life
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
        correct_number = solution_board.getColsBoard(cell_row)[cell_column]  # Obtenir le nombre correct

        # Vérifier si la cellule contient déjà le numéro correct
        if cell_value != 0 and cell_value == correct_number:
            messagebox.showinfo("Case invalide", "Cette cellule est déjà complétée correctement")
            return

        if cell_value == 0:
            cell_rectangle = self.game_board_canvas.create_rectangle(cell_x + 10, cell_y + 10, cell_width - 10,
                                                                     cell_height - 10, outline='', fill="white")

            if selected_number == correct_number:
                cell_text = self.game_board_canvas.create_text(cell_x + 30, cell_y + 30, text=int(selected_number),
                                                               font=('Helvetica', 12, 'bold'), fill="green")
                # Mettre à jour la valeur de la cellule dans player_board
                player_board.getColsBoard(cell_row)[cell_column] = selected_number
            else:
                cell_text = self.game_board_canvas.create_text(cell_x + 30, cell_y + 30, text=int(selected_number),
                                                               font=('Helvetica', 12, 'bold'), fill="red")
                life -= 1
                self.vie.destroy()
                self.vie = Label(self.main_window, text="Vies restantes : " + str(life), font="Calibri, 20", fg='Black',
                                 bg="White")
                self.vie.pack()
                if (life <= 0):
                    self.vie.destroy()
                    messagebox.showinfo("YOU LOSE", "Vous êtes arrivé à court de vie")
                    self.play()

        else:
            messagebox.showinfo("Case invalide", "Cette cellule est déjà complétée")

    def next_page(self):
        global page_index
        page_index = 1
        global z
        z = 1
        global photo, label_image
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
        self.label_image.destroy()

        self.text1 = Label(self.main_window, text="Utiliser le processus d'élimination", font=("Calibri", 20, "bold"),
                           fg='Black', bg="White")
        self.text1.pack(side=TOP, anchor=SW, pady=2, padx=15)

        self.text2 = Label(self.main_window,
                           text="""Que voulons-nous dire en utilisant "processus d'élimination" pour jouer au Sudoku? Voici un exemple. Dans cette grille de Sudoku (illustrée ci-dessous), la colonne verticale de l'extrême gauche""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text2.pack(side=TOP, anchor=SW, padx=15)
        self.text7 = Label(self.main_window,
                           text="""(encerclée en bleu) ne manque que quelques chiffres: 1, 5 et 6. Une façon de déterminer quels nombres peuvent aller dans chaque espace est d'utiliser le processus d'élimination pour voir""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text7.pack(side=TOP, anchor=SW, padx=15)
        self.text3 = Label(self.main_window,
                           text="""quels autres numéros sont déjà inclus dans chaque carré-car il ne peut y avoir de duplication des nombres 1-9 dans chaque carré (ou ligne ou colonne).""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text3.pack(side=TOP, anchor=SW, padx=15)

        image = Image.open("Sudoku_im1.jpg")
        image = image.resize((int(image.width / 1.5), int(image.height / 1.5)))
        photo = ImageTk.PhotoImage(image)
        self.label_image = Label(self.main_window, image=photo)
        self.label_image.image = photo
        self.label_image.pack(side=TOP, pady=10)

        self.text4 = Label(self.main_window,
                           text="""Dans ce cas, remarquons rapidement la présence du nombre 1 en haut à gauche et au centre des cases gauches de la grille (encadrés en rouge). Cela implique qu'il ne reste qu'un seul espace""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text4.pack(side=TOP, anchor=SW, padx=15)
        self.text5 = Label(self.main_window,
                           text="""dans la colonne à l'extrême gauche où un 1 pourrait être placé (encadré en vert). Voici comment fonctionne le processus d'élimination dans Sudoku : vous identifiez les espaces disponibles et""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text5.pack(side=TOP, anchor=SW, padx=15)
        self.text6 = Label(self.main_window,
                           text="""les chiffres manquants, puis vous déduisez, en fonction de leur position dans la grille, quels chiffres peuvent être insérés dans chaque espace. Le jeu offre une infinité de variations, avec des""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text6.pack(side=TOP, anchor=SW, padx=15)
        self.text8 = Label(self.main_window,
                           text="""millions de combinaisons possibles et divers niveaux de difficulté. Tout repose sur l'utilisation des chiffres, le remplissage des espaces vides par déduction et l'interdiction de répéter les chiffres""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text8.pack(side=TOP, anchor=SW, padx=15)
        self.text9 = Label(self.main_window, text="""dans chaque carré, ligne ou colonne.""", font=("Calibri", 13),
                           fg='Black', bg="White")
        self.text9.pack(side=TOP, anchor=SW, padx=15)

        self.next_button = Button(self.main_window, text=' Retour au menu ', command=self.create_menu,
                                  font="Calibri, 20", bg='Black', fg='White')
        self.next_button.place(x=1140, y=715)
        self.back_button = Button(self.main_window, text=' Retour ', command=self.rules_page, font="Calibri, 20",
                                  bg='Black', fg='White')
        self.back_button.place(x=0, y=715)

        # Create new page elements (same as before)

    def rules_page(self):
        global z, page_index
        page_index = 1
        if z == 0:
            self.title.destroy()
            self.play_button.destroy()
            self.quit_button.destroy()
            self.rules_button.destroy()
        elif z == 1:
            self.text1.destroy()
            self.text2.destroy()
            self.text3.destroy()
            self.text4.destroy()
            self.text5.destroy()
            self.text6.destroy()
            self.text7.destroy()
            self.text8.destroy()
            self.text9.destroy()
            self.title.destroy()
            self.back_button.destroy()
            self.next_button.destroy()
            self.label_image.destroy()

        self.title = Label(self.main_window, text="Règles", font="Calibri, 40", fg='Black', bg="White")
        self.title.pack(side=TOP)
        self.text1 = Label(self.main_window, text="Utilisez les numéros 1-9", font=("Calibri", 20, "bold"), fg='Black', bg="White")
        self.text1.pack(side=TOP, anchor=SW, pady=3, padx=15)

        self.text2 = Label(self.main_window,
                           text="""Sudoku est joué sur une grille de 9 x 9 espaces. Dans les lignes et les colonnes sont 9 "carrés" (composé de 3 x 3 espaces). Chaque rangée, colonne et carré (9 espaces chacun) doit être rempli""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text2.pack(side=TOP, anchor=SW, padx=15)
        self.text3 = Label(self.main_window,
                           text="""avec les numéros 1-9, sans répéter aucun nombre dans la rangée, la colonne ou le carré. Comme sur l'image ci-dessous d'une grille de Sudoku réelle, chaque grille de Sudoku est livré avec""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text3.pack(side=TOP, anchor=SW, padx=15)
        self.text7 = Label(self.main_window,
                           text="""quelques espaces déjà remplis; plus les espaces sont remplis, plus le jeu est facile, mais il y a très peu d'espaces qui sont déjà remplis.""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text7.pack(side=TOP, anchor=SW, padx=15)

        self.text4 = Label(self.main_window, text="Ne répétez aucun numéro", font=("Calibri", 20, "bold"), fg='Black', bg="White")
        self.text4.pack(side=TOP, anchor=SW, pady=3, padx=15)

        image = Image.open("Sudoku_im2.jpg")
        image = image.resize((int(image.width / 1.5), int(image.height / 1.5)))
        photo = ImageTk.PhotoImage(image)
        self.label_image = Label(self.main_window, image=photo)
        self.label_image.image = photo
        self.label_image.pack(side=TOP, pady=10)

        self.text5 = Label(self.main_window,
                           text="""Dans le coin supérieur gauche (encerclé en bleu), la plupart des cases sont remplies ne laissant que les chiffres 5 et 6 absents. En identifiant les chiffres manquants dans chaque carré, ligne""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text5.pack(side=TOP, anchor=SW, padx=15)
        self.text6 = Label(self.main_window,
                           text="""ou colonne, nous utilisons l'élimination et la déduction pour remplir les espaces vides de la grille. Dans le coin supérieur gauche, nous avons besoin des chiffres 5 et 6 pour finir le carré.""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text6.pack(side=TOP, anchor=SW, padx=15)
        self.text8 = Label(self.main_window,
                           text="""Mais avec la complexité des lignes et des carrés voisins, leur emplacement est incertain. Nous devons donc mettre ce coin de côté pour l'instant et remplir d'autres parties de la grille à la place.""",
                           font=("Calibri", 13), fg='Black', bg="White")
        self.text8.pack(side=TOP, anchor=SW, padx=15)

        self.next_button = Button(self.main_window, text=' Continuer ', command=self.next_page, font="Calibri, 20",
                                  bg='Black', fg='White')
        self.next_button.place(x=1220, y=715)
        self.back_button = Button(self.main_window, text=' Retour au menu ', command=self.create_menu,
                                  font="Calibri, 20", bg='Black', fg='White')
        self.back_button.place(x=0, y=715)

    def create_menu(self):
        global z, y, page_index
        if page_index == 1:
            self.title.destroy()
            self.text1.destroy()
            self.text2.destroy()
            self.text3.destroy()
            self.text4.destroy()
            self.text5.destroy()
            self.text6.destroy()
            self.text7.destroy()
            self.text8.destroy()
            if hasattr(self, 'text9'):
                self.text9.destroy()
            self.back_button.destroy()
            self.next_button.destroy()
            self.label_image.destroy()
        elif page_index == 2:
            self.difficulty_title.destroy()
            self.difficult_button.destroy()
            self.medium_button.destroy()
            self.easy_button.destroy()
            self.back_button.destroy()
        z = 0
        y = 0
        page_index = 0

        self.title = Label(self.main_window, text="SUDOKU", font="Calibri, 40", fg='Black', bg="White")
        self.title.pack(side=TOP)

        self.play_button = Button(self.main_window, text='  Jouer  ', command=self.play, font="Calibri, 20", bg='Black',
                                  fg='White')
        self.play_button.pack(side=TOP, pady=90)
        self.rules_button = Button(self.main_window, text=' Règles ', command=self.rules_page, font="Calibri, 20",
                                   bg='Black', fg='White')
        self.rules_button.pack(side=TOP, pady=90)
        self.quit_button = Button(self.main_window, text=' Quitter ', command=self.main_window.destroy,
                                  font="Calibri, 20", bg='Black', fg='White')
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

        global y, life
        life = 5
        y = 1
        self.difficulty_title.destroy()
        self.difficult_button.destroy()
        self.medium_button.destroy()
        self.easy_button.destroy()
        self.back_button.destroy()

        self.title = Label(self.main_window, text=difficulty, font="Calibri, 40", fg='Black', bg="White")
        self.title.pack(side=TOP)

        self.chargement()  # Afficher l'écran de chargement

        # Utiliser le threading pour exécuter la génération de la grille en arrière-plan
        threading.Thread(target=self.generate_board, args=(difficulty,)).start()

    def generate_board(self, difficulty):
        global board, player_board, solution_board
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
        self.vie = Label(self.main_window, text="Vies restantes : " + str(life), font="Calibri, 20", fg='Black', bg="White")
        self.vie.pack()

    def draw_loading_circle(self, x, y, radius):
        self.canvas.delete("all")
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='Black', width=2)
        self.loading_animation(x, y, radius, 0)

    def loading_animation(self, x, y, radius, angle):
        self.canvas.delete("hole")
        angle_rad = math.radians(angle)
        hole_x = x + radius * math.cos(angle_rad)
        hole_y = y - radius * math.sin(angle_rad)
        hole = self.canvas.create_oval(hole_x - 35, hole_y - 35, hole_x + 7, hole_y + 7, fill="White", outline="White",
                                       tags="hole")
        angle += 10
        if angle >= 360:
            angle = angle - 360
        self.loading.after(50, lambda: self.loading_animation(x, y, radius, angle))

    def chargement(self):
        self.loading = Toplevel(self.main_window)
        self.loading.title("Chargement en cours...")
        self.loading.geometry("200x200")
        self.loading.minsize(200, 200)  # Définir la taille minimale de la fenêtre à 200x200
        self.loading.maxsize(200, 200)  # Définir la taille maximale de la fenêtre à 200x200

        self.canvas = Canvas(self.loading, width=200, height=200, bg="white")
        self.canvas.pack()

        self.radius = 50
        self.center_x = 100
        self.center_y = 100
        self.angle = 0

        self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                               self.center_x + self.radius, self.center_y + self.radius,
                               start=0, extent=360, style=ARC, fill="Black", outline="Black",
                               width=5)

        self.canvas.create_text(100, 25, text="Chargement de la grille...", fill="Black",
                                font=("Helvetica", 12, "bold"))  # Ajouter le style gras au texte

        self.animate()

    def animate(self):
        self.angle += 10
        self.canvas.delete("slice")
        self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                               self.center_x + self.radius, self.center_y + self.radius,
                               start=self.angle, extent=50, style=CHORD, outline="black", width=10, tags="slice",
                               fill="white")

        self.loading.after(50, self.animate)

    def play(self):
        global page_index, y, w
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
            self.vie.destroy()

        self.difficulty_title = Label(self.main_window, text="DIFFICULTÉ", font="Calibri, 40", fg='Black', bg="White")
        self.difficulty_title.pack(side=TOP)

        self.difficult_button = Button(self.main_window, text=' Difficile ',
                                       command=lambda: self.start_game("Difficile"), font="Calibri, 20", bg='Black',
                                       fg='White')
        self.difficult_button.pack(side=TOP, pady=90)
        self.medium_button = Button(self.main_window, text='  Moyen  ', command=lambda: self.start_game("Moyen"),
                                    font="Calibri, 20", bg='Black', fg='White')
        self.medium_button.pack(side=TOP, pady=90)
        self.easy_button = Button(self.main_window, text='  Facile  ', command=lambda: self.start_game("Facile"),
                                  font="Calibri, 20", bg='Black', fg='White')
        self.easy_button.pack(side=TOP, pady=90)

        self.back_button = Button(self.main_window, text=' Retour ', command=self.create_menu, font="Calibri, 20",
                                  bg='Black', fg='White')
        self.back_button.place(x=0, y=715)
        page_index = 2

    def run(self):
        self.main_window.mainloop()


life = 0
page_index = 0
z = 0
y = 0
selected_cell = False
selected_number = False
gui = SudokuGUI()
gui.run()
