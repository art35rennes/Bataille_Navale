from tkinter import *
import socket, sys
from socket import gethostbyname_ex, gethostname
from threading import Thread
global role, iphost
import random
import os

def Redemarrage():
        global mysocket, fenetre

        try:
                mysocket.close()
        except:
                pass

        fenetre.destroy

        Mene_Principale()
                

def Tuto():
        
        os.startfile('Tutorial.pyw')


def Rejoindre(): #appeler par le bouton rejoindre
	
	global contre, role
	
	contre = "joueur"
	role = "client"
	
	
	fenetre_choix.destroy()
	
def connection(): #appeler par la fonction rejoindre quand on clic sur connection
	global fenetre_connection
	
	
	connectdata = (ip_serveur, port_serveur)
	
	fenetre_connection.destroy()


def Serveur(): #appeler par valider

	global HOST, iphost, fenetre_choix, contre, role, connectdata
	contre = "joueur"
	role = "hote"
	os.startfile('IP.pyw')
	
	fenetre_choix.destroy()
	
	

def Choix_IA():

	global fenetre_choix, contre, fenetre_IA
	
	contre = "IA"
	
	fenetre_choix.destroy()

	fenetre_IA = Tk()
	fenetre_IA.title("Choisissez un niveau d'IA")
	fenetre_IA.configure(bg = "#00B3D7")

	button_easy = Button(fenetre_IA, text = "Difficulté: Facile", font="arial 12 bold", relief=FLAT, bg = "white", command=niveaueasy)
	button_medium = Button(fenetre_IA, text = "Difficulté: Moyenne", font="arial 12 bold", relief=FLAT, bg = "white", command=niveaumedium)
	button_hard = Button(fenetre_IA, text = "Difficulté: Difficile", font="arial 12 bold", relief=FLAT, bg = "white", command=niveauhard)

	button_easy.pack(side=LEFT,padx=50,pady=10)
	button_medium.pack(side=LEFT,padx=50,pady=10)
	button_hard.pack(side=LEFT,padx=50,pady=10)



def niveaueasy(): # on sélectionne le niveau facile
	global niveau, fenetre_IA
	niveau = "easy"
	fenetre_IA.destroy()
	
def niveaumedium(): # on sélectionne le niveau moyen
	global niveau, fenetre_IA
	niveau = "medium"
	fenetre_IA.destroy()
	
def niveauhard(): # on sélectionne le niveau hard
	global niveau, fenetre_IA
	niveau = "hard"
	fenetre_IA.destroy()
	
def Menu_Principale():

        global fenetre_choix
        
        #Debut du programme

        fenetre_choix = Tk()
        fenetre_choix.title('Bataille Navale')
        fenetre_choix.resizable(width=False, height=False)
  
        # pick a .gif image file you have in the working directory
        image_background = PhotoImage(file="bg menu p.png")
        w = image_background.width()
        h = image_background.height()
  
        fenetre_choix.geometry("%dx%d+0+0" % (w, h))
  
        # tk.Frame has no image argument
        # so use a label as a panel/frame
        label_background = Label(fenetre_choix, image=image_background)
        label_background.pack(side='top', fill='both', expand='yes')
  
        button_heber = Button(label_background, text = " Heberger une partie ",command=Serveur,font="arial 16 bold",bg = "white", relief=FLAT)
        button_rej = Button(label_background, text = "Rejoindre une partie",command=Rejoindre,font="arial 16 bold", bg = "white", relief=FLAT)
        button_ia = Button(label_background, text = "   Jouer contre l'IA   ",command=Choix_IA,font="arial 16 bold",bg = "white", relief=FLAT)
        button_help = Button(label_background, text = "Comment jouer?",font="arial 16 bold",command = Tuto, bg = "white", relief=FLAT)


        button_heber.pack(side=TOP,padx=50,pady=10)
        button_rej.pack(side=TOP,padx=50,pady=10)
        button_ia.pack(side=TOP,padx=50,pady=10)
        button_help.pack(side=LEFT,padx=50,pady=10)

        fenetre_choix.mainloop()

Menu_Principale()

import tkinter as tk

