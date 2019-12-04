from turtle import*

def init(n):
	poteau_g = []
	poteau_c = []
	poteau_d = []

	vargd = []
	grandeur_disque = []
	bord_select = []
	m = n

	while n!=0:
		poteau_g.append(n)
		vargd.append(n)
		n = n-1

	for k in range(0,m):
		g = ((vargd[k])*30)-10
		grandeur_disque.append(g)
		bord_select.append(g)

	grandeur_disque.sort()
	return poteau_g,poteau_c,poteau_d,grandeur_disque,bord_select

def nombre_disques(n,p):
	varinit = init(n) #variables définies dans init
	l = varinit[p] #Variable l qui prend l'un des poteaux en parametres
	lengh = len(l)
	return lengh

def disque_superieur(n):

	varinit = init(n) #variables définies dans init
	dsup = []


	for ntour in range(0,3):
		a = varinit[ntour]
		if (a != []):
			a = a[-1]
			dsup.append(a)
		else:
			dsup.append(0)

	return dsup
def pos_disque(n,numdisque):

	varinit = init(n) #variables définies dans init
	
	if numdisque in varinit[0]:
		print("Le disque n°", numdisque, "est dans la tour gauche.")
	elif numdisque in varinit[1]:
		print("Le disque n°", numdisque, "est dans la tour centre.")
	elif numdisque in varinit[2]:
		print("Le disque n°", numdisque, "est dans la tour droite.")
	else:
		print("Le numéro de disque n'existe pas.")

def verif_deplacement(n,nt1,nt2):
	ldsup = disque_superieur(n) #liste des plus hauts disques de chaque tour
	if ldsup[nt1]<ldsup[nt2] and (ldsup[nt1]!=0 or ldsup[nt2]==0):
		return True
	else:
		return False

def verifier_victoire(n):
	varinit = init(n)
	nt2 = varinit[2]
	if len(nt2) == n:
		print("GG")
	else:
		print("PAS GG")


#TURTLE
#hideturtle()
def dessine_plateau(n):
	
	# bgpic("C:\Users\lazer\Desktop\HanoiPowa\wallpaper.gif")
	# print(bgpic())

	dim_grd_disque = 20 + ((n-1)*30) 					#Diamètre du plus grand disque disque
	bord = (dim_grd_disque/2)+11						#Espace entre les tours gauche et droite avec les extremités du plateau
	dim_plateau = dim_grd_disque*3 + 80					#Longueur plateau
	htour = n*20 + 20									#Hauteur tour

	hideturtle()

	up()
	goto(-300,-200)
	down()

	for k in range (0,2):
		begin_fill()
		forward(dim_plateau)
		left(90)
		forward(60)
		left(90)
		end_fill()

	up()
	goto(-(300-bord),-140)
	down()

	begin_fill()

	for k in range (0,3):
		left(90)
		forward(htour)
		right(90)
		forward(18)
		right(90)
		forward(htour)
		left(90)

		up()
		forward((dim_plateau-2*bord-54)/2)
		down()
	end_fill()

	up()
	goto(-300,-200)
	down()

def dessine_disque(numdisque,n):
	varinit = init(n)
	dessine_plateau(n)
	grandeur_disque = varinit[3]
	bord_select = varinit[4]

	a = varinit[0]
	b = varinit[1]
	c = varinit[2]

	if numdisque in a:

		if numdisque == a[0]:
			up()
			goto(-300+bord_select[numdisque-1],-140)
			down()

		else:
			up()
			goto(-300+bord_select[numdisque-1],-140+20*a[numdisque-1])
			down()
			
		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)
		
	elif numdisque in b:
		if numdisque == b[0]:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-140)
			down()

		else:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-140+20*a[numdisque-1])
			down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

	elif numdisque in c:
		if numdisque == c[0]:
			up()
			goto(-300+3*bord_select[numdisque-1]+2*grandeur_disque[numdisque-1],-140)
			down()

		else:
			up()
			goto(-280+2*bord_select[numdisque-1],-140+20*a[numdisque-1])
			down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		return grandeur_disque

def efface_disque(numdisque,n):
	varinit = init(n)
	dessine_plateau(n)
	grandeur_disque = varinit[3]
	bord_select = varinit[4]
	dessine_disque(numdisque,n)

	a = varinit[0]
	b = varinit[1]
	c = varinit[2]

	begin_fill(white)

	if numdisque in a:

		if numdisque == a[0]:
			up()
			goto(-300+bord_select[numdisque-1],-140)
			down()

		else:
			up()
			goto(-300+bord_select[numdisque-1],-140+20*a[numdisque-1])
			down()
			
		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		mainloop()
		
	elif numdisque in b:
		if numdisque == b[0]:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-140)
			down()

		else:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-140+20*a[numdisque-1])
			down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		mainloop()

	elif numdisque in c:
		if numdisque == c[0]:
			up()
			goto(-300+3*bord_select[numdisque-1]+2*grandeur_disque[numdisque-1],-140)
			down()

		else:
			up()
			goto(-280+2*bord_select[numdisque-1],-140+20*a[numdisque-1])
			down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		mainloop()

#dessine_plateau(5)
efface_disque(5,5)

def lire_coords(n):
	varinit = init(n)
	poteau_g = varinit[0]
	poteau_c = varinit[1]
	poteau_d = varinit[2]
	print(poteau_g,poteau_c,poteau_d)
	tour_depart = 0
	tour_arrivee = 0
	while (tour_depart != True) and (tour_arrivee != True):
		tour_depart = int(input("Entrez la tour de départ (0 à 2): "))
		tour_arrivee = int(input("Entrez la tour d'arrivée (0 à 2): "))
		td = tour_depart
		ta = tour_arrivee
		p = tour_depart
		lengh = nombre_disques(n,p)
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
	print("Le déplacement entre la tour",td,"et la tour",ta,"est possible.")


lire_coords(10)
#nombre_disques(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))
#disque_superieur(int(input("Entrez un nombre de disque : ")))
#pos_disque(int(input("Entrez un nombre de disque : ")),(int(input("Entrez le numéro de disque souhaité: "))))
#verif_deplacement(int(input("Entrez le nombre de disque:")),int(input("Entrez la tour de départ (0 à 2):")),int(input("Entrez le numéro de la tour d'arrivée:")))