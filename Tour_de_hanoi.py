def init(n):
	poteau_g = []
	poteau_c = []
	poteau_d = []

	#dsup = [-1] #compteur disque supérieur

	while n!=0:
		poteau_g.append(n)
		n = n-1

	#print(dsup)
	return poteau_g,poteau_c,poteau_d

def nombre_disques(n,p):

	varinit = init(n) #variables définies dans init
	l = varinit[p] #Variable l qui prend l'un des poteaux en parametres
	#print(len(l))

def disque_superieur(n,p):

	varinit = init(n) #variables définies dans init
	l = varinit[p]
	l = l[-1]
	print(l)

# ikjhgjhg
#nombre_disques(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))
disque_superieur(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))




