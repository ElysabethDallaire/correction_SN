"""
Elysabeth Dallaire
Optionnel #1 - Annee
"""


def calculer_age():
    annee_naissance = int(input("Quelle est ton année de naissance? "))
    annee_courante = 2024
    nb_annees_ecoulees = annee_courante - annee_naissance
    return nb_annees_ecoulees


print("Il y a " + str(calculer_age()) + " années qui se sont écoulées depuis ta naissance")