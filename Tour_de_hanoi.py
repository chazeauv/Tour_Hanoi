from turtle import*

def init(n):
	poteau_g = []
	poteau_c = []
	poteau_d = []

	#dsup = [-1] #compteur disque supérieur

	while n!=0:
		poteau_d.append(n)
		n = n-1

	#print(dsup)
	return poteau_g,poteau_c,poteau_d

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

#nombre_disques(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))
#disque_superieur(int(input("Entrez un nombre de disque : ")))
#pos_disque(int(input("Entrez un nombre de disque : ")),(int(input("Entrez le numéro de disque souhaité: "))))
#verif_deplacement(int(input("Entrez le nombre de disque:")),int(input("Entrez la tour de départ (0 à 2):")),int(input("Entrez le numéro de la tour d'arrivée:")))

#TURTLE

def dessine_plateau(n):
	
	dim_grd_disque = n*3 + 98

	up()
	goto(-300,-200)
	down()

	for k in range (0,2):
		forward(dim_grd_disque)
		left(90)
		forward(20)
		left(90)
	mainloop()

dessine_plateau(int(input("Entrez le nombre de disques: ")))
	