"""
Elysabeth Dallaire
Optionnel #7 - Aleatoire
"""

import random

#Initialisation des variables
nombres_superieurs = 0

#Génération des nombres aléatoires
for x in range(50):
    valeur_aleatoire = random.randint(0, 1)
    if valeur_aleatoire > 0.5:
        nombres_superieurs += 1

#A
print(f"Le nombre a ete superieur a 0.5 -> {nombres_superieurs} fois")

#B
pourcentage = (nombres_superieurs / 50 ) * 100
print(f"Également {pourcentage:.4f} %")

#C - Toujours aux alentours de 40 - 60 %

#D - Aux alentours de 50 %. Plus c'est précis, plus c'est proche de 50%

