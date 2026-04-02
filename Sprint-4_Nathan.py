# Titre : MA-20 | 2048
# Auteur : Nathan
# Date : 02.04.2026
# Version : 4.0

from tkinter import *
import random
from tkinter import messagebox


############################ variables #################################


# Variables des coups.
coups = 0
coups2 = 0

# Variables de victoire/défaite.
won = False
won2 = False
defeat = False
defeat2 = False

# Tableaux 2 dimensions des valeurs des tuiles + Labels.
numbers= [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],]

numbers2= [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],]

#numbers= [[2, 4, 8, 16],
#          [32, 64, 128, 256],
#          [512, 1024, 2048, 4096],
#          [8192, 0, 0, 0]]

labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]

labels2=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]

lbl_defeat = None
lbl_defeat2 = None

# Dictionnaires des couleurs (fond des tuiles).
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

colors2={0:"white",
        2:"#FFB7A7",
        4:"#FF8282",
        8:"#FF4848",
        16:"#FF0D0D",
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

# Ces 8 fonctions parcourent chaque colonne, récupèrent les 4 valeurs de droite à gauche / gauche à droite / haut en bas / bas en haut,
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


def left():
    tot_coups = 0
    for line in range(4):
        (numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3], coups) = \
            pack4(numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()

def up():
    tot_coups = 0
    for col in range(4):
        (numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col], coups) = \
            pack4(numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()

def down():
    tot_coups = 0
    for col in range(4):
        (numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col], coups) = \
            pack4(numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col])
        tot_coups += coups
    if tot_coups > 0:
        random_function(numbers)
    display_game()


def right2():
    tot_coups = 0
    for line in range(4):
        (numbers2[line][3], numbers2[line][2], numbers2[line][1], numbers2[line][0], coups2) = \
            pack4(numbers2[line][3], numbers2[line][2], numbers2[line][1], numbers2[line][0])
        tot_coups += coups2
    if tot_coups > 0:
        random_function(numbers2)
    display_game()


def left2():
    tot_coups = 0
    for line in range(4):
        (numbers2[line][0], numbers2[line][1], numbers2[line][2], numbers2[line][3], coups2) = \
            pack4(numbers2[line][0], numbers2[line][1], numbers2[line][2], numbers2[line][3])
        tot_coups += coups2
    if tot_coups > 0:
        random_function(numbers2)
    display_game()

def up2():
    tot_coups = 0
    for col in range(4):
        (numbers2[0][col], numbers2[1][col], numbers2[2][col], numbers2[3][col], coups2) = \
            pack4(numbers2[0][col], numbers2[1][col], numbers2[2][col], numbers2[3][col])
        tot_coups += coups2
    if tot_coups > 0:
        random_function(numbers2)
    display_game()

def down2():
    tot_coups = 0
    for col in range(4):
        (numbers2[3][col], numbers2[2][col], numbers2[1][col], numbers2[0][col], coups2) = \
            pack4(numbers2[3][col], numbers2[2][col], numbers2[1][col], numbers2[0][col])
        tot_coups += coups2
    if tot_coups > 0:
        random_function(numbers2)
    display_game()




# Cette fonction sert à écouter les touches.
def key_pressed(event) :
    touche=event.keysym #récupérer le symbole de la touche
    if (touche=="d" or touche=="D"):
        right()
    if (touche=="a" or touche=="A"):
        left()
    if (touche=="w" or touche=="W"):
        up()
    if (touche=="s" or touche=="S"):
        down()
    if (touche=="Right"):
        right2()
    if (touche=="Left"):
        left2()
    if (touche=="Up"):
        up2()
    if (touche=="Down"):
        down2()

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
    for line in range(len(numbers2)):
        for col in range(len(numbers2[line])):
            if numbers2[line][col] == 0:
                labels2[line][col].config(text="", bg=colors2[numbers2[line][col]])
            else:
                labels2[line][col].config(text=numbers2[line][col], bg=colors2[numbers2[line][col]])


# Cette fonction sert à détecter si vous avez gagné (atteindre le 2048), et affiche un message pour l'annoncer.
def check_2048(numbers):
    global won
    for li in numbers:
        for valeur in li:
            if valeur == 2048 and won == False:
                messagebox.showinfo("Bravo", "Vous avez fait un 2048 !!! \n \nVous pouvez continuer à jouer.")
                won = True


# Ces 2 fonction servent à afficher un label quand un joueur a perdu.
def display_defeat():
    global lbl_defeat
    if lbl_defeat is None:
        lbl_defeat= Label(frm_global,height=1, width=27, bg="black", fg="white", text="Vous avez perdu :/", font=("Arial 15 bold"))
        lbl_defeat.place(x=17, y=95)