if contre == "IA":
	
	


	fenetre = tk.Tk() #fenetre nécessaire pour variables objet
	fenetre.config(bg = "#1691BE")
	fenetre.resizable(width=False, height=False)
	
	
	imagedict = {"Fire": tk.PhotoImage(file="Bateau/Bang.gif"), "0Po[0, 1]": tk.PhotoImage(file="Bateau/0Po[0, 1].gif"), "1Po[0, 1]": tk.PhotoImage(file="Bateau/1Po[0, 1].gif"), "2Po[0, 1]": tk.PhotoImage(file="Bateau/2Po[0, 1].gif"), "3Po[0, 1]": tk.PhotoImage(file="Bateau/3Po[0, 1].gif"), "4Po[0, 1]": tk.PhotoImage(file="Bateau/4Po[0, 1].gif"), "0Po[1, 0]": tk.PhotoImage(file="Bateau/0Po[1, 0].gif"), "1Po[1, 0]": tk.PhotoImage(file="Bateau/1Po[1, 0].gif"), "2Po[1, 0]": tk.PhotoImage(file="Bateau/2Po[1, 0].gif"), "3Po[1, 0]": tk.PhotoImage(file="Bateau/3Po[1, 0].gif"), "4Po[1, 0]": tk.PhotoImage(file="Bateau/4Po[1, 0].gif"), "0Po[0, -1]": tk.PhotoImage(file="Bateau/0Po[0, -1].gif"), "1Po[0, -1]": tk.PhotoImage(file="Bateau/1Po[0, -1].gif"), "2Po[0, -1]": tk.PhotoImage(file="Bateau/2Po[0, -1].gif"), "3Po[0, -1]": tk.PhotoImage(file="Bateau/3Po[0, -1].gif"), "4Po[0, -1]": tk.PhotoImage(file="Bateau/4Po[0, -1].gif"), "0Po[-1, 0]": tk.PhotoImage(file="Bateau/0Po[-1, 0].gif"), "1Po[-1, 0]": tk.PhotoImage(file="Bateau/1Po[-1, 0].gif"), "2Po[-1, 0]": tk.PhotoImage(file="Bateau/2Po[-1, 0].gif"), "3Po[-1, 0]": tk.PhotoImage(file="Bateau/3Po[-1, 0].gif"), "4Po[-1, 0]": tk.PhotoImage(file="Bateau/4Po[-1, 0].gif"), "0Cr[0, 1]": tk.PhotoImage(file="Bateau/0Cr[0, 1].gif"), "1Cr[0, 1]": tk.PhotoImage(file="Bateau/1Cr[0, 1].gif"), "2Cr[0, 1]": tk.PhotoImage(file="Bateau/2Cr[0, 1].gif"), "3Cr[0, 1]": tk.PhotoImage(file="Bateau/3Cr[0, 1].gif"), "0Cr[1, 0]": tk.PhotoImage(file="Bateau/0Cr[1, 0].gif"), "1Cr[1, 0]": tk.PhotoImage(file="Bateau/1Cr[1, 0].gif"), "2Cr[1, 0]": tk.PhotoImage(file="Bateau/2Cr[1, 0].gif"), "3Cr[1, 0]": tk.PhotoImage(file="Bateau/3Cr[1, 0].gif"), "0Cr[0, -1]": tk.PhotoImage(file="Bateau/0Cr[0, -1].gif"), "1Cr[0, -1]": tk.PhotoImage(file="Bateau/1Cr[0, -1].gif"), "2Cr[0, -1]": tk.PhotoImage(file="Bateau/2Cr[0, -1].gif"), "3Cr[0, -1]": tk.PhotoImage(file="Bateau/3Cr[0, -1].gif"), "0Cr[-1, 0]": tk.PhotoImage(file="Bateau/0Cr[-1, 0].gif"), "1Cr[-1, 0]": tk.PhotoImage(file="Bateau/1Cr[-1, 0].gif"), "2Cr[-1, 0]": tk.PhotoImage(file="Bateau/2Cr[-1, 0].gif"), "3Cr[-1, 0]": tk.PhotoImage(file="Bateau/3Cr[-1, 0].gif"), "0So[0, 1]": tk.PhotoImage(file="Bateau/0So[0, 1].gif"), "1So[0, 1]": tk.PhotoImage(file="Bateau/1So[0, 1].gif"), "2So[0, 1]": tk.PhotoImage(file="Bateau/2So[0, 1].gif"), "0So[1, 0]": tk.PhotoImage(file="Bateau/0So[1, 0].gif"), "1So[1, 0]": tk.PhotoImage(file="Bateau/1So[1, 0].gif"), "2So[1, 0]": tk.PhotoImage(file="Bateau/2So[1, 0].gif"), "0So[0, -1]": tk.PhotoImage(file="Bateau/0So[0, -1].gif"), "1So[0, -1]": tk.PhotoImage(file="Bateau/1So[0, -1].gif"), "2So[0, -1]": tk.PhotoImage(file="Bateau/2So[0, -1].gif"), "0So[-1, 0]": tk.PhotoImage(file="Bateau/0So[-1, 0].gif"), "1So[-1, 0]": tk.PhotoImage(file="Bateau/1So[-1, 0].gif"), "2So[-1, 0]": tk.PhotoImage(file="Bateau/2So[-1, 0].gif"), "0Co[0, 1]": tk.PhotoImage(file="Bateau/0Co[0, 1].gif"), "1Co[0, 1]": tk.PhotoImage(file="Bateau/1Co[0, 1].gif"), "2Co[0, 1]": tk.PhotoImage(file="Bateau/2Co[0, 1].gif"), "0Co[1, 0]": tk.PhotoImage(file="Bateau/0Co[1, 0].gif"), "1Co[1, 0]": tk.PhotoImage(file="Bateau/1Co[1, 0].gif"), "2Co[1, 0]": tk.PhotoImage(file="Bateau/2Co[1, 0].gif"), "0Co[0, -1]": tk.PhotoImage(file="Bateau/0Co[0, -1].gif"), "1Co[0, -1]": tk.PhotoImage(file="Bateau/1Co[0, -1].gif"), "2Co[0, -1]": tk.PhotoImage(file="Bateau/2Co[0, -1].gif"), "0Co[-1, 0]": tk.PhotoImage(file="Bateau/0Co[-1, 0].gif"), "1Co[-1, 0]": tk.PhotoImage(file="Bateau/1Co[-1, 0].gif"), "2Co[-1, 0]": tk.PhotoImage(file="Bateau/2Co[-1, 0].gif"), "0To[0, 1]": tk.PhotoImage(file="Bateau/0To[0, 1].gif"), "1To[0, 1]": tk.PhotoImage(file="Bateau/1To[0, 1].gif"), "0To[1, 0]": tk.PhotoImage(file="Bateau/0To[1, 0].gif"), "1To[1, 0]": tk.PhotoImage(file="Bateau/1To[1, 0].gif"), "0To[0, -1]": tk.PhotoImage(file="Bateau/0To[0, -1].gif"), "1To[0, -1]": tk.PhotoImage(file="Bateau/1To[0, -1].gif"), "0To[-1, 0]": tk.PhotoImage(file="Bateau/0To[-1, 0].gif"), "1To[-1, 0]": tk.PhotoImage(file="Bateau/1To[-1, 0].gif")}
	
	#, "0To[-1, 0]": tk.PhotoImage(file="Bateau/0To[-1, 0].gif"), "1To[-1, 0]": tk.PhotoImage(file="Bateau/1To[-1, 0].gif")
	
		
	
	placepos = ""
	placeside = ""
	boatsize = ""
	boatname = ""
	postoplace = []
	posplaced = []
	selectedbonus = ""
	boats = {}
	
	bonuslist = ["Avion", "Radar", "Bombe", "Missile perforant"]
	
	bateauxlist = ["Porte-avion (5 cases)", "Croiseur (4 cases)", "Contre-torpilleur (3 cases)", "Sous-marin (3 cases)", "Torpilleur (2 cases)"]
	
	boatslefts = [boat[0:boat.index(" ")] for boat in bateauxlist]
	
	
	key = tk.StringVar()
	
	def onboatclick():
		global placeside, placepos, boatsize, boatname, postoplace, boatslefts, boats, imagedict
		
		postoplace = []
		
		if placepos != "" and placeside != "" and boatsize != "" and boatname in boatslefts:
			if placeside == "Left":
				placeside = [0, -1]
			if placeside == "Right":
				placeside = [0, 1]
			if placeside == "Up":
				placeside = [-1, 0]
			if placeside == "Down":
				placeside = [1, 0]
				
			
			
			maxpos = [int(placepos[0])+int(placeside[0])*int(boatsize), int(placepos[1])+int(placeside[1])*int(boatsize)]
			print(str(maxpos) + "=maxpos")
			if int(maxpos[0]) > 11 or int(maxpos[0]) < 0 or int(maxpos[1]) > 11 or int(maxpos[1]) < 0:
	
				return
			
			
			
			for changingpos in range(0, int(boatsize)):
				x = str(int(placepos[0]) + int(changingpos*placeside[0]))
				y = str(int(placepos[1]) + int(changingpos*placeside[1]))
				postoplace.append(str(x) + " " + str(y))
				
			
			
			
			for pos in postoplace:
				if pos in posplaced:
	
					return
			
			# Here boats can be placed
			
			
			
			
			boats[boatname] = list()
			
			
			for pos in postoplace:
				x = pos[0:pos.index(" ")]
				y = pos[pos.index(" "):]
			#	bateauquiflotte = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_rectangle(4,4,32,32, fill="blue")
			#	infodubateauquiflotte = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_text(18,18, text=str(postoplace.index(pos)) + str(boatname[0:2]) + str(placeside[:]))
				print(str(postoplace.index(pos)) + str(boatname[0:2]) + str(placeside[:]), "image", imagedict[str(str(postoplace.index(pos)) + str(boatname[0:2]) + str(placeside[:]))])
				imagedubatoquiflotte = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_image(18, 18, image=imagedict[str(postoplace.index(pos)) + str(boatname[0:2]) + str(placeside[:])]) # code image bato : morceau nom[0:2] côté
				grilledefense.grid_slaves(row=int(x), column=int(y))[0].unbind("<Key>")
				boats[boatname].append(pos)
				posplaced.append(pos)
				
			boatslefts.remove(boatname)
			selectedboatwidget.config(bg="light green")
			
			
			
			
			if boatslefts == []:
				grilleattaque.grid(row=1, column=2, padx=30, pady=5) # ici tous les bateaux sont placés
				initIA() # on est prêt, l'IA commence
			
	
	
	def boatsetter(event):
		global boatsize, boatname, selectedboatwidget
		selectedboatwidget = event.widget
		selectedboatwidget.focus_set()
		selectedboat = event.widget.itemcget(objet, "text")
		boatsize = selectedboat[selectedboat.index("(")+1]
		
		boatname = selectedboat[0:selectedboat.index(" ")]
		
		print(boatsize, boatname)
	
	def placesetter(event):
		global placepos, placeside
		placepos = event.widget.itemcget(pos, "text").split()
		placeside = event.keysym
		print(placeside)
		print(placepos)
		onboatclick()
	
	
	
	
	
	def shootedpossetter(event):
		global shootedpos	
		
	#	event.widget.unbind("<Button-1>")
		shootedpos = event.widget.itemcget(pos, "text")
		
		event.widget.focus_set()
		
		print(shootedpos)
		use(shootedpos)
	
	
	
	
	
	
	def use(shootedpos):
		
		x = shootedpos[0:shootedpos.index(" ")]
		y = shootedpos[shootedpos.index(" "):]	
		
		bateautouché = [key for key in BoatsIA if shootedpos in BoatsIA[key]]
		
		
		if bateautouché != []:
			BoatsIA[bateautouché[0]].remove(shootedpos)
		#	flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
			grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="red")
			if BoatsIA[bateautouché[0]] == []:
				modifyhistorique("Bateau ennemi " + bateautouché[0] + " coulé", "touché")
				BoatsIA.pop(bateautouché[0])
		else:
			grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="lightblue")
		
			
	
			
		if BoatsIA == {}:
			modifyhistorique("Vous avez gagné", "alert")
			historique.grab_set()
			return
		
		IA() # on a joué, a l'IA de jouer
		return
			
		
	
	def touchee(pos):
		x = pos[0:pos.index(" ")]
		y = pos[pos.index(" "):]
		flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
	
	
	
	def initIA():
		if niveau == "easy":
			global Grille, CoordGrille, Boat_found, Boat_direction, Boats_joueur, Toucher, nbtir, azerty, Grille_Tir, Boat_direction, Boats_joueur, Toucher,Croix, a_remove, Grande_Croix, Couler
	
			Grille = []
			for x in range (1,11):
				for y in range (1,11):
					CoordGrille = str(x) + " " + str(y)
					Grille.append(CoordGrille)
			print(Grille)
			Boat_found = "non"
			Boat_direction = "non"
			Boats_joueur = boats
			Toucher = 0
			nbtir = 0
			Placement_bateau()
		
		
		if niveau == "medium":
		#	global Grille, CoordGrille, Boat_found, Boats_joueur, Toucher, nbtir, Grille_Tir, nbcase, azerty
		
			Placement_bateau()
	
			Grille = []
			for x in range (1,11):
				for y in range (1,11):
					CoordGrille = str(x) + " " + str(y)
					#print(CoordTirIA)
					Grille.append(CoordGrille)
			Boat_found = "non"
			Boat_direction = "non"
			Boats_joueur = boats
			Toucher = 0
			nbtir = 0
			Grille_Tir = []
		
			for coord in Boats_joueur.values(): # On ajoute les coordonnées des navires ennemis dans la liste des possibilitées de tir
				print(coord)
				for rang in range (0,len(coord)):
					Grille_Tir.append(coord[rang])
					Grille.remove(coord[rang])
		
			print(" ")
			print(Grille_Tir)
			print(" ")
		
			for nbcase in range (0,random.randint(25,40)): # On ajoute un nombre aleatoire de cases d'eau (entre 25 et 40) dans la liste des possibilitées de tir
				azerty = random.choice(Grille)
				Grille.remove(azerty)
				Grille_Tir.append(azerty)
		
		if niveau == "hard":
		#	global Grille, CoordGrille, Boat_found, Boat_direction, Boats_joueur, Toucher,Croix, a_remove, Grande_Croix, Couler
			Grille = []
			for x in range (1,11): #Genere toute les coordonnees de la grille
				for y in range (1,11):
					CoordGrille = str(x) + " " + str(y)
					#																											   print(CoordTirIA)
					Grille.append(CoordGrille)
			print(Grille)
			Boat_found = 0
			Boat_direction = 0
			Boats_joueur = boats
			Toucher = 0
			Croix = []
			#																													   print(len(Croix))
			a_remove = []
			Couler = 0
			Grande_Croix = []
		
			Placement_bateau()
	
	def Placement_bateau():
		global BoatsIA
		
		composition = 0
	
		composition = random.randint(0,10)
		print(" ")
		print("composition " + str(composition))
		print(" ")
	
		if composition == 0:
			BoatsIA = {'Porte-avion': ['2 2', '2 3', '2 4', '2 5', '2 6'], 'Croiseur': ['3 8', '4 8', '5 8', '6 8'], 'Contre-torpilleur': ['4 5', '4 4', '4 3'], 'Torpilleur': ['8 8', '8 9'], 'Sous-marin': ['7 5', '8 5', '9 5']}
		elif composition == 1:
			BoatsIA = {'Contre-torpilleur': ['9 8', '9 9', '9 10'], 'Torpilleur': ['3 4', '3 3'], 'Croiseur': ['1 6', '1 5', '1 4', '1 3'], 'Porte-avion': ['3 8', '4 8', '5 8', '6 8', '7 8'], 'Sous-marin': ['6 4', '7 4', '8 4']}
		elif composition == 2:
			BoatsIA = {'Croiseur': ['4 5', '4 4', '4 3', '4 2'], 'Torpilleur': ['9 6', '10 6'], 'Contre-torpilleur': ['6 8', '7 8', '8 8'], 'Porte-avion': ['3 6', '3 7', '3 8', '3 9', '3 10'], 'Sous-marin': ['7 4', '7 3', '7 2']}
		elif composition == 3:
			BoatsIA = {'Sous-marin': ['7 3', '6 3', '5 3'], 'Contre-torpilleur': ['6 7', '5 7', '4 7'], 'Porte-avion': ['10 3', '10 4', '10 5', '10 6', '10 7'], 'Torpilleur': ['8 5', '7 5'], 'Croiseur': ['4 5', '3 5', '2 5', '1 5']}
		elif composition == 4:
			BoatsIA = {'Croiseur': ['7 1', '8 1', '9 1', '10 1'], 'Sous-marin': ['8 10', '9 10', '10 10'], 'Porte-avion': ['6 10', '5 10', '4 10', '3 10', '2 10'], 'Torpilleur': ['3 1', '2 1'], 'Contre-torpilleur': ['1 3', '1 4', '1 5']}
		elif composition == 5:
			BoatsIA = {'Sous-marin': ['3 5', '3 4', '3 3'], 'Contre-torpilleur': ['5 5', '6 5', '7 5'], 'Torpilleur': ['6 7', '6 8'], 'Croiseur': ['4 7', '4 8', '4 9', '4 10'], 'Porte-avion': ['5 3', '6 3', '7 3', '8 3', '9 3']}
		elif composition == 6:
			BoatsIA = {'Croiseur': ['3 6', '4 6', '5 6', '6 6'], 'Sous-marin': ['3 4', '4 4', '5 4'], 'Contre-torpilleur': ['3 5', '4 5', '5 5'], 'Torpilleur': ['3 3', '4 3'], 'Porte-avion': ['3 7', '4 7', '5 7', '6 7', '7 7']}
		elif composition == 7:
			BoatsIA = {'Sous-marin': ['1 1', '2 1', '3 1'], 'Croiseur': ['6 6', '6 5', '6 4', '6 3'], 'Porte-avion': ['9 9', '8 9', '7 9', '6 9', '5 9'], 'Torpilleur': ['9 3', '9 4'], 'Contre-torpilleur': ['2 7', '2 8', '2 9']}
		elif composition == 8:
			BoatsIA = {'Sous-marin': ['8 4', '8 5', '8 6'], 'Porte-avion': ['3 5', '3 6', '3 7', '3 8', '3 9'], 'Contre-torpilleur': ['6 6', '6 7', '6 8'], 'Croiseur': ['4 3', '5 3', '6 3', '7 3'], 'Torpilleur': ['8 9', '9 9']}
		else:
			Placement_bateau()
	
	
	def IA():
		fenetre.update()
		if niveau == "easy": # On choisit aléatoirement une case dans toute la grille
			global Grille, Coord_Tir, Grille_Tir
	
			Coord_Tir = random.choice(Grille)
			print("Tir aleat " + str(Coord_Tir))
			Grille.remove(Coord_Tir)
			Verif_joueur_toucher_easy_medium()
			
			
		if niveau == "medium": # On choisit une case parmi les navires ennemis et quelques cases d'eau
	
	
			Coord_Tir = random.choice(Grille_Tir)
			print("Tir aleat " + str(Coord_Tir))
			Grille_Tir.remove(Coord_Tir)
			Verif_joueur_toucher_easy_medium()
			
			
		if niveau == "hard":
			global Boat_found, Boat_direction, Premiere_touche, Croix, Deuxieme_Touche, Couler, Grande_Croix
	
	
		if Boat_found == 0: #Si aucun bateau n'a ete trouver
	
			Tir_aleat()
			Verif_joueur_toucher_hard()
	
		elif Boat_direction == 0: #Si un bateau a ete trouver mais que l'on ne connait sa direction
			
			Croix_de_tir()
			Coord_Tir = random.choice(Croix)
			Deuxieme_Touche = Coord_Tir
			print("Tir en " + str(Coord_Tir) + "^")
			Croix.remove(Coord_Tir)
			#																												   print(Croix)
			Verif_joueur_toucher_hard()
	
		else: #On termine de couler le navire ennemie
	
			#																												   print("len croix = " + str(len(Croix)))
			Generation_grande_croix()
			try:
				Coord_Tir = random.choice(Grande_Croix)
				Grande_Croix.remove(Coord_Tir)
				print("Tir en " + str(Coord_Tir))
				Verif_joueur_toucher_hard()
			except:
				Reset_IA_hard()
			
	
	def Croix_de_tir(): # La croix de tir correspond aux 4 cases qui entourent Premiere_touche 
	
		global Grille, Boat_found, Boat_direction, Premiere_touche, Croix, a_remove
	
		if niveau == "hard":
			if len(Croix) == 0 :
		
				a_remove = []
		
				x = Premiere_touche.split(" ",1)[0]
				y = Premiere_touche.split(" ",1)[1]
		
				xbis = int(x) + 1	
				Croix.append(str(xbis) + " " + str(y))
		
				xbis = int(x) - 1
				Croix.append(str(xbis) + " " + str(y))
		
				ybis = int(y) + 1
				Croix.append(str(x) + " " + str(ybis))
		
				ybis = int(y) - 1
				Croix.append(str(x) + " " + str(ybis))
		
				for nbcase in range(0,len(Croix)): #On verifie si les coordonnees genere sont encore disponible
		
					try:
						Grille.remove(Croix[nbcase])
					except:
						a_remove.append(Croix[nbcase]) #On stocke les coordonnes qui se trouve dans Croix mais pas dans Grille (elles ont deja ete tirer)
		
				#																												   print(a_remove)
				if len(a_remove) > 0:
					for nbcase in range (0,(len(a_remove)-1)):
		
						Croix.remove(a_remove[nbcase])
		
				#																												   print("Croix = " + str(Croix))				 
		
	
	
	def Generation_grande_croix(): #Il ne s'agit pas réellement d'une croix mais d'une ligne, on utilise toujours en case de reference Premiere_touche
								   #La ligne est horizontale ou verticale cela depend de Deuxieme_touche. Grande_Croix contient 7cases au maximum, case de reference +4 et -4
								   #exemple: Premiere_touche: "4 4" Deuxieme_touche: "4 5", le bateau est donc horizontale. Grande_Croix : "4 1", "4 2", "4 3", "4 6", "4 7", "4 8"
	
		global Grille, Boat_found, Boat_direction, Coord_Tir, Premiere_touche, Croix, Deuxieme_Touche, Grande_Croix
		if niveau == "hard":
			if len(Croix) > 0: #On reintegre les coordonnees restante dans Croix dans la Grille afin de pouvoir les reutiliser
					for nbcase in range (0,(len(Croix))):
						Grille.append(Croix[nbcase])
						
					#																											   print("croix = " + str(Croix))
					Croix = []
		
			x1 = Premiere_touche.split(" ",1)[0]
			y1 = Premiere_touche.split(" ",1)[1]
		
			x2 = Deuxieme_Touche.split(" ",1)[0]
			y2 = Deuxieme_Touche.split(" ",1)[1]
		
			x1=int(x1); y1=int(y1); x2=int(x2); y2=int(y2)
		
			#																													   print("len grande croix = " + str(len(Grande_Croix)))
			
			if len(Grande_Croix) == 0: #On ne regenre une liste que si elle vide ce qui n'arrive que suite a un reset
				if x1 - x2 == 0:
				   #																												print("je suis passer la ")
					for i in range (-4,5):
						if i != 110: #110 car avec 0 une erreur ce produisait, ce if est donc surement inutile
							#																									   print("						par la i=" + str(i))
							y1bis  = y1+i
							#																									   print("y1bis = " + str(y1))
							tempe = str(x1) + " " + str(y1bis)
							#print("tempe = " + str(tempe))
							Grande_Croix.append(tempe)
							try:
								Grille.remove(tempe); 
							except:
								Grande_Croix.remove(tempe)		   
				else:
					#																											   print("je suis passer la aussi ")
					for i in range (-4,5):
						if i != 110:
							#																									   print("						par la aussi i=" + str(i))
							x1bis  = x1+i
							#																									   print("y1bis = " + str(x1))
							tempe = str(x1bis+1) + " " + str(y1)
							#print("tempe = " + str(tempe))
							Grande_Croix.append(tempe)
							try:
								Grille.remove(tempe)
							except:
								Grande_Croix.remove(tempe)
			#																													   print("									Grande Croix = " + str(Grande_Croix))
		
		
	
	
	
		
	def Verif_joueur_toucher_easy_medium():
		global Grille, Boat_found, Boat_direction, Boats_joueur, Coord_Tir, Toucher, toucher, bateautouche
		
		if [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]] != []:
	
			print("										 **Bateau toucher"+ " " + Coord_Tir)
			touchee(Coord_Tir)
			bateautouche = [key for key in boats if Coord_Tir in boats[key]]
			boats[bateautouche[0]].remove(Coord_Tir)
			print("					   ^^ "+str(bateautouche))
	
			if boats[bateautouche[0]] == []:
				print("										 bateau coulé")
				print("					   // "+str(bateautouche))
				boats.pop(bateautouche[0])
				modifyhistorique("Bateau " + bateautouche[0] + " coulé", "coulé")
		else:
			print("										 dans l'eau")
		
		
		if boats == {}:
			modifyhistorique("Vous avez perdu", "alert")
			historique.grab_set()
	
	
	
		
	
	def Verif_joueur_toucher_hard(): #On verifie si on a toucher un navire ennemie et si il est couler
	
		"""
		Note a Leo: C'est surement dans cette fonction qu'il gerer la partie graphique de l'IA
		"""
	
		global Grille, Boat_found, Boat_direction, Boats_joueur, Coord_Tir, Toucher, toucher, bateautouche, Premiere_touche, Couler
		
		if [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]] != []:
			
			print("										 **Bateau toucher"+ " " + Coord_Tir)
			Toucher = Toucher + 1
			toucher = 1
			
			if Boat_found == 1:
				Boat_direction = 1
			
			Boat_found = 1
					   
			bateautouche = [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]]
			Boats_joueur[bateautouche[0]].remove(Coord_Tir)
			print("					   ^^ "+str(bateautouche))
			#																												   print("on est la")
	
			touchee(Coord_Tir)
	
			if Boats_joueur[bateautouche[0]] == []:
				print("										 bateau coulé")
				print("					   // "+str(bateautouche)+" coulé")
				Boats_joueur.pop(bateautouche[0])
				modifyhistorique("Bateau " + bateautouche[0] + " coulé", "coulé")
				Reset_IA_hard() #Si couler alors reset
				#																											   print("on est la2")
		else:
			print("										 dans l'eau")
			toucher = "non"
			#																												   print("on est la3")
			
			if boats == {}:
				modifyhistorique("Vous avez perdu !", "alert")
	def Tir_aleat(): #Choisie un lot de coordonnée parmit toute celle disponible dans Grille
	
	    global Grille, Coord_Tir, Premiere_touche, Croix
	
	    Coord_Tir = random.choice(Grille)
	    print("Tir aleat " + str(Coord_Tir))
	    Grille.remove(Coord_Tir)
	    Premiere_touche = Coord_Tir
	    Croix = []
	
	
	def Reset_IA_hard(): #Permet a l'IA de rapartire en tir aleatoire suite a une erreur ou un bateau ennemie couler
	
	    global Boat_found, Boat_direction, touche, Couler,Croix, Grande_Croix, a_remove
	
	    if len(Grande_Croix) > 0: #Les coordonnees n'ayant pas ete tirer dans la derniere phase de tir son reinserer dans la grille afin de pouvoir les reutiliser
	            for nbcase in range (0,(len(Grande_Croix))):
	                Grille.append(Grande_Croix[nbcase])
	
	    Toucher = 0
	    Croix = []
	    #                                                                                                                       print(len(Croix))
	    a_remove = []
	    Couler = 0
	    Grande_Croix = []
	    Boat_found = 0
	    Boat_direction = 0
	    print("                                                                               RESET")
	
	
	
	def modifyhistorique(string, tag=None): # on modifie l'historique (couleur en fonction de l'évènement)
				# définition des tags
			
		historique.tag_config("alert", background="red")
		historique.tag_config("warning", foreground="orange")
		historique.tag_config("info", foreground="blue")
		historique.tag_config("chat", foreground="green")
		historique.tag_config("touché", foreground="purple")
		historique.tag_config("coulé", foreground="grey")
			
			
		if string != "":	
			historique.config(state="normal")
			historique.insert("end", string + "\n", (tag))
			historique.see("end")
			historique.config(state="disabled")
		
	
	
	bateauxlist = ["Porte-avion (5 cases)", "Croiseur (4 cases)", "Contre-torpilleur (3 cases)", "Sous-marin (3 cases)", "Torpilleur (2 cases)"]
	
	boatslefts = [boatname[0:boatname.index(" ")] for boatname in [boat for boat in bateauxlist]]
	
	print("boatslefts", boatslefts)
	
	
	fenetre.title("Bataille-navale")

	bonus = tk.Canvas(fenetre, height = 300, width = 200, bg = "white")
	menu = tk.Canvas(bonus, bg="white", height=50, width=200)	
	text = menu.create_text(100,25, text="Menu principale", fill="red", font=("Purisa", 20))
	menu.config(bg="pink")	
	menu.bind("<Button-1>", Menu_Principale)		
	menu.grid(row=1)	
	bonus.grid(row=1, column=1, padx=10)
	
	
	bateaux = tk.Canvas(fenetre, height = 300, width = 200, bg = "white")
	
	for x in range(0, len(bateauxlist)+1):
		case = tk.Canvas(bateaux, bg="white", height=50, width=200)
		image = case.create_image(100,20)
		if x == 0:
			text = case.create_text(100,25, text="Bateaux :", fill="dark blue", font=("Purisa", 20))
			case.config(bg="azure2")
		elif x > 0:
			objet = case.create_text(100,25, text=str(bateauxlist[x-1]), state="")
			case.bind("<Button-1>", boatsetter)
		case.grid(row=x)
	
	bateaux.grid(row=2, column=1, padx=10)
	
	
	
	grilleattaque = tk.Canvas(fenetre, bg = "white")
	
	for x in range(1, 10+1):
		for y in range(1, 10+1):
		
			case = tk.Canvas(grilleattaque, bg="white", height=32, width=32)
		#	image = case.create_image(18,18)
			pos = case.create_text(18,18, text=str(x) + " " + str(y), state="hidden")
			case.bind("<Button-1>", shootedpossetter)
	   #	 case.bind("<Button-3>", onrightclick)
			case.grid(row=x, column=y)
	
	
	
	
	# grilleattaque.grid(row=1, column=2, padx=30, pady=5) # on attend que tous les bateaux soient placés pour l'afficher
	
		
	
	grilledefense = tk.Canvas(fenetre, bg = "white")
	
	for x in range(1, 10+1):
		for y in range(1, 10+1):
		
			case = tk.Canvas(grilledefense, bg="white", height=32, width=32)
		#	image = case.create_image(18,18)
			pos = case.create_text(18,18, text=str(x) + " " + str(y), state="hidden")
			case.bind("<Button-1>", lambda event: event.widget.focus_set())
			case.bind("<Key>", placesetter)
	   #	 case.bind("<Button-3>", onrightclick)
			case.grid(row=x, column=y)
	grilledefense.grid(row=2, column=2, padx=30, pady=5)
	
	
	
	historique = tk.Text(fenetre, bg="white", height=40, width=40)
	
	historique.config(state="disabled")
	
	historique.grid(column=3, row=1, rowspan=2, sticky="NS", pady=10, padx=10)
	

	fenetre.mainloop()



