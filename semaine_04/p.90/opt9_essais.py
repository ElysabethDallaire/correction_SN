"""
Elysabeth Dallaire
Optionnel #9 - Essais
"""

import random

#A
#Initilisation de la variable
nombre_essais = 1

#Simulation de dé
while nombre_essais :
    lancer_de = random.randint(1, 6)
    if lancer_de == 6:
        break
    nombre_essais += 1

#Affichage
print(f"Il y a eu besoin de {nombre_essais} essais")

#B - Environ 6

#C
resultats_lancers = []

#Boucle de 1000 tours
for x in range(1000):
    #Initilisation de la variable
    nombre_essais = 1
    #Simulation de dé
    while nombre_essais :
        lancer_de = random.randint(1, 6)
        if lancer_de == 6:
            break
        nombre_essais += 1
    resultats_lancers.append(nombre_essais) #Ajouter le nombre d'essais nécéssaires (pour ce tour)

#Calcul de la moyenne
moyenne = sum(resultats_lancers) / len(resultats_lancers)


#Affichage
print(f"La moyenne du nombre de lancers est {moyenne}")