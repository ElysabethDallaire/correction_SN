"""
Elysabeth Dallaire
Optionnel #17 - Bacteries
"""

import math as mt 

#a
def fonction_N(temps):
    croissance = 10 * (mt.e ** (0.02 * temps))
    return croissance


#b
print(f"N(0) {fonction_N(0)}")
print(f"N(1) {fonction_N(1)}")
print(f"N(2) {fonction_N(2)}")

#c
print(f"Avant 1000 : {fonction_N(230.25)}")
print(f"Après 1000 : {fonction_N(230.26)}")

#d
print(f"Après 1 000 000 : {fonction_N(575.65)}")
