"""
Elysabeth Dallaire
Optionnel #16 - Dettes
"""

#Initialisation des variables
nb_paiements = 0

#Definition de la dette
dette_totale = int(input("Quel est le montant de la dette? "))
dette_remboursable = dette_totale

#Traitement complet de la dette
while dette_remboursable > 0:
    remboursement = int(input((f"Dette : {dette_remboursable:.2f}$. Combien voulez-vous rembourser? ")))   
    dette_remboursable -= remboursement
    nb_paiements += 1

#Affichage des statistiques
print(f"{'':*>20}")
print(f"Nombre de paiements :{"": <25}{nb_paiements}")
print(f"Montant total remboursé : {"": <20}{dette_totale} $")
print(f"Moyenne des paiements : {"": <22}{dette_totale/nb_paiements} $")