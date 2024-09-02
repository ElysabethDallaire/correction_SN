"""
Elysabeth Dallaire
Optionnel #6 Location
"""

#Lecture au clavier
nb_jours = int(input("Quel est le nombre de jours de location ? "))
nb_kilometres = int(input("Quel est le nombre de kilometres à parcourir ? "))

#Traitement de la location
cout_base = 25
cout_kilometres = round(nb_kilometres * 0.07, 2)
cout_jours = round(nb_jours * 15, 2)
sous_total = round(cout_base + cout_kilometres + cout_jours, 2)
cout_taxes_assurances = round(sous_total * 0.22, 2)
total = round(sous_total + cout_taxes_assurances, 2)

#Affichage
print("-------------------------------")
print("---  FACTURE DE LA LOCATION ---")
print("- PRIX DE BASE              : " + str(cout_base) + " $")
print("- PRIX DU KILOMETRAGE       : " + str(cout_kilometres) + " $")
print("- PRIX DES JOURS            : " + str(cout_jours) + " $")
print("- PRIX DES ASSURANCES/TAXES : " + str(cout_taxes_assurances) + " $")
print("- PRIX TOTAL : " + str(total) + " $")
print("-------------------------------")
