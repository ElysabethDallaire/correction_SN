"""
Elysabeth Dallaire
Optionnel #17 - Triangle
"""
nb_lignes_actuels = 1
nb_lignes = int(input("Combien de lignes voulez-vous? "))
nb_etoiles = "*"

while nb_lignes_actuels <= nb_lignes:
    print(f"{nb_etoiles: ^100}")
    nb_lignes_actuels += 1
    nb_etoiles = nb_etoiles + "**"