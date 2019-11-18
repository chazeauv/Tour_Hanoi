def init(n):
	poteau_g = []
	poteau_c = []
	poteau_d = []

	#dsup = [-1] #compteur disque supérieur

	while n!=0:
		poteau_c.append(n)
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
	a = varinit[0]
	b = varinit[1]
	c = varinit[2]
	
	if (a != []):
		a = a[-1]
		dsup.append(a)
	else:
		dsup.append(0)
	if (b != []):
		b = b[-1]
		dsup.append(b)
	else:
		dsup.append(0)
	if (c != []):
		c = c[-1]
		dsup.append(c)
	else:
		dsup.append(0)
	print(dsup)
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


#nombre_disques(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))
disque_superieur(int(input("Entrez un nombre de disque : ")))
#pos_disque(int(input("Entrez un nombre de disque : ")),(int(input("Entrez le numéro de disque souhaité: "))))



