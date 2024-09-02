"""
Elysabeth Dallaire
Optionnel #6 Location
"""

#Lecture au clavier
nb_jours = int(input("Quel est le nombre de jours de location ? "))
nb_kilometres = int(input("Quel est le nombre de kilometres à parcourir ? "))

#Traitement de la location
cout_base = 25
cout_kilometres = nb_kilometres * 0.07
cout_jours = nb_jours * 15
sous_total = cout_base + cout_kilometres + cout_jours
cout_taxes_assurances = sous_total * 0.22
total = sous_total + cout_taxes_assurances

#Affichage
print("-------------------------------")
print("---  FACTURE DE LA LOCATION ---")
print("- PRIX DE BASE              : " + str(cout_base) + " $")
print("- PRIX DU KILOMETRAGE       : " + str(cout_kilometres) + " $")
print("- PRIX DES JOURS            : " + str(cout_jours) + " $")
print("- PRIX DES ASSURANCES/TAXES : " + str(cout_taxes_assurances) + " $")
print("- PRIX TOTAL : " + str(total) + " $")
print("-------------------------------")
