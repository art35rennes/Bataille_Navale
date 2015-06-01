from tkinter import *

global n, fenetre, label_background

n = 0

def Suivant():

    global n, fenetre, label_background
    
    n = n + 1
    image_background = PhotoImage(file=(str("Tuto" + str(n) + ".png")))
    Fenetre()

def Precedent():

    global n, fenetre, label_background
    
    n = n - 1
    image_background = PhotoImage(file=(str("Tuto" + str(n) + ".png")))
    Fenetre()


def Fenetre():

    global n, fenetre, label_background

    try:
        fenetre.destroy()
    except:
        pass

            
    fenetre = Tk()
    fenetre.config(bg = "white")
    fenetre.resizable(width=False, height=False)

    image_background = PhotoImage(file=(str("Tuto" + str(n) + ".png")))

    print(image_background)

    w = image_background.width()
    h = image_background.height()

    fenetre.geometry("%dx%d+0+0" % (w + 30, h + 100))

    label_background = Label(fenetre, image=image_background)
    label_background.pack(side=TOP)
    

    button_suivant = Button(fenetre, text = "Suivant", command = Suivant, font="arial 12 bold",bg = "#AFCBE8")
    button_precedent = Button(fenetre, text = "Precedent", command = Precedent, font="arial 12 bold",bg = "#AFCBE8")

    button_suivant.pack(side = RIGHT, padx = 10, pady = 10)
    button_precedent.pack(side = RIGHT, padx = 10, pady = 10)

    fenetre.mainloop()

Fenetre()
