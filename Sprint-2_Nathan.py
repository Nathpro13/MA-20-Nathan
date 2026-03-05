# Function : MA-20 | 2048
# author : Nathan
# Date : 05.03.2026
# Version : 2.0

from tkinter import *

############################ variables #################################

score = 0
coups = 0

# Tableau 2 dimensions des valeurs des tuiles.

numbers= [[0, 0, 0, 0],
          [0, 2, 2, 0],
          [0, 2, 2, 0],
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

# Ces fonctions servent à fusionner. (j'ai déjà essayé de calculer le nombre de coups mais je n'y suis pas parvenu)

def right(coups):
    for line in range(4):
        (numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0]) = \
            pack4(numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0])
#    coups+=1
    display_game()
def left():
    for line in range(4):
        (numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3]) = \
            pack4(numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3])
    display_game()
def up():
    for col in range(4):
        (numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col]) = \
            pack4(numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col])
    display_game()
def down():
    for col in range(4):
        (numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col]) = \
            pack4(numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col])
    display_game()


# Cette fonction sert à écouter les touches.

def key_pressed(event) :
    print(coups)
    touche=event.keysym #récupérer le symbole de la touche
    if (touche=="Right" or touche=="d" or touche=="D"):
#        right(coups)
        right()
    if (touche=="Left" or touche=="a" or touche=="A"):
        left()
    if (touche=="Up" or touche=="w" or touche=="W"):
        up()
    if (touche=="Down" or touche=="s" or touche=="S"):
        down()

# Cette fonction sert à calculer les positions.

def pack4(a,b,c,d):
    if c==0:
        c,d = d,0
    if b==0:
        b,c,d = c,d,0
    if a==0:
        a,b,c,d = b,c,d,0

    if a==b:
        a,b,c,d = 2*a,c,d,0
    if b==c:
        b,c,d = 2*b,d,0
    if c==d:
        c,d = 2*c,0

    return a,b,c,d


# Cette fonction sert à afficher le jeu.
def display_game():
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if numbers[line][col] == 0:
                labels[line][col].config(text="", bg=colors[numbers[line][col]])
            else:
                labels[line][col].config(text=numbers[line][col], bg=colors[numbers[line][col]])


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