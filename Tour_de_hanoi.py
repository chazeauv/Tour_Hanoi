#pylint: skip-file
from turtle import*
import sys

def init(n):
	poteau_g = []
	poteau_c = []
	poteau_d = []

	vargd = []
	grandeur_disque = []
	h = 20
	m = n

	while n!=0:
		poteau_g.append(n) 
		vargd.append(n)
		n = n-1

	for k in range(0,m):
		g = ((vargd[k])*30)-10
		grandeur_disque.append(g)

	for k in range(0,m-1):
		h = h +15

	grandeur_disque.sort()
	plateau = [poteau_g,poteau_c,poteau_d]

	return poteau_g,poteau_c,poteau_d,grandeur_disque,plateau

def nombre_disques(plateau,ntour):
	lengh = len(plateau[ntour])
	return lengh

def disque_superieur(plateau,n):
	dsup = []

	for ntour in range(0,3):
		a = plateau[ntour]
		if (a != []):
			a = a[-1]
			dsup.append(a)
		else:
			dsup.append(0)

	return(dsup)

def pos_disque(n,numdisque,plateau):
	
	if numdisque in plateau[0]:
		print("Le disque n°", numdisque, "est dans la tour gauche.")
	elif numdisque in plateau[1]:
		print("Le disque n°", numdisque, "est dans la tour centre.")
	elif numdisque in plateau[2]:
		print("Le disque n°", numdisque, "est dans la tour droite.")
	else:
		print("Le numéro de disque n'existe pas.")

def verif_deplacement(n,nt1,nt2):
	ldsup = disque_superieur(plateau,n) #liste des plus hauts disques de chaque tour
	if ldsup[nt1]<ldsup[nt2] and (ldsup[nt1]!=0 or ldsup[nt2]==0):
		return True
	else:
		return False

def verifier_victoire(plateau,n):
	if len(plateau[2]) == n:
		return True 
	else:
		return False 


#TURTLE
hideturtle()
speed(0)
def dessine_plateau(n):
	
	#bgpic("C:\Users\lazer\Desktop\HanoiPowa\wallpaper.gif")
	# print(bgpic())

	dim_grd_disque = 20 + ((n-1)*30) 					#Diamètre du plus grand disque disque
	bord = (dim_grd_disque/2)+15						#Espace entre les tours gauche et droite avec les extremités du plateau
	dim_plateau = dim_grd_disque*3 + 80					#Longueur plateau
	htour = n*20 + 20									#Hauteur tour

	up()
	goto(-300,-200)
	down()

	for k in range (0,2):
		begin_fill()
		forward(dim_plateau)
		left(90)
		forward(30)
		left(90)
		end_fill()

	up()
	goto(-(300-bord),-170)
	down()

	begin_fill()

	for k in range (0,3):
		left(90)
		forward(htour)
		right(90)
		forward(10)
		right(90)
		forward(htour)
		left(90)

		up()
		forward(dim_grd_disque+10)
		down()
	end_fill()

	up()
	goto(-300,-200)
	down()

def dessine_disque(numdisque,n,plateau):
	grandeur_disque = varinit[3]  #Variable donnant la longueur du disque sélectionné
	bord_select = varinit[4]	  #Variable donnant l'écart entre le disque sélectionné et les bordures du plateau
	dim_grd_disque = 20 + ((n-1)*30)

	fillcolor("white")
	begin_fill()

	a = plateau[0]
	b = plateau[1]
	c = plateau[2]

	if numdisque in a:										#Test la tour dans laquelle est le disque

		up()
		goto(-280+((grandeur_disque[-1]/2)-(grandeur_disque[numdisque-1]/2)),-189+20*a[numdisque-1])
		down()
			
		for k in range(0,2):								#Boucle dessin disque
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)
		
	elif numdisque in b:

		up()
		goto(-260+dim_grd_disque+((grandeur_disque[-1]/2)-(grandeur_disque[numdisque-1]/2)),-189+20*b[numdisque-1])
		down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

	elif numdisque in c:

		up()
		goto(-240+2*dim_grd_disque+((grandeur_disque[-1]/2)-(grandeur_disque[numdisque-1]/2)),-189+20*c[numdisque-1])
		down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

	end_fill()
	return grandeur_disque

