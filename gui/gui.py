from tkinter import *

from PIL import Image, ImageTk
from algo import generator
from utils.board import SudokuBoard



class SudokuGUI:
    def num(self, event):
        global w, rectangle, a, b, y1, x1, y2, x2
        if w == 1:
            self.canvas.delete(rectangle)
        a = event.x
        b = event.y
        c = a % 60
        x1 = a - c
        x2 = x1 + 60
        d = b % 60
        y1 = b - d
        y2 = y1 + 60
        rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=5)
        w = 1

    def selectChiffre(self, event):
        global u, rectangle2, a, b, y1, x1
        if u == 1:
            self.canvaChiffre.delete(rectangle2)
        a2 = event.x
        b2 = event.y
        c = a2 % 60
        x1C = a2 - c
        x2C = x1C + 60
        d = b2 % 60
        y1C = b2 - d
        y2C = y1C + 60
        rectangle2 = self.canvaChiffre.create_rectangle(x1C, y1C, x2C, y2C, outline="red", width=5)
        u = 1
        if (a != 0 and b != 0):
            chiffre = (y1C / 60) + 1
            r = self.canvas.create_rectangle(x1 + 10, y1 + 10, x2 - 10, y2 - 10, outline='', fill="white")
            self.canvas.create_text(x1 + 30, y1 + 30, text=int(chiffre), font=('Helvetica', 12, 'bold'))

    def suivant(self):
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
        self.bt_retour.destroy()
        self.bt_suivant.destroy()
        self.label_image.destroy()

        self.text1 = Label(self.window, text="Utiliser le processus d'élimination", font=("Calibri", 15, "bold"),
                           fg='Black')
        self.text1.pack(side=TOP, anchor=SW, pady=2, padx=20)

        self.text2 = Label(self.window,
                           text="""Que voulons-nous dire en utilisant "processus d'élimination" pour jouer au Sudoku? Voici un exemple. Dans cette grille de Sudoku (illustrée ci-dessous), la colonne verticale de l'extrême gauche (encerclée en bleu) ne manque que quelques chiffres: 1, 5 et 6. """,
                           font=("Calibri", 8), fg='Black')
        self.text2.pack(side=TOP, anchor=SW, padx=20)
        self.text3 = Label(self.window,
                           text="""Une façon de déterminer quels nombres peuvent aller dans chaque espace est d'utiliser le processus d'élimination pour voir quels autres numéros sont déjà inclus dans chaque carré-car il ne peut y avoir de duplication des nombres 1-9 dans chaque carré (ou ligne ou colonne).""",
                           font=("Calibri", 8), fg='Black')
        self.text3.pack(side=TOP, anchor=SW, padx=20)

        image = Image.open("./gui/Sudoku_im1.jpg")
        photo = ImageTk.PhotoImage(image)
        self.label_image = Label(self.window, image=photo)
        self.label_image.image = photo
        self.label_image.pack(side=TOP, pady=2)

        self.text4 = Label(self.window,
                           text="""Dans ce cas, remarquons rapidement la présence du nombre 1 en haut à gauche et au centre des cases gauches de la grille (encadrés en rouge). Cela implique qu'il ne reste qu'un seul espace dans la colonne à l'extrême gauche où un 1 pourrait être placé (encadré en vert).""",
                           font=("Calibri", 8), fg='Black')
        self.text4.pack(side=TOP, anchor=SW, padx=20)
        self.text5 = Label(self.window,
                           text="""Voici comment fonctionne le processus d'élimination dans Sudoku : vous identifiez les espaces disponibles et les chiffres manquants, puis vous déduisez, en fonction de leur position dans la grille, quels chiffres peuvent être insérés dans chaque espace.""",
                           font=("Calibri", 8), fg='Black')
        self.text5.pack(side=TOP, anchor=SW, padx=20)
        self.text6 = Label(self.window,
                           text="""Le jeu offre une infinité de variations, avec des millions de combinaisons possibles et divers niveaux de difficulté. Tout repose sur l'utilisation des chiffres, le remplissage des espaces vides par déduction et l'interdiction de répéter les chiffres dans chaque carré, ligne ou colonne.""",
                           font=("Calibri", 8), fg='Black')
        self.text6.pack(side=TOP, anchor=SW, padx=20)

        self.bt_suivant = Button(self.window, text=' Retour au menu ', command=self.menu, font="Calibri, 20",
                                 bg='Black', fg='White')
        self.bt_suivant.place(x=1140, y=715)
        self.bt_retour = Button(self.window, text=' Retour ', command=self.regle, font="Calibri, 20", bg='Black',
                                fg='White')
        self.bt_retour.place(x=0, y=715)

    def regle(self):
        global z, x
        x = 1
        if z == 0:
            self.titre.destroy()
            self.bt_jouer.destroy()
            self.bt_quitter.destroy()
            self.bt_regle.destroy()
        elif z == 1:
            self.text1.destroy()
            self.text2.destroy()
            self.text3.destroy()
            self.text4.destroy()
            self.text5.destroy()
            self.text6.destroy()
            self.titre.destroy()
            self.bt_retour.destroy()
            self.bt_suivant.destroy()
            self.label_image.destroy()

        self.titre = Label(self.window, text="Règles", font="Calibri, 40", fg='Black')
        self.titre.pack(side=TOP)
        self.text1 = Label(self.window, text="Utilisez les numéros 1-9", font=("Calibri", 15, "bold"), fg='Black')
        self.text1.pack(side=TOP, anchor=SW, pady=3, padx=20)

        self.text2 = Label(self.window,
                           text="""Sudoku est joué sur une grille de 9 x 9 espaces. Dans les lignes et les colonnes sont 9 "carrés" (composé de 3 x 3 espaces). Chaque rangée, colonne et carré (9 espaces chacun) doit être rempli avec les numéros 1-9, sans répéter aucun nombre dans la rangée, la colonne ou le carré.""",
                           font=("Calibri", 8), fg='Black')
        self.text2.pack(side=TOP, anchor=SW, padx=20)
        self.text3 = Label(self.window,
                           text="""Comme sur l'image ci-dessous d'une grille de Sudoku réelle, chaque grille de Sudoku est livré avec quelques espaces déjà remplis; plus les espaces sont remplis, plus le jeu est facile, mais il y a très peu d'espaces qui sont déjà remplis.""",
                           font=("Calibri", 8), fg='Black')
        self.text3.pack(side=TOP, anchor=SW, padx=20)

        self.text4 = Label(self.window, text="Ne répétez aucun numéro", font=("Calibri", 15, "bold"), fg='Black')
        self.text4.pack(side=TOP, anchor=SW, pady=3, padx=20)

        image = Image.open("./gui/Sudoku_im2.jpg")
        photo = ImageTk.PhotoImage(image)
        self.label_image = Label(self.window, image=photo)
        self.label_image.image = photo
        self.label_image.pack(side=TOP, pady=10)

        self.text5 = Label(self.window,
                           text="""Dans le coin supérieur gauche (encerclé en bleu), la plupart des cases sont remplies ne laissant que les chiffres 5 et 6 absents. En identifiant les chiffres manquants dans chaque carré, ligne ou colonne, nous utilisons l'élimination et la déduction pour remplir les espaces vides de la grille.""",
                           font=("Calibri", 8), fg='Black')
        self.text5.pack(side=TOP, anchor=SW, padx=20)
        self.text6 = Label(self.window,
                           text="""Dans le coin supérieur gauche, nous avons besoin des chiffres 5 et 6 pour finir le carré. Mais avec la complexité des lignes et des carrés voisins, leur emplacement est incertain. Nous devons donc mettre ce coin de côté pour l'instant et remplir d'autres parties de la grille à la place.""",
                           font=("Calibri", 8), fg='Black')
        self.text6.pack(side=TOP, anchor=SW, padx=20)

        self.text7 = Label(self.window, text="Ne devinez pas", font=("Calibri", 15, "bold"), fg='Black')
        self.text7.pack(side=TOP, anchor=SW, pady=3, padx=20)
        self.text8 = Label(self.window,
                           text="""Dans le coin supérieur gauche, nous avons besoin des chiffres 5 et 6 pour finir le carré. Mais avec la complexité des lignes et des carrés voisins, leur emplacement est incertain. Nous devons donc mettre ce coin de côté pour l'instant et remplir d'autres parties de la grille à la place.""",
                           font=("Calibri", 8), fg='Black')
        self.text8.pack(side=TOP, anchor=SW, padx=20)

        self.bt_suivant = Button(self.window, text=' Suivant ', command=self.suivant, font="Calibri, 20", bg='Black',
                                 fg='White')
        self.bt_suivant.place(x=1240, y=715)
        self.bt_retour = Button(self.window, text=' Retour ', command=self.menu, font="Calibri, 20", bg='Black',
                                fg='White')
        self.bt_retour.place(x=0, y=715)

    def menu(self):
        global x, z, y
        if x == 1:
            self.titre.destroy()
            self.text1.destroy()
            self.text2.destroy()
            self.text3.destroy()
            self.text4.destroy()
            self.text5.destroy()
            self.text6.destroy()
            self.text7.destroy()
            self.text8.destroy()
            self.bt_suivant.destroy()
            self.bt_retour.destroy()
            self.label_image.destroy()
        elif x == 2:
            self.titre_difficulte.destroy()
            self.bt_difficile.destroy()
            self.bt_facile.destroy()
            self.bt_moyen.destroy()
            self.bt_retour.destroy()
        z = 0
        y = 0

        self.titre = Label(self.window, text="SUDOKU", font="Calibri, 40", fg='Black')
        self.titre.pack(side=TOP)

        self.bt_jouer = Button(self.window, text='  Jouer  ', command=self.jouer, font="Calibri, 20", bg='Black',
                               fg='White')
        self.bt_jouer.pack(side=TOP, pady=90)
        self.bt_regle = Button(self.window, text=' Règles ', command=self.regle, font="Calibri, 20", bg='Black',
                               fg='White')
        self.bt_regle.pack(side=TOP, pady=90)
        self.bt_quitter = Button(self.window, text=' Quitter ', command=self.window.destroy, font="Calibri, 20",
                                 bg='Black', fg='White')
        self.bt_quitter.pack(side=TOP, pady=90)

    def grille(self):
        self.canvas = Canvas(self.window, width=540, height=540)
        self.canvas.pack(side=TOP, pady=20, padx=30)
        for i in range(10):
            if i % 3 == 0:
                thickness = 5
            else:
                thickness = 2
            self.canvas.create_line(60 * i, 0, 60 * i, 540, fill="black", width=thickness)
            self.canvas.create_line(0, 60 * i, 540, 60 * i, fill="black", width=thickness)
            self.canvas.bind('<Button-1>', self.num)

    def grilleChiffre(self):
        self.canvaChiffre = Canvas(self.window, width=50, height=540)
        self.canvaChiffre.place(x=300, y=85)
        for i in range(9):
            self.canvaChiffre.create_text(25, i * 60 + 30, text=str(i + 1), width=100, font=('Helvetica', 12, 'bold'))
            self.canvaChiffre.create_line(0, 60 * i, 50, 60 * i)
        self.canvaChiffre.bind('<Button-1>', self.selectChiffre)

    def partie(self, difficulty):
        global y
        y = 1
        self.titre_difficulte.destroy()
        self.bt_difficile.destroy()
        self.bt_moyen.destroy()
        self.bt_facile.destroy()
        self.bt_retour.destroy()

        self.titre = Label(self.window, text=difficulty, font="Calibri, 40", fg='Black')
        self.titre.pack(side=TOP)

        self.grille()
        self.grilleChiffre()

        self.bt_quitter = Button(self.window, text=' Quitter ', command=self.window.destroy, font="Calibri, 20",
                                 bg='Black', fg='White')
        self.bt_quitter.place(x=1240, y=715)
        self.bt_retour = Button(self.window, text=' Retour ', command=self.jouer, font="Calibri, 20", bg='Black',
                                fg='White')
        self.bt_retour.place(x=0, y=715)

    def jouer(self):
        global x, y, w
        if y == 0:
            self.titre.destroy()
            self.bt_jouer.destroy()
            self.bt_quitter.destroy()
            self.bt_regle.destroy()
        elif y == 1:
            self.titre.destroy()
            self.canvas.destroy()
            self.canvaChiffre.destroy()
            self.bt_quitter.destroy()
            self.bt_retour.destroy()

        self.titre_difficulte = Label(self.window, text="DIFFICULTÉ", font="Calibri, 40", fg='Black')
        self.titre_difficulte.pack(side=TOP)

        self.bt_difficile = Button(self.window, text=' Difficile ', command=lambda: self.partie("Difficile"),
                                   font="Calibri, 20", bg='Black', fg='White')
        self.bt_difficile.pack(side=TOP, pady=90)
        self.bt_moyen = Button(self.window, text='  Moyen  ', command=lambda: self.partie("Moyen"), font="Calibri, 20",
                               bg='Black', fg='White')
        self.bt_moyen.pack(side=TOP, pady=90)
        self.bt_facile = Button(self.window, text='  Facile  ', command=lambda: self.partie("Facile"),
                                font="Calibri, 20", bg='Black', fg='White')
        self.bt_facile.pack(side=TOP, pady=90)

        self.bt_retour = Button(self.window, text=' Retour ', command=self.menu, font="Calibri, 20", bg='Black',
                                fg='White')
        self.bt_retour.place(x=0, y=715)
        x = 2

    def __init__(self):
        self.window = Tk()
        self.window.title("Sudoku")
        self.window.config(background='White')
        self.window.geometry("1366x768")
        self.window.minsize(1366, 768)
        self.window.maxsize(1366, 768)

        self.menu()

    def run(self):
        self.window.mainloop()


x = 0
z = 0
y = 0
w = 0
u = 0
a = 0
b = 0
gui = SudokuGUI()
gui.run()
