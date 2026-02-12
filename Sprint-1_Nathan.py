# Function : MA-20 | 2048
# author : Nathan
# Date : 05.02.2026
# Version : 1.0

from tkinter import *

############################ variables #################################

score = 0

# Tableau 2 dimensions des valeurs des tuiles.

# numbers= [[0, 0, 0, 0],
#          [0, 2, 0, 0],
#          [0, 0, 2, 0],
#          [0, 0, 0, 0],]

numbers= [[2, 4, 8, 16],
          [32, 64, 128, 256],
          [512, 1024, 2048, 4096],
          [8192, 0, 0, 0]]

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

# Cette fonction sert à afficher le jeu.
def display_game():
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if numbers[line][col] == 0:
                labels[line][col].config(text="")
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


display_game()
window.mainloop()