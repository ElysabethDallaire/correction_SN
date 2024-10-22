"""
Elysabeth Dallaire
Optionnel #8 - Mesures
"""

def piedpouce_vers_centimetre(pied, pouce):
    nb_pouces = (12 * pied) + pouce
    centimetres = nb_pouces * 2.54
    return centimetres

def centimetre_vers_piedpouce(centimetres):
    nb_pouces = int(centimetres / 2.54)
    nb_pieds = 0
    while nb_pouces > 12:
        nb_pieds += 1
        nb_pouces -= 12
    return nb_pieds, nb_pouces

centimetres = piedpouce_vers_centimetre(1, 2)
print(f"En centimetres : {centimetres}")
pied, pouce = centimetre_vers_piedpouce(35.56)
print(f"En pied {pied} et pouce {pouce}")