def efface_disque(numdisque,n,plateau):
	grandeur_disque = varinit[3]
	dim_grd_disque = 20 + ((n-1)*30)

	a = plateau[0]
	b = plateau[1]
	c = plateau[2]


	if numdisque in a:
		up()
		goto(-280+((grandeur_disque[-1]/2)-(grandeur_disque[numdisque-1]/2)),-189+20*a[numdisque-2])
		down()
			
		color("white")
		begin_fill()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		forward((grandeur_disque[numdisque-1]/2)-5)
		color("black")
		begin_fill()

		for k in range(0,2):
			forward(10)
			left(90)
			forward(20)
			left(90)

		end_fill()
		
	elif numdisque in b:
		
		up()
		goto(-260+dim_grd_disque+((grandeur_disque[-1]/2)-(grandeur_disque[numdisque-1]/2)),-189+20*b[numdisque-2])
		down()

		color("white")								#Blanc pour effacer le disque
		begin_fill()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		forward((grandeur_disque[numdisque-1]/2)-5)			#Positionnement disque pour retracer la tour
		color("black")										#Couleur tour
		begin_fill()

		for k in range(0,2):								#Bloucle dessin tour
			forward(10)
			left(90)
			forward(20)
			left(90)

		end_fill()

	elif numdisque in c:

		up()
		goto(-240+2*dim_grd_disque+((grandeur_disque[-1]/2)-(grandeur_disque[numdisque-1]/2)),-189+20*c[numdisque-2])
		down()

		color("white")
		begin_fill()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		forward((grandeur_disque[numdisque-1]/2)-5)
		color("black")
		begin_fill()

		for k in range(0,2):
			forward(10)
			left(90)
			forward(20)
			left(90)

		end_fill()

def dessine_config(n):
	for k in range(0,n+1):
		dessine_disque(k,n,plateau)


def efface_tout(n):
	for k in range(0,n+1):
		efface_disque(k,n,plateau)
	

def lire_coords(n):
	poteau_g = varinit[0]
	poteau_c = varinit[1]
	poteau_d = varinit[2]

	tour_depart = 0
	tour_arrivee = 0
	while (tour_depart != True) and (tour_arrivee != True):
		tour_depart = int(input("Entrez la tour de départ (0 à 2): "))
		tour_arrivee = int(input("Entrez la tour d'arrivée (0 à 2): "))
		td = tour_depart
		ta = tour_arrivee
		p = tour_depart
		lengh = nombre_disques(plateau,p)
		nt1 = tour_depart
		nt2 = tour_arrivee
		verif = verif_deplacement(n,nt1,nt2)
		if lengh > 0:
			tour_depart = True
		else:
			tour_depart = False
		if verif == True:
			tour_arrivee = True
		else:
			tour_arrivee = False
	return td,ta

def jouer_un_coup(n,plateau):
	lire_c = lire_coords(n)
	td = lire_c[0]
	ta = lire_c[1]

	dadd = 0
	deff = 0

	a = plateau[0]
	b = plateau[1]
	c = plateau[2]

	if td == 0 and ta == 1:
		g = a[-1]
		efface_disque(g,n,plateau)
		b.append(g)
		del a[-1]
		dessine_disque(g,n,plateau)
	elif td == 0 and ta == 2:
		g = a[-1]
		efface_disque(g,n,plateau)
		c.append(g)
		del a[-1]
		dessine_disque(g,n,plateau)
	elif td == 1 and ta == 0:
		g = b[-1]
		efface_disque(g,n,plateau)
		a.append(g)
		del b[-1]
		dessine_disque(g,n,plateau)
	elif td == 1 and ta == 2:
		g = b[-1]
		efface_disque(g,n,plateau)
		c.append(g)
		del b[-1]
		dessine_disque(g,n,plateau)	
	elif td == 2 and ta == 0:
		g = c[-1]
		efface_disque(g,n,plateau)
		a.append(g)
		del c[-1]
		dessine_disque(g,n,plateau)
	elif td == 2 and ta == 1:
		g = c[-1]
		efface_disque(g,n,plateau)
		b.append(g)
		del c[-1]
		dessine_disque(g,n,plateau)

	return plateau

def indice_dis(n):
	this = sys.modules[__name__] 
	for x in range(0,n):
		setattr(this, 'ndis%s' % x, n)
		n = n-1
	for i in range(0,n):
		return 'ndis%s'

def boucle_jeu(plateau,n,bord_select):
	limite = 60
	ver_vic = verifier_victoire(plateau,n)
	while ver_vic != True or limite > 0:
		jouer_un_coup(n)
		verifier_victoire(plateau,n)
		limite = limite - 1
	



varinit = init(5)
plateau = varinit[4]
indice_dis(5)


#lire_coords(5)
#nombre_disques(plateau,2)
#disque_superieur(plateau,2)
#pos_disque(5,ndis0,plateau)
#verifier_victoire(plateau,5)
#verif_deplacement(int(input("Entrez le nombre de disque:")),int(input("Entrez la tour de départ (0 à 2):")),int(input("Entrez le numéro de la tour d'arrivée:")))

#dessine_plateau(5)
#dessine_disque(5,5,plateau)
#efface_disque(5,5)
#dessine_config(5)
#jouer_un_coup(5,plateau)
#efface_tout(5)

#mainloop()