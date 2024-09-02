"""
Elysabeth Dallaire
Optionnel #2 Comparaisons
"""

reponse = True

#A
if (5 * 4) == (2 * 10):
    reponse = True
else:
    reponse = False

print("Il est " + str(reponse) + " que 5 x 4 est égal à 2 x 10")


#B
if (52 * 20 + 4) < (130 * 8):
    reponse = True
else:
    reponse = False

print("Il est " + str(reponse) + " que 52 x 20 + 4 est plus petit que 130 x 8 ")


#C
if 52 * (20 + 4) >= 52 * 100 + 4:
    reponse = True
else:
    reponse = False

print("Il est " + str(reponse) + " que 52 x (20 + 4) est plus grand ou égal à 52 x 100 + 4")
