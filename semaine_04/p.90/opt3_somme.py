"""
Elysabeth Dallaire
Optionnel #3 : Somme
"""

#A
print("SECTION A")

#Initialisation de la variable pour la somme
somme = 0

#Boucle du calcul de la somme
for entier in range(1, 1000):
    somme += entier

#Affichage du resultat
print("Somme des 1000 premiers nombres entiers : ", somme)



#B
print("SECTION B")

#Initialisation des variables
qte_nombre_pairs = 0    #Nombre de chiffres qui ont été trouvés
nombre_actuel = 1       #On commence à 1
somme_pairs = 0         #Total qui contient la somme

#Boucle du calcul de la somme des nombres pairs
while qte_nombre_pairs < 1000:       #Validation pour avoir 1000 nombres pairs au total
    if nombre_actuel % 2 == 0:       #Si le modulo donne 0, il est divisible directement par 2, donc pair
        somme_pairs += nombre_actuel #On ajoute sa valeur au total
        qte_nombre_pairs += 1        #On augmente de 1 le nombre de nombres pairs trouvés
    nombre_actuel += 1               #On incrémente à coup de 1 pour vérifier tous les entiers
#Affichage du resultat
print("Somme des 1000 premiers nombres pairs : ", somme_pairs)

#C
print("SECTION C")

#Initialisation de la variable pour la somme
somme = 0

#Boucle du calcul de la somme
for entier in range(1, 1000):
    somme += entier ** 2

#Affichage du resultat
print("Somme des 1000 premiers nombres au carre : ", somme)