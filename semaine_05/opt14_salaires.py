"""
Elysabeth Dallaire
Optionnel 14 - Salaires
"""


#le document CSV est ouvert et lu
with open("exercices/bloc_B/semaine_05/salaires.csv", "r") as f:
    lignes = f.read().splitlines() 
nb_lignes = len(lignes)

#creation des variables
separateur = ","
entete = []
noms = []
salaires = []


#distribution des donnees dans les listes
for i in range(nb_lignes):
    ligne = lignes[i]
    colonnes = ligne.split(separateur)
    if i == 0:
        entete = colonnes
    else:
        noms.append(colonnes[0])
        salaires.append(float(colonnes[1]))

#affichage d'un resume
print(entete)
print(f"Nombre de lignes : {len(noms)}")
print(f"Liste (noms)    :  {type(noms[0])} Ex : {noms[0]}")
print(f"Liste (ages)    :  {type(salaires[0])} Ex : {salaires[0]}")
print()

#a
salaire_moyen = sum(salaires)/len(salaires)
print(f"Le salaire moyen des employes est :  {salaire_moyen:.2f} $")

#b
salaire_maximum = max(salaires)
salaire_minimum = min(salaires)
print("Le salaire le plus eleve est : ", salaire_maximum, "$")
print("Le salaire le moins eleve est : ", salaire_minimum, "$")

#c
ratio = salaire_minimum / salaire_maximum
print(f"Le ratio entre le salaire le moins eleve et le plus eleve est : {ratio:.1%}")

#d
salaires_superieurs_200000 = 0
for salaire in salaires:
    if salaire > 200000:
        salaires_superieurs_200000 += 1
print(f"Il y a {salaires_superieurs_200000} employes qui ont un salaire superieur a 200 000 $")