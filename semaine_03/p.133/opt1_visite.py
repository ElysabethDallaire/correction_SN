#le document CSV est ouvert et lu
with open("exercices/bloc_B/semaine_03/visiteurs.csv", "r") as f: 
    lignes = f.read().splitlines()
nb_lignes = len(lignes)

#creation des variables
separateur = ";"
entete = []
noms = []
ages = []


#distribution des donnees dans les listes
for i in range(nb_lignes):
    ligne = lignes[i]
    colonnes = ligne.split(separateur)
    if i == 0:
        entete = colonnes
    else:
        noms.append(colonnes[0])
        ages.append(int(colonnes[1]))

#affichage d'un resume
print(entete)
print(f"Nombre de lignes : {len(noms)}")
print(f"Liste (noms)    :  {type(noms[0])} Ex : {noms[0]}")
print(f"Liste (ages)    :  {type(ages[0])} Ex : {ages[0]}")


