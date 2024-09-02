"""
Elysabeth Dallaire
Optionnel #6 Bissextile
"""

#Lecture au clavier
annee_a_tester = int(input("Quelle est l'annee à tester ? "))

#Traitement
if annee_a_tester % 4 == 0 and annee_a_tester % 100 != 0:
    print("L'annee " + str(annee_a_tester) + " est bissextile")
elif annee_a_tester % 400 == 0:
    print("L'annee " + str(annee_a_tester) + " est bissextile")
else :
    print("L'annee " + str(annee_a_tester) + " n'est pas bissextile")