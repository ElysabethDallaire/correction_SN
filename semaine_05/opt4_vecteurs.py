"""
Elysabeth Dallaire
Optionnel 4 - Vecteurs
"""


import numpy as np

#a
vecteur_u = np.array([2, -7, 4])
vecteur_v = np.array([-3, -1, 11])

#b
vecteur_resultant_addition = vecteur_u + vecteur_v
print("Vecteur resultant de l'addition des deux vecteurs : ", vecteur_resultant_addition)

#c
vecteur_resultant_soustraction = vecteur_u - vecteur_v
print("Vecteur resultant de la soustraction des deux vecteurs : ", vecteur_resultant_soustraction)

#d
vecteur_w = 4 * vecteur_u + 3 * vecteur_v
print("Le vecteur w est : ", vecteur_w)

#e
vecteur_u_variation = vecteur_u + 5
print("Vecteur u original : ", vecteur_u)
print("Vecteur u modifie : ", vecteur_u_variation)