"""
#########################################################################################################################################################################################################################
"""






	


if contre == "joueur":
	
	
	import pickle
	
	profileasking = tk.Tk()
	profileasking.title("Make your profile !") 
	
	profiledict = {"username" : tk.StringVar(), "comment" : tk.StringVar(), "image" : ""}
	
	imagestring = ""
	
	
	def profileoutput(): # on sort le profil en sauvegarde
	
		global profiledict, imagestring
		
	#	profiledict["image"] = imagestring
		profiledict["username"] = usernameget.get()
		profiledict["comment"] = commentget.get()
		print(profiledict)
					
		profileasking.destroy()
	
	
	
	askusername = tk.Label(profileasking, text="Username")
	usernameget = tk.Entry(profileasking, textvariable=profiledict["username"], width=10)
	askcomment = tk.Label(profileasking, text="Comment")
	commentget = tk.Entry(profileasking, width=80)

	profilegetter = tk.Button(profileasking, text="I'm done !", command=profileoutput)
	
	askusername.grid(row=1, column=0)
	usernameget.grid(row=1, column=1)

	profilegetter.grid(row=4, column=0, columnspan=2)

	
	profileasking.mainloop()
	
		
		
	
	"""
	Fin partie profil
	"""
	
	
	# Fenêtre demande IP/PORT:
	
	demande = tk.Tk()
	demande.title("Entrez IP/Port (" + role + ")") # on demande 
	
	connectdata = (tk.StringVar(), tk.StringVar())
	
	# temporaire :
	connectdata[0].set("localhost") # temportaire
	connectdata[1].set("50000")
	
	def connexion():
		demande.destroy()
	
	askIP = tk.Label(demande, text="IP")
	IPget = tk.Entry(demande, textvariable=connectdata[0], width=15)
	askPort = tk.Label(demande, text="Port")
	Portget = tk.Entry(demande, textvariable=connectdata[1], width=5)
	Connectionbutton = tk.Button(demande, text="Connexion", command=connexion)
	
	askIP.grid(row=0, column=0)
	IPget.grid(row=0, column=1)
	askPort.grid(row=1, column=0)
	Portget.grid(row=1, column=1)
	Connectionbutton.grid(row=3, columnspan=2)
	
	
	demande.mainloop()
	
	print("ej contre joueur")
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	
	
	
	if role == "hote":
		print("je hote")
		# 2) liaison du socket à une adresse précise :
		try:
			mySocket.bind((connectdata[0].get(), int(connectdata[1].get())))
		except socket.error:
			print("La liaison du socket à l'adresse choisie a échoué.")
			sys.exit()
		
		# 3) Attente de la requête de connexion d'un client :
		print("Serveur prêt, en attente de requêtes ...")
		mySocket.listen(1)
		  
		# 4) Etablissement de la connexion :
			
		try:
			connexion, adresse = mySocket.accept()
			print("Client connecté, adresse IP " + str(adresse[0]) + " , port " + str(adresse[1]))
		
		except mySocket.error:
			pass
		
		
		# 5)a) Reception de message
		
		
		class update(Thread):
			def __init__(self):
				Thread.__init__(self)
		
		
			def run(self):
				"""Code à exécuter pendant l'exécution du thread.""" # ce code sera en permanence éxécuté en parallèle du reste du programme
				while True:
					try:
						msgClient = connexion.recv(1024) # on recoit le message
						if msgClient != "" and msgClient != b"":
							print("message de client", msgClient)
							paquethandler(msgClient) # on le gére
						if msgClient == b"":

							break
					except:
						pass
		
		
		updater = update()
		
		updater.start() # on démarre le thread
		
		
		
	if role == "client":
			
		# 2) Envoi d'une requête de connexion au serveur :
		try:
			mySocket.connect((connectdata[0].get(), int(connectdata[1].get())))
		except:
			print("La connexion a échoué.")
			sys.exit()	
		print("Connexion établie avec le serveur.")
		
		
		
		# 5)a) Réception de message
		
		
		class update(Thread):
			def __init__(self):
				Thread.__init__(self)
		
		
			def run(self):
				"""Code à exécuter pendant l'exécution du thread."""
				while On_continue == "oui":
					try:
						msgServeur = mySocket.recv(1024)
						if msgServeur != "" and msgServeur != b"":
							print("message de serv", msgServeur)
							paquethandler(msgServeur)
					except:
						pass
				
		
		
		updater = update()
		
		updater.start()
		
		
	
	"""
	Fin partie connection
	"""
	
		
	"""
	Insérer partie réseau
	"""
	
	
	# on affiche temporairement les paquets envoyés dans le widget "paquetdisplayer", en vert, ce qu'on envoie, en rouge, ce qu'on recoit
	
	
	def paquetsender(paquet):
		
		global role
		
		# on envoie le paquet pour pouvoir le gerer de l'autre côté
		
		if role == "hote":
			try:
				paquet = str(paquet + chr(0)).encode('latin-1') # on encode le paquet en bytes (encodage 'latin-1' qui supporte les accents)
				connexion.send(paquet)
			except:
				pass
				
				
		if role == "client":
			try:
				paquet = str(paquet + chr(0)).encode('latin-1')
				mySocket.send(paquet)
			except:
				pass
				
			# on sépare les paquets par un caractère relativement improbable (chr(0)) naturellement
				
				
		paquetdisplayer.insert("end", paquet.decode('latin-1') + "\n", "sended")
		
	
	
	
	
	def paquethandler(paquet):
		global dicoinfotir, usedbonus, enemyprofiledisplayer, enemyprofiledict
		
		paquet = paquet.decode('latin-1') # on décode le paquet en string
		
		if chr(0) in paquet:					# si par 'latence', on recoit plusieurs paquets collés, on les sépare
			paquetlist = paquet.split(chr(0))
		else:
			paquetlist = paquet
		
		for paquet in paquetlist:
	
			
			if paquet == "lancé": # le jeu est lancé chez l'adversaire, on peut lui envoyer le profil
				paquetsender("p" + str(profiledict))
			
			
			if paquet[0] == "g": # paquet lié au jeu
				paquet = paquet[1:]
				
				if paquet == "ready":
					modifyhistorique("Votre adversaire est prêt !", "info")
					unpause() # si l'adversaire est prêt, on peut jouer
					
					paquetdisplayer.insert("end", "ready" + "\n", "received")
					return
					
				if paquet == "perdu":
					modifyhistorique("Vous avez gagné", "info")
					
					pause() # pause définitive car jeu fini, mais possibilité de parler dans le chat
					
					return
				
				
				if paquet[0] == "{": # un bateau est coulé
					
					paquet = eval(paquet)
					
					for bateau in paquet:
						modifyhistorique("Bateau ennemi " + str(bateau) + " coulé", "touché")
					return
		
								
				if paquet[0] == "1": # étape 1
					
					paquet = paquet[1:]
					
					dicoinfotir = eval(paquet)
					
					
					print(dicoinfotir)
					
		#	ci-après : dicoinfotir -> dicopostouchées
					
					
					bateautouché = [key for key in boats if dicoinfotir["pos"] in boats[key]]
					
					
					if dicoinfotir["bonus"] == None:
						if bateautouché != []:
							
							touchee(dicoinfotir["pos"])
							
							paquetsender("g2" + str({dicoinfotir["pos"] : True}))
				
							paquetdisplayer.insert("end", "g2" + str({dicoinfotir["pos"] : True}) + "\n", "received")
		
			
							boats[bateautouché[0]].remove(dicoinfotir["pos"])
			
		
						
						
							if boats[bateautouché[0]] == []:
			
								boats.pop(bateautouché[0])
							
								paquetsender("g" + str({bateautouché[0] : "Coulé"}))
								
								modifyhistorique("Bateau " + str(bateautouché[0]) + " coulé", "coulé")
								
								paquetdisplayer.insert("end", "g" + str({bateautouché[0] : "Coulé"}) + "\n", "received")
					
					
					
						else:
						
							paquetsender("g2" + str({dicoinfotir["pos"] : False}))
				
							paquetdisplayer.insert("end","g2" + str({dicoinfotir["pos"] : False}) + "\n", "received")
				
		
				
					if dicoinfotir["bonus"] == "Avion":
			
						survolés = [str(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")]) + str(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):]), str(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")]) + dicoinfotir["direct"][0]) + " " + str(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):]) + dicoinfotir["direct"][1])]
					
						paquetsender("g2" + str({pos: pos in [pos for key in boats for pos in boats[key]] for pos in survolés}))
					
						paquetdisplayer.insert("end","g2" + str({pos: pos in [pos for key in boats for pos in boats[key]] for pos in survolés}) + "\n", "received")
			
						for pos in survolés:
						
							if pos in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]:
								bateautouché = [key for key in boats if pos in boats[key]]
						
							if bateautouché != []:
							
								boats[bateautouché[0]].remove(pos)
							
								touchee(pos)
			
								if boats[bateautouché[0]] == []:
									
									paquetsender("g" + str({bateautouché[0] : "Coulé"}))
									print("G COULEEEEE11")
									modifyhistorique("Bateau " + str(bateautouché[0]) + " coulé", "coulé")
									print("G COULEEEEE22")
							#		paquetdisplayer.insert("end","g" + str({bateautouché[0] : "Coulé"}) + "\n", "received")
									print("G COULEEEEE33")
									boats.pop(bateautouché[0])
									print("G COULEEEEE44")

									
									pass
				
				
				
					if dicoinfotir["bonus"] == "Radar":
					
						scannés = [item for item in [str(x) + " " + str(y) for x in range(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])-1, int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])+2) for y in range(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):])-1,int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]] + [str(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])-2) + " " + str(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):]))] + [str(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])+2) + " " + str(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):]))] + [str(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])) + " " + str(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):])-2)] + [str(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])) + " " + str(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):])+2)] if item in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
					
						paquetsender("g2" + str({pos: pos in [pos for key in boats for pos in boats[key]] for pos in scannés}))
			
						paquetdisplayer.insert("end","g2" + str({pos: pos in [pos for key in boats for pos in boats[key]] for pos in scannés}) + "\n", "received")
				
				
				
				
					if dicoinfotir["bonus"] == "Bombe":
						bombardés = [str(x) + " " + str(y) for x in range(int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])-1, int(dicoinfotir["pos"][0:dicoinfotir["pos"].index(" ")])+2) for y in range(int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):])-1,int(dicoinfotir["pos"][dicoinfotir["pos"].index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
					
			
						paquetsender("g2" + str({pos : pos in [pos for key in boats for pos in boats[key]] for pos in bombardés}))
			
						paquetdisplayer.insert("end","g2" + str({pos : pos in [pos for key in boats for pos in boats[key]] for pos in bombardés}) + "\n", "received")
					
					
						for pos in bombardés:
				
							bateautouché = [key for key in boats if pos in boats[key]]
							
							if bateautouché != []:
				
								boats[bateautouché[0]].remove(pos)
								
								touchee(pos)
								
								
								if boats[bateautouché[0]] == []:
				
									boats.pop(bateautouché[0])
									
									paquetsender("g" + str({bateautouché[0] : "Coulé"}))
									
									modifyhistorique("Bateau " + str(bateautouché[0]) + " coulé", "coulé")
									
									paquetdisplayer.insert("end","g" + str({bateautouché[0] : "Coulé"}) + "\n", "received")
					
					
					
					if dicoinfotir["bonus"] == "Missile perforant":
						
						paquetsender("g2" + str({dicoinfotir["pos"] : dicoinfotir["pos"] in [pos for key in boats for pos in boats[key]]}))
						
						paquetdisplayer.insert("end","g2" + str({dicoinfotir["pos"] : dicoinfotir["pos"] in [pos for key in boats for pos in boats[key]]}) + "\n", "received")
						
						if bateautouché != []:
							
							paquetsender("g" + str({bateautouché[0] : "Coulé"}))
							
							modifyhistorique("Bateau " + str(bateautouché[0]) + " coulé", "coulé")
							
							for pos in boats[bateautouché[0]]:
								touchee(pos)
							
							boats.pop(bateautouché[0])
					
					
					if boats == {}:
						modifyhistorique("Perdu, tous vos bateaux sont coulés !", "alert")
						paquetsender("g" + "perdu")
						
						paquetdisplayer.insert("end","g" + "perdu" + "\n", "received")
					
						pause() # pause définitive car jeu fini, mais possibilité de parler dans le chat
						
						return # la réponse conduit a la fin du jeu alors on sort de la boucle
						
					unpause() # on a répondu on peut jouer
					modifyhistorique("A vous de jouer", "info")
					
		#	fin ci-après
			
				if paquet[0] == "2": # étape 2 essentiellement retour graphique et passtontournoob (voire mettre le passtontournoob direct apres l'envoi du paquet)
					
					
					print(usedbonus, "USEDBONUS")
					
					paquet = paquet[1:]
					
					dictreponse = eval(paquet)
					
					
					print(dictreponse, "DICTREPONSE")
					
					
					
					
					
					if usedbonus == None:
						for pos in dictreponse:
							
							
							
							print(pos, "POS")
							
							
							x = pos[0:pos.index(" ")]
							y = pos[pos.index(" "):]
							if dictreponse[pos]:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="red")
							else:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="light blue")
								
					if usedbonus == "Avion":
						for pos in dictreponse:
							print(pos,"POS")
							x = pos[0:pos.index(" ")]
							y = pos[pos.index(" "):]
							if dictreponse[pos]:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="red")
							else:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="light blue")
													
					if usedbonus == "Bombe":
						if True in dictreponse.values():
							for pos in dictreponse:
								print(pos,"POS")
								x = pos[0:pos.index(" ")]
								y = pos[pos.index(" "):]
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="hot pink")
						else:
							for pos in dictreponse:
								x = pos[0:pos.index(" ")]
								y = pos[pos.index(" "):]
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="light blue")
								
					if usedbonus == "Radar":
						for pos in dictreponse:
							print(pos,"POS")
							x = pos[0:pos.index(" ")]
							y = pos[pos.index(" "):]
							if dictreponse[pos]:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="light green")
							else:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="light blue")
					
					if usedbonus == "Missile perforant":
						for pos in dictreponse:
							
							print(pos,"POS")
							
							x = pos[0:pos.index(" ")]
							y = pos[pos.index(" "):]
							if dictreponse[pos]:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="dark red")
							else:
								grilleattaque.grid_slaves(row=int(x), column=int(y))[0].config(bg="light blue")
				
					
					pass
				
				pass
				
				"""
				format d'un paquet jeu :
				
				
				2 étapes :
					- paquet[0] = "1" si étape 1 : on envoie les infos du tir et on traite de l'autre côté les coordonnées du tir
					
						{bonus:selectedbonus, pos:shootedpos} (bonus = None si pas de bonus sélectionné)
					
					- paquet[0] = "2" si étape 2 : on recoit le dictionnaire du résultat du tir et on affiche les résultat
				
						{pos for pos in postouchées : boléen} (postouchées = liste des positions affectées par le tir, boléen = True si bateau False sinon)
				
				OU
				
				"ready" (le joueur adverse à placé ses bateaux)
				
				OU
				
				"perdu" (le joueur adverse à perdu)
				"""
				
			if paquet[0] == "c": # paquet lié au chat
				paquet = paquet[1:]
				
				
				modifyhistorique(" << " + paquet, "chatrecu")
				
				
				
				pass
				
				"""
				format d'un paquet chat : 
				"message"
				"""
				
			if paquet[0] == "p": # paquet lié au profil
				
				
				
				paquet = paquet[1:]
				
				
				enemyprofiledict = eval(paquet)
				
				print("JAI LE PROFIL", enemyprofiledict)
				
				
				enemyprofiledisplayer = tk.Canvas(fenetre, bg="red", height=200, width=300)
							
				enemyusernamedisplayer = enemyprofiledisplayer.create_text(150,20, text=enemyprofiledict["username"], font=("Ubuntu", 20), fill="dark red")
				
				enemyprofileimage = tk.PhotoImage(data=enemyprofiledict["image"])
				
				enemyprofileimagedisplayer = enemyprofiledisplayer.create_image(150,100, image=enemyprofileimage)
				
				
				enemyprofiledisplayer.grid(column=4, row=2, rowspan=2, padx=10, sticky="S")
				
				
				print("normalement affiche")
				
				
				pass
				
				"""
				format d'un paquet profil :
				dictionnaire (image encodée en base64; pseudo = None ou image = None si pas selectionnée) (/!\ ne contiendra peut-être que le pseudo)
				"""
		
	
	"""
	Fin partie réseau
	"""
	
	
	
	
	"""
	Début sélection bonus
	"""
	
	asking = tk.Tk()
	asking.title("Bonus")
	
	
	bonuslist = ["Avion", "Radar", "Bombe", "Missile perforant"]
	bonusdict = {"Avion": tk.IntVar(), "Radar": tk.IntVar(), "Bombe": tk.IntVar(), "Missile perforant": tk.IntVar()}
	bonuscost = {"Avion": 3, "Radar": 5, "Bombe": 9, "Missile perforant": 5}
	points = 30
	pointsleft = tk.IntVar()
	pointsleft.set(points)
	

	
	
	def ready():
		
		for bonus in bonusdict:
			bonusdict[bonus] = bonusdict[bonus].get()
	
		
		print(bonusdict)
		
		
		asking.destroy() # on passe à la suite
		
	
	
	
	def update(event):
		# 1. On prend l'action (+ ou -)
		# 2. On trouve quel bonus concerné
		# 3. On fait l'action si possible et on change les points
		
				
		
		todo = event.widget.cget("text")
		selectedbonus = asking.grid_slaves(row=event.widget.grid_info()["row"], column=0)[0].cget("text")
		print(event.widget.grid_info()["row"])
		print(todo)
		print(selectedbonus)
	
	
		if todo == "+":
			if pointsleft.get() >= bonuscost[selectedbonus]:
				pointsleft.set(pointsleft.get() - bonuscost[selectedbonus])
				bonusdict[selectedbonus].set(bonusdict[selectedbonus].get() + 1)
			pass
		
		
		if todo == "-":
			if bonusdict[selectedbonus].get() > 0:
				pointsleft.set(pointsleft.get() + bonuscost[selectedbonus])
				bonusdict[selectedbonus].set(bonusdict[selectedbonus].get() - 1)
			pass
		
		
		displaypoint.config(text="Points left = "+ str(pointsleft.get()))
		
	
	
	for bonus in bonusdict: # on fait la même chose pour tous les bonus
		text = tk.Label(asking, text=bonus)
		value = tk.Label(asking, textvariable=bonusdict[bonus])
		buttonplus = tk.Label(asking, text="+", font=("Arial", 20))
		buttonmoins = tk.Label(asking, text="-", font=("Arial", 20))
		buttonplus.bind("<Button-1>", update)
		buttonmoins.bind("<Button-1>", update)
		text.grid(row=bonuslist.index(bonus), column=0) # placement relatif au nombre de bonus
		buttonplus.grid(row=bonuslist.index(bonus), column=3)
		value.grid(row=bonuslist.index(bonus), column=2)
		buttonmoins.grid(row=bonuslist.index(bonus), column=1)
	
	
	
	
	displaypoint = tk.Label(asking, text="Points left = "+ str(points))
	displaypoint.grid(columnspan=4, row=len(bonuslist))
	
	button = tk.Button(asking, text="Ready", command=ready)
	button.grid(columnspan=4, row=len(bonuslist)+1)
	
	
	asking.mainloop()
	
	
	"""
	Fin partie selection bonus
	"""
	
		
	
	"""
	Début du jeu :P
	"""
	
	
	
	
	fenetre = tk.Tk() #fenetre nécessaire pour variables objet
	fenetre.config(bg = "#1691BE")
	fenetre.resizable(width=False, height=False)
	
	
	imagedict = {"Fire": tk.PhotoImage(file="Bateau/Bang.gif"), "0Po[0, 1]": tk.PhotoImage(file="Bateau/0Po[0, 1].gif"), "1Po[0, 1]": tk.PhotoImage(file="Bateau/1Po[0, 1].gif"), "2Po[0, 1]": tk.PhotoImage(file="Bateau/2Po[0, 1].gif"), "3Po[0, 1]": tk.PhotoImage(file="Bateau/3Po[0, 1].gif"), "4Po[0, 1]": tk.PhotoImage(file="Bateau/4Po[0, 1].gif"), "0Po[1, 0]": tk.PhotoImage(file="Bateau/0Po[1, 0].gif"), "1Po[1, 0]": tk.PhotoImage(file="Bateau/1Po[1, 0].gif"), "2Po[1, 0]": tk.PhotoImage(file="Bateau/2Po[1, 0].gif"), "3Po[1, 0]": tk.PhotoImage(file="Bateau/3Po[1, 0].gif"), "4Po[1, 0]": tk.PhotoImage(file="Bateau/4Po[1, 0].gif"), "0Po[0, -1]": tk.PhotoImage(file="Bateau/0Po[0, -1].gif"), "1Po[0, -1]": tk.PhotoImage(file="Bateau/1Po[0, -1].gif"), "2Po[0, -1]": tk.PhotoImage(file="Bateau/2Po[0, -1].gif"), "3Po[0, -1]": tk.PhotoImage(file="Bateau/3Po[0, -1].gif"), "4Po[0, -1]": tk.PhotoImage(file="Bateau/4Po[0, -1].gif"), "0Po[-1, 0]": tk.PhotoImage(file="Bateau/0Po[-1, 0].gif"), "1Po[-1, 0]": tk.PhotoImage(file="Bateau/1Po[-1, 0].gif"), "2Po[-1, 0]": tk.PhotoImage(file="Bateau/2Po[-1, 0].gif"), "3Po[-1, 0]": tk.PhotoImage(file="Bateau/3Po[-1, 0].gif"), "4Po[-1, 0]": tk.PhotoImage(file="Bateau/4Po[-1, 0].gif"), "0Cr[0, 1]": tk.PhotoImage(file="Bateau/0Cr[0, 1].gif"), "1Cr[0, 1]": tk.PhotoImage(file="Bateau/1Cr[0, 1].gif"), "2Cr[0, 1]": tk.PhotoImage(file="Bateau/2Cr[0, 1].gif"), "3Cr[0, 1]": tk.PhotoImage(file="Bateau/3Cr[0, 1].gif"), "0Cr[1, 0]": tk.PhotoImage(file="Bateau/0Cr[1, 0].gif"), "1Cr[1, 0]": tk.PhotoImage(file="Bateau/1Cr[1, 0].gif"), "2Cr[1, 0]": tk.PhotoImage(file="Bateau/2Cr[1, 0].gif"), "3Cr[1, 0]": tk.PhotoImage(file="Bateau/3Cr[1, 0].gif"), "0Cr[0, -1]": tk.PhotoImage(file="Bateau/0Cr[0, -1].gif"), "1Cr[0, -1]": tk.PhotoImage(file="Bateau/1Cr[0, -1].gif"), "2Cr[0, -1]": tk.PhotoImage(file="Bateau/2Cr[0, -1].gif"), "3Cr[0, -1]": tk.PhotoImage(file="Bateau/3Cr[0, -1].gif"), "0Cr[-1, 0]": tk.PhotoImage(file="Bateau/0Cr[-1, 0].gif"), "1Cr[-1, 0]": tk.PhotoImage(file="Bateau/1Cr[-1, 0].gif"), "2Cr[-1, 0]": tk.PhotoImage(file="Bateau/2Cr[-1, 0].gif"), "3Cr[-1, 0]": tk.PhotoImage(file="Bateau/3Cr[-1, 0].gif"), "0So[0, 1]": tk.PhotoImage(file="Bateau/0So[0, 1].gif"), "1So[0, 1]": tk.PhotoImage(file="Bateau/1So[0, 1].gif"), "2So[0, 1]": tk.PhotoImage(file="Bateau/2So[0, 1].gif"), "0So[1, 0]": tk.PhotoImage(file="Bateau/0So[1, 0].gif"), "1So[1, 0]": tk.PhotoImage(file="Bateau/1So[1, 0].gif"), "2So[1, 0]": tk.PhotoImage(file="Bateau/2So[1, 0].gif"), "0So[0, -1]": tk.PhotoImage(file="Bateau/0So[0, -1].gif"), "1So[0, -1]": tk.PhotoImage(file="Bateau/1So[0, -1].gif"), "2So[0, -1]": tk.PhotoImage(file="Bateau/2So[0, -1].gif"), "0So[-1, 0]": tk.PhotoImage(file="Bateau/0So[-1, 0].gif"), "1So[-1, 0]": tk.PhotoImage(file="Bateau/1So[-1, 0].gif"), "2So[-1, 0]": tk.PhotoImage(file="Bateau/2So[-1, 0].gif"), "0Co[0, 1]": tk.PhotoImage(file="Bateau/0Co[0, 1].gif"), "1Co[0, 1]": tk.PhotoImage(file="Bateau/1Co[0, 1].gif"), "2Co[0, 1]": tk.PhotoImage(file="Bateau/2Co[0, 1].gif"), "0Co[1, 0]": tk.PhotoImage(file="Bateau/0Co[1, 0].gif"), "1Co[1, 0]": tk.PhotoImage(file="Bateau/1Co[1, 0].gif"), "2Co[1, 0]": tk.PhotoImage(file="Bateau/2Co[1, 0].gif"), "0Co[0, -1]": tk.PhotoImage(file="Bateau/0Co[0, -1].gif"), "1Co[0, -1]": tk.PhotoImage(file="Bateau/1Co[0, -1].gif"), "2Co[0, -1]": tk.PhotoImage(file="Bateau/2Co[0, -1].gif"), "0Co[-1, 0]": tk.PhotoImage(file="Bateau/0Co[-1, 0].gif"), "1Co[-1, 0]": tk.PhotoImage(file="Bateau/1Co[-1, 0].gif"), "2Co[-1, 0]": tk.PhotoImage(file="Bateau/2Co[-1, 0].gif"), "0To[0, 1]": tk.PhotoImage(file="Bateau/0To[0, 1].gif"), "1To[0, 1]": tk.PhotoImage(file="Bateau/1To[0, 1].gif"), "0To[1, 0]": tk.PhotoImage(file="Bateau/0To[1, 0].gif"), "1To[1, 0]": tk.PhotoImage(file="Bateau/1To[1, 0].gif"), "0To[0, -1]": tk.PhotoImage(file="Bateau/0To[0, -1].gif"), "1To[0, -1]": tk.PhotoImage(file="Bateau/1To[0, -1].gif"), "0To[-1, 0]": tk.PhotoImage(file="Bateau/0To[-1, 0].gif"), "1To[-1, 0]": tk.PhotoImage(file="Bateau/1To[-1, 0].gif")}
	
	
	placepos = ""
	placeside = ""
	boatsize = ""
	boatname = ""
	postoplace = []
	posplaced = []
	selectedbonus = ""
	boats = {}
	
	bonuslist = ["Avion", "Radar", "Bombe", "Missile perforant"]
	
	bateauxlist = ["Porte-avion (5 cases)", "Croiseur (4 cases)", "Contre-torpilleur (3 cases)", "Sous-marin (3 cases)", "Torpilleur (2 cases)"]
	
	boatslefts = [boat[0:boat.index(" ")] for boat in bateauxlist]
	
	
	key = tk.StringVar()
	
	def onboatclick():
		global placeside, placepos, boatsize, boatname, postoplace, boatslefts, boats
		
		postoplace = []
		
		if placepos != "" and placeside != "" and boatsize != "" and boatname in boatslefts: # si toutes les conditions sont réunies (on a bato + côté + taille + bato pas encore placé)
			if placeside == "Left":
				placeside = [0, -1]
			if placeside == "Right":
				placeside = [0, 1]
			if placeside == "Up":
				placeside = [-1, 0]
			if placeside == "Down":
				placeside = [1, 0]
				
			
			
			maxpos = [int(placepos[0])+int(placeside[0])*int(boatsize), int(placepos[1])+int(placeside[1])*int(boatsize)] # on voit jusqu'où le bateau va aller
			print(str(maxpos) + "=maxpos")
			if int(maxpos[0]) > 11 or int(maxpos[0]) < 0 or int(maxpos[1]) > 11 or int(maxpos[1]) < 0:
				modifyhistorique("Bateau hors de la grille", "warning")
				return
			
			
			
			for changingpos in range(0, int(boatsize)):
				x = str(int(placepos[0]) + int(changingpos*placeside[0]))
				y = str(int(placepos[1]) + int(changingpos*placeside[1]))
				postoplace.append(str(x) + " " + str(y)) # liste des pos a placer
				
			
			
			
			for pos in postoplace:
				if pos in posplaced:
					modifyhistorique("Case déja utilisée !", "warning")
					return
			
			# les bateaux sont dans la grille et n'occupent pas de place déja utilisé
			
						
			
			boats[boatname] = list() # on initialise la liste
			
			
			for pos in postoplace:
				x = pos[0:pos.index(" ")]
				y = pos[pos.index(" "):]
				imagedubatoquiflotte = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_image(18, 18, image=imagedict[str(postoplace.index(pos)) + str(boatname[0:2]) + str(placeside[:])]) # code image bato : morceau nom[0:2] côté
				grilledefense.grid_slaves(row=int(x), column=int(y))[0].unbind("<Key>")
				boats[boatname].append(pos) # on remplit la liste du bateau
				posplaced.append(pos) # et celle des pos placées
				
			boatslefts.remove(boatname) # on a plus besoin de placer le bateau
			selectedboatwidget.config(bg="light green") # on affiche que le bateau est placé
			print(boats)
			
			
			
			
			if boatslefts == []:
				grilleattaque.grid(row=1, column=2, padx=30, pady=5) # ici tous les bateaux sont placés
				pause() # on se met en attente de l'autre joueur
	#			modifyhistorique("A l'adversaire de jouer", "info")
				paquetsender("gready") # on dit à l'autre joueur qu'on est prêt
			
	
	
	def boatsetter(event): # on prend toutes les caractéristiques du bateau
		global boatsize, boatname, selectedboatwidget
		selectedboatwidget = event.widget
		selectedboatwidget.focus_set()
		selectedboat = event.widget.itemcget(objet, "text") # on prend le texte du bateau
		boatsize = selectedboat[selectedboat.index("(")+1] # on en ressort la taille
		
		boatname = selectedboat[0:selectedboat.index(" ")]
		
		print(boatsize, boatname)
	
	def placesetter(event): # quand on appuie sur une touche du clavier avec le focus sur une case de la grille de placement
		global placepos, placeside
		placepos = event.widget.itemcget(pos, "text").split()
		placeside = event.keysym # on prend la touche utilisée
		print(placeside)
		print(placepos)
		onboatclick() # on va placer le bateau
	
	
	
	
	
	def shootedpossetter(event): # quand on clique sur une case de la grille d'attaque
		global shootedpos	
		
	#	event.widget.unbind("<Button-1>")
		shootedpos = event.widget.itemcget(pos, "text")
		
		event.widget.focus_set() # on la met en valeur (comme ca on peut diriger l'avion aussi)
		
		print(shootedpos)
		use(shootedpos)
	
	
	
	
	
	
	def use(shootedpos): # on transforme le tir en paquet à envoyer
	#	global paused
		
	#	if paused == True:
	#		return
		
		
		global usedbonus, selectedbonus
		
	
		usedbonus = selectedbonus
		if usedbonus == "":
			usedbonus = None
		
			
		x = shootedpos[0:shootedpos.index(" ")]
		y = shootedpos[shootedpos.index(" "):]	
			
		
		if selectedbonus != "":
			if bonusdict[selectedbonus] == 0:
				selectedbonus = ""
				return
			
		
			# ici, on a shootedpos et selectedbonus SAUF AVION !!!
			
				
		""" 1) """
		if selectedbonus != bonuslist[0]:
			paquetsender("g1" + str({"bonus":[None if selectedbonus == "" else selectedbonus][0] , "pos":shootedpos}))
		
		
		
		#
		# [pos for key in boats for pos in boats[key]] => liste des position de toutes les cases de tous les bateaux
		#
		# ^ pas besoin (en fait si)
		#
		#
		#
		# [key for key in boats if shootedpos in boats[key]] => liste du bateau touché par shootedpos (attention: peut être vide)
		#
		# ^ = bateautouché (self-explainatory)
		#
		#
		#
		# [str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
		#
		# ^ = bombardés (cases touchées par bombe dans la grille)
		#
		# 
		# set([str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]).intersection([pos for key in boats for pos in boats[key]])
		# 
		# ^ = explosés (bateaux touchés par la bombe)
		#
		#
		# [str(shootedpos[0:shootedpos.index(" ")]) + str(shootedpos[shootedpos.index(" "):]), str(int(shootedpos[0:shootedpos.index(" ")]) + direction[0]) + " " + str(int(shootedpos[shootedpos.index(" "):]) + direction[1])]
		#
		# ^ = survolés (positions survolées par l'avion)
		#
		# [item for item in [str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]] + [str(int(shootedpos[0:shootedpos.index(" ")])-2) + " " + str(int(shootedpos[shootedpos.index(" "):]))] + [str(int(shootedpos[0:shootedpos.index(" ")])+2) + " " + str(int(shootedpos[shootedpos.index(" "):]))] + [str(int(shootedpos[0:shootedpos.index(" ")])) + " " + str(int(shootedpos[shootedpos.index(" "):])-2)] + [str(int(shootedpos[0:shootedpos.index(" ")])) + " " + str(int(shootedpos[shootedpos.index(" "):])+2)] if item in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
		# 
		# ^ = scannés (positions dans le radar)
		#
	
				
		
		if selectedbonus == bonuslist[0]:
			
			
			
			
			grilleattaque.grid_slaves(row=int(x), column=int(y))[0].grab_set()
			grilleattaque.grid_slaves(row=int(x), column=int(y))[0].bind("<Key>", lambda event: key.set(event.keysym))
			grilleattaque.grid_slaves(row=int(x), column=int(y))[0].unbind("<Button-1>")
					
		#	paused = True
			
			grilleattaque.grid_slaves(row=int(x), column=int(y))[0].wait_variable(key)
			
			
			grilleattaque.grid_slaves(row=int(x), column=int(y))[0].grab_release()
			
			grilleattaque.grid_slaves(row=int(x), column=int(y))[0].bind("<Button-1>", shootedpossetter)
			
			if key.get() not in ["Left", "Up", "Down", "Right"]:
				selectedbonus = ""
				return
				
		#	paused = False
			
			direction = ""
			
					
			
			if key.get() == "Left":
				direction = [0, -1]
			if key.get() == "Right":
				direction = [0, 1]
			if key.get() == "Up":
				direction = [-1, 0]
			if key.get() == "Down":
				direction = [1, 0]
				
			# ici on a tous ce qu'il faut pour l'avion
			
			
			
			paquetsender("g1" + str({"bonus":[None if selectedbonus == "" else selectedbonus][0] , "pos":shootedpos, "direct":direction}))
			
		for bonus in bonusdict:
			if bonus == selectedbonus:
				bonusdict[selectedbonus] = bonusdict[selectedbonus] - 1
				
		if selectedbonus != "":
			selectedbonuswidget.itemconfig(objet, text=str(selectedbonus) + " (" + str(bonusdict[selectedbonus]) + " restants)")


		
		selectedbonus = ""
		pause() # on a joué, on se met en pause
		modifyhistorique("A l'adversaire de jouer", "info")
		return
			
			
			
			
	def touchee(pos): # on met une image sur les pos touchées
		x = pos[0:pos.index(" ")]
		y = pos[pos.index(" "):]
		flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
	
	
	
	
	
	
	
	def sendmessage(event): # on envoie un message dans le chat (et on l'affiche)
		if event.widget.get() != "" and len(event.widget.get()) < 100:
			messageaenvoyer = event.widget.get()
			event.widget.delete(0, "end")
			modifyhistorique(" >> " + messageaenvoyer, "chatenvoye")
			paquetsender("c" + messageaenvoyer)
		
		if len(event.widget.get()) >= 100:
			event.widget.delete(0, "end")
		
	
	
	def modifyhistorique(string, tag=None): # on modifie l'historique (couleur en fonction de l'évènement)
				# définition des tags
			
		historique.tag_config("alert", background="red")
		historique.tag_config("warning", foreground="orange")
		historique.tag_config("info", foreground="blue")
		historique.tag_config("chatrecu", foreground="dark green")
		historique.tag_config("chatenvoye", foreground="green")
		historique.tag_config("touché", foreground="purple")
		historique.tag_config("coulé", foreground="grey")
			
			
		if string != "":	
			historique.config(state="normal")
			historique.insert("end", string + "\n", (tag))
			historique.see("end")
			historique.config(state="disabled")
	
	
	def bonussetter(event): # on sauvegarde le bonus selectionné
		global selectedbonus
		
		global selectedbonuswidget
		
		selectedbonuswidget = event.widget
		selectedbonuswidget.focus_set()
		selectedbonus = event.widget.itemcget(objet, "text")
		selectedbonus = selectedbonus[0:selectedbonus.index("(")-1]
		print(selectedbonus)
		print(bonus)
		
	
	def pause(): # pause : on force les évènements à aller dans le chat
		chat.grab_set()
	
	def unpause(): # on libère les évènements
		chat.grab_release()
	
	
	
	"""
	Partie graphique
	"""
	
	
	fenetre.title("Bataille-navale")
	
	bonus = tk.Canvas(fenetre, height = 300, width = 200, bg = "white")
	
	for x in range(0, len(bonuslist)+1):
		case = tk.Canvas(bonus, bg="white", height=50, width=200)
	#	image = case.create_image(100,20)
		if x == 0:
			text = case.create_text(100,25, text="Bonus :", fill="red", font=("Purisa", 20))
			case.config(bg="pink")
		elif x > 0:
			objet = case.create_text(100,25, text=str(bonuslist[x-1]) + " (" + str(bonusdict[bonuslist[x-1]]) + " restants)", tags=str(bonuslist[x-1]))
			case.bind("<Button-1>", bonussetter)
		#   case.bind("<Button-3>", onrightclick)
			print(case.gettags(bonuslist[x-1]))
			print(bonuslist[x-1])
		
		
			
		case.grid(row=x)
		
	
	bonus.grid(row=1, column=1, padx=10)
	
	bonuswidget = bonus
		
	bateaux = tk.Canvas(fenetre, height = 300, width = 200, bg = "white")
	
	for x in range(0, len(bateauxlist)+1):
		case = tk.Canvas(bateaux, bg="white", height=50, width=200)
	#	image = case.create_image(100,20)
		if x == 0:
			text = case.create_text(100,25, text="Bateaux :", fill="dark blue", font=("Purisa", 20))
			case.config(bg="azure2")
		elif x > 0:
			objet = case.create_text(100,25, text=str(bateauxlist[x-1]), state="")
			case.bind("<Button-1>", boatsetter)
		#	case.bind("<Button-3>", onrightclick)
		case.grid(row=x)
	
	bateaux.grid(row=2, column=1, padx=10)
	
	
	
	grilleattaque = tk.Canvas(fenetre, bg = "white")
	
	for x in range(1, 10+1):
		for y in range(1, 10+1):
		
			case = tk.Canvas(grilleattaque, bg="white", height=36, width=36)
		#	image = case.create_image(18,18)
			pos = case.create_text(18,18, text=str(x) + " " + str(y), state="hidden")
			case.bind("<Button-1>", shootedpossetter)
	   #     case.bind("<Button-3>", onrightclick)
			case.grid(row=x, column=y)
	
	
	
	
	# grilleattaque.grid(row=1, column=2, padx=30, pady=5) # on attend que tous les bateaux soient placés pour l'afficher
	
	
	grilledefense = tk.Canvas(fenetre, bg = "white")
	
	for x in range(1, 10+1):
		for y in range(1, 10+1):
		
			case = tk.Canvas(grilledefense, bg="white", height=36, width=36)
		#	image = case.create_image(18,18)
			pos = case.create_text(18,18, text=str(x) + " " + str(y), state="hidden")
			case.bind("<Button-1>", lambda event: event.widget.focus_set())
			case.bind("<Key>", placesetter)
	   #     case.bind("<Button-3>", onrightclick)
			case.grid(row=x, column=y)
	grilledefense.grid(row=2, column=2, padx=30, pady=5)
	
	
	
	
	
	historique = tk.Text(fenetre, bg="white", height=40, width=40)
	
	historique.config(state="disabled")
	
	historique.grid(column=3, row=1, rowspan=2, sticky="NS", pady=10, padx=10)
	
	
	
	chat = tk.Entry(fenetre, width=35)
	
	
	chat.bind("<Return>", sendmessage)
	chat.grid(column=3, row=2, sticky="S", pady=10, padx=10)
	
	
	
	
	"""
	Partie affichage du profil
	"""
	
	
	
	profiledisplayer = tk.Canvas(fenetre, bg = "light green", height=200, width=300)
	
	usernamedisplayer = profiledisplayer.create_text(150,20, text=profiledict["username"], font=("Ubuntu", 20), fill="dark green")
	
	print(profiledict)
	
	
	profileimage = tk.PhotoImage(data=profiledict["image"])
	
		
	profileimagedisplayer = profiledisplayer.create_image(150,100, image=profileimage)
	
	
	profiledisplayer.grid(column=4, row=1, rowspan=2, padx=10, sticky="N")
	
	
	# faire la même chose pour le profil ennemi (UNIQUEMENT LORS DE LA RECEPTION DU PAQUET PROFIL DONC DANS PAQUETHANDLER!!!!!!!)
	
	
		
	"""
	Fin partie affichage du profil
	"""
	
	
	"""
	temporaire : afficheur de paquet
	"""
	
	
	paquetdisplayer = tk.Text(fenetre, bg="grey", height=40, width=40)
	
	paquetdisplayer.tag_config("received", foreground="red")
	paquetdisplayer.tag_config("sended", foreground="green")
	
	
	
	#paquetdisplayer.grid(column=5, row=1, rowspan=2, sticky="NS", pady=10, padx=10)
	
	
	
	"""
	fin : temporaire : afficheur de paquet
	"""
	
	fenetre.after(100, paquetsender("lancé"))
	
	fenetre.mainloop()
	
