# Function : MA-20 | 2048
# author : Nathan
# Date : 05.03.2026
# Version : 3.0
import sys
from tkinter import *
import random
from tkinter import messagebox

############################ variables #################################

score = 0
coups = 0

# Tableau 2 dimensions des valeurs des tuiles.
numbers= [[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0],]

#numbers= [[2, 4, 8, 16],
#          [32, 64, 128, 256],
#          [512, 1024, 2048, 4096],
#          [8192, 0, 0, 0]]

labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]

# Dictionnaire des couleurs (fond des tuiles).
colors={0:"white",
        2:"#A7F6FF",
        4:"#A3CBFF",
        8:"#489EFF",
        16:"#5B3FFF",
        32:"#FFFFDA",
        64:"#FFFF82",
        128:"#FFFF00",
        256:"#D4D400",
        512:"#94FFAB",
        1024:"#3CFF66",
        2048:"#00E30F",
        4096:"#00B728",
        8192:"#F80004",
        }

############################# functions #################################

# Cette fonction sert à faire apparaitre aléatoirement un "2" ou un "4" à chaque coups.
def random_function(numbers):

    case_vide = []
    for line in range(4):
        for col in range(4):
            if numbers[line][col] == 0:
                case_vide.append((line,col))

    if case_vide == []:
        return

    line, col = random.choice(case_vide)

    valeur = random.choice([2, 2, 2, 2, 4])
    numbers[line][col] = valeur

# Ces 4 fonctions parcourent chaque colonne, récupèrent les 4 valeurs de droite à gauche / gauche à droite / haut en bas / bas en haut,
# les passe à pack4(), réécrivent la colonne avec le résultat et affiche le jeu mis à jour.
def right():
    tot_coups = 0
    for line in range(4):
        (numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0], coups) = \
            pack4(numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()
    print(tot_coups)


def left():
    tot_coups = 0
    for line in range(4):
        (numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3], coups) = \
            pack4(numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()
    print(tot_coups)

def up():
    tot_coups = 0
    for col in range(4):
        (numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col], coups) = \
            pack4(numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()
    print(tot_coups)

def down():
    tot_coups = 0
    for col in range(4):
        (numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col], coups) = \
            pack4(numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()
    print(tot_coups)


# Cette fonction sert à écouter les touches.
def key_pressed(event) :
    touche=event.keysym #récupérer le symbole de la touche
    if (touche=="Right" or touche=="d" or touche=="D"):
        right()
    if (touche=="Left" or touche=="a" or touche=="A"):
        left()
    if (touche=="Up" or touche=="w" or touche=="W"):
        up()
    if (touche=="Down" or touche=="s" or touche=="S"):
        down()


# Cette fonction sert à calculer les positions.
def pack4(a, b, c, d):
    coups = 0
    if c == 0 and d > 0:
        c, d = d, 0
        coups += 1
    if b == 0 and c > 0:
        b, c, d = c, d, 0
        coups += 1
    if a == 0 and b > 0:
        a, b, c, d = b, c, d, 0
        coups += 1
    if a == b and a > 0:
        a, b, c, d = a * 2, c, d, 0
        coups += 1
    if b == c and b > 0:
        b, c, d = b * 2, d, 0
        coups += 1
    if c == d and c > 0:
        c, d = c * 2, 0
        coups += 1

    return [a, b, c, d, coups]

# Cette fonction sert à afficher le jeu.
def display_game():
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if numbers[line][col] == 0:
                labels[line][col].config(text="", bg=colors[numbers[line][col]])
            else:
                labels[line][col].config(text=numbers[line][col], bg=colors[numbers[line][col]])
    check_2048(numbers)
    finish_game(numbers)


won = False
# Cette fonction sert à détecter si vous avez gagné (atteindre le 2048), et affiche un message pour l'annoncer.
def check_2048(numbers):
    global won
    for li in numbers:
        for valeur in li:
            if valeur == 2048 and won == False:
                messagebox.showinfo("Bravo", "Vous avez fait un 2048 !!! \n \nVous pouvez continuer à jouer.")
                won = True

# Cette fonction sert à détecter si vous avez perdu, et affiche un message pour l'annoncer.
def finish_game(numbers):
    for line in numbers:
        if 0 in line:
            return

    for line in range(4):
        for col in range(3):
            if numbers[line][col] == numbers[line][col+1]:
                return

    for col in range(4):
        for line in range(3):
            if numbers[line][col] == numbers[line+1][col]:
                return

    messagebox.showerror("OUPS", "Vous avez perdu !")

#def restart():
#    global numbers
#    numbers = [[2, 4, 8, 16],
#               [32, 64, 128, 256],
#               [512, 1024, 2048, 4096],
#               [8192, 0, 0, 0]]


############################## UI & main ###################################


window = Tk()
window.title("2048")
window.geometry("370x555")
window.resizable(width=False, height=False)


frm_global = Frame(window, bg="#D5FEFF")
frm_global.pack(fill=X)


frm_score = Frame(frm_global, bg="#D5FEFF")
frm_score.pack(fill=X)


lbl_score = Label(frm_score, text=f"Score : {score}", bg="#5de1ff", fg="#0004FF", width=20, height=1, borderwidth=1, relief="solid", font=("Arial 45 bold"))
lbl_score.pack(padx=10, pady=10, side=TOP)


frm_restart = Frame(frm_global, bg="#D5FEFF")
frm_restart.pack(fill=X)


# Pour plus tard -> command=restart
btn_restart = Button(frm_restart, text="Recommencer", bg="#13099C", width=17, height=1, borderwidth=1, relief="solid", font=("Arial 25 bold"), fg="white")
btn_restart.pack(side=TOP)

# Cette frame sert à créer une séparation au milieu de la fenêtre pour respecter ma maquette.
frm_separation = Frame(frm_global, bg="#D5FEFF")
frm_separation.pack(padx=14, pady=14, fill=X, side=TOP)

dx=5 # horizontal
dy=5 # vertical

# Cette frame contient le tableau d'affichage des tuiles.
frm_game = Frame(frm_global, bg="#D5FEFF")
frm_game.pack(padx=10, pady=10, fill=X, side=BOTTOM)

for line in range(len(numbers)):
    frm_line = Frame(frm_game, bg="#5de1ff")
    frm_line.pack(fill=X)
    for col in range(len(numbers[line])):
        labels[line][col] = Label (frm_line,text =numbers[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial 15 bold"))
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)

window.bind("<Key>", key_pressed)
display_game()
window.mainloop()