def display_defeat2():
    global lbl_defeat2
    if lbl_defeat2 is None:
        lbl_defeat2= Label(frm_global,height=1, width=27, bg="black", fg="white", text="Vous avez perdu :/", font=("Arial 15 bold"))
        lbl_defeat2.place(x=655, y=95)


# Cette fonction sert à détecter si un des joueurs a perdu.
def finish_game(numbers):
    global defeat, defeat2

    defeat = True
    for line in numbers:
        if 0 in line:
            defeat = False
    for line in range(4):
        for col in range(3):
            if numbers[line][col] == numbers[line][col+1]:
                defeat = False
    for col in range(4):
        for line in range(3):
            if numbers[line][col] == numbers[line+1][col]:
                defeat = False
    defeat2 = True
    for line in numbers2:
        if 0 in line:
            defeat2 = False
    for line in range(4):
        for col in range(3):
            if numbers2[line][col] == numbers2[line][col+1]:
                defeat2 = False
    for col in range(4):
        for line in range(3):
            if numbers2[line][col] == numbers2[line+1][col]:
                defeat2 = False

    if defeat:
        display_defeat()
    if defeat2:
        display_defeat2()

# Cette fonction sert à recommencer à zero (les labels et certaines variables).
def restart():
    global numbers, numbers2,defeat, defeat2, lbl_defeat2,lbl_defeat
    defeat = False
    defeat2 = False
    numbers = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0], ]

    numbers2 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0], ]


    if lbl_defeat != None:
        lbl_defeat.destroy()
        lbl_defeat = None

    if lbl_defeat2 != None:
        lbl_defeat2.destroy()
        lbl_defeat2 = None

    random_function(numbers)
    random_function(numbers)
    random_function(numbers2)
    random_function(numbers2)

    display_game()


############################## UI & main ###################################


window = Tk()
window.title("2048")
window.geometry("1000x490")
window.resizable(width=False, height=False)

frm_global = Frame(window, bg="#D5FEFF")
frm_global.pack(fill=X)


frm_score = Frame(frm_global, bg="#D5FEFF")
frm_score.pack(fill=X)


lbl_score = Label(frm_score, text=f"Bleu", bg="#5de1ff", fg="#0004FF", width=9, height=1, borderwidth=1, relief="solid", font=("Arial 45 bold"))
lbl_score.pack(padx=10, pady=10, side=LEFT)

lbl_score = Label(frm_score, text=f"Rouge", bg="#FFA8A8", fg="#FF0000", width=9, height=1, borderwidth=1, relief="solid", font=("Arial 45 bold"))
lbl_score.pack(padx=10, pady=10, side=RIGHT)

frm_restart = Frame(frm_global, bg="#D5FEFF")
frm_restart.pack(fill=X)


# Cette frame sert à créer une séparation au milieu de la fenêtre pour respecter ma maquette.
frm_separation = Frame(frm_global, bg="#D5FEFF")
frm_separation.pack(padx=15, pady=15, fill=X, side=TOP)

dx=5 # horizontal
dy=5 # vertical

# Cette frame contient le tableau d'affichage des tuiles.
frm_game = Frame(frm_global, bg="#D5FEFF")
frm_game.pack(padx=10, pady=10, fill=X, side=LEFT)

frm_game2 = Frame(frm_global, bg="#FF8C75")
frm_game2.pack(padx=10, pady=10, fill=X, side=RIGHT)

frm_restart2 = Frame(frm_global, bg="#D5FEFF")
frm_restart2.pack(padx=10, pady=10, fill=X, side=TOP)

# Pour plus tard -> command=restart
btn_restart = Button(frm_restart2, text="Recommencer", bg="#26D91A", width=14, height=1, borderwidth=1, relief="solid", font=("Arial 25 bold"), fg="white", command=restart)
btn_restart.pack(side=BOTTOM)





# Ces boucles "for" servent à definir les grilles avec leurs bonnes couleurs.
for line in range(len(numbers)):
    frm_line = Frame(frm_game, bg="#5de1ff")
    frm_line.pack(fill=X)
    for col in range(len(numbers[line])):
        labels[line][col] = Label (frm_line,text =numbers[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial 15 bold"))
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)
for line in range(len(numbers2)):
    frm_line = Frame(frm_game2, bg="#FF8C75")
    frm_line.pack(fill=X)
    for col in range(len(numbers2[line])):
        labels2[line][col] = Label (frm_line,text =numbers2[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial 15 bold"))
        labels2[line][col].pack (side=LEFT, padx=dx,pady=dy)

# Ces appels de fonctions servent à faire apparaître dès le début de la partie 2 tuiles aléatoirement sur chacune des grilles.
random_function(numbers)
random_function(numbers)
random_function(numbers2)
random_function(numbers2)

window.bind("<Key>", key_pressed)
display_game()
window.mainloop()