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
		poteau_d.append(n)
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
	#print(len(l))

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
		print("VAS Y PASSE")
	else:
		print("BOUFFON TU FOUS QUOI DEGAGE")

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
	
	# bgpic("file:///C:/Users/lazer/OneDrive/Documents/GitHub/Tour_Hanoi/giphy.gif")
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

	print(bord_select[numdisque-1])

	a = varinit[0]
	b = varinit[1]
	c = varinit[2]

	if numdisque in varinit[0]:

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
		
	elif numdisque in varinit[1]:
		if numdisque == b[0]:
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

	elif numdisque in varinit[2]:
		if numdisque == c[0]:
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
		
	else:
		print("ERROR 404 DNF")


#dessine_plateau(5)
dessine_disque(5,5)

#nombre_disques(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))
#disque_superieur(int(input("Entrez un nombre de disque : ")))
#pos_disque(int(input("Entrez un nombre de disque : ")),(int(input("Entrez le numéro de disque souhaité: "))))
#verif_deplacement(int(input("Entrez le nombre de disque:")),int(input("Entrez la tour de départ (0 à 2):")),int(input("Entrez le numéro de la tour d'arrivée:")))