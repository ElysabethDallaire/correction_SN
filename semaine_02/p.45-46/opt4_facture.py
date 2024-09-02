"""
Elysabeth Dallaire
Optionnel #4 Facture
"""

#Lecture au clavier
sous_total = float(input("Quel est le sous-total de la facture ? "))

#Calcul des taxes
tps = round(sous_total * 0.05, 2)
tvq = round(sous_total * 0.09975, 2)
total = sous_total + tvq + tps

#Affichage
print("Sous-total : " + str(sous_total) + " $")
print("TPS        : " + str(tps) + " $")
print("TVQ        : " + str(tvq) + " $")
print("Total      : " + str(total) + " $")