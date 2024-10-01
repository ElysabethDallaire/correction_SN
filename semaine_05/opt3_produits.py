"""
Elysabeth Dallaire
Optionnel 3 - Produits
"""


import numpy as np

#a
liste_prix = [26.95, 14.46, 1.50, 32.68, 10.50, 12.86, 19.86]
prix = np.array(liste_prix)
print("Liste des prix : ", prix)

#b
prix[prix >= 20] *= 1.18
print("Liste des prix avec frais de douanes : ", prix)

#c
facture_finale = prix.sum()
print("La facture finale est : ", facture_finale, "$")

