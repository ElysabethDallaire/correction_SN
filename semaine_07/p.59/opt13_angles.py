"""
Elysabeth Dallaire
Optionnel #13 - Angles
"""

import math as mt

def convertir_en_radian(angle_degre):
    angle_rad = mt.radians(angle_degre)
    return angle_rad


def convertir_en_degres(angle_rad):
    angle_degre = mt.degrees(angle_rad)
    return angle_degre


def calculer_sin(angle_degre):
    sinus = mt.sin(angle_degre)
    return sinus


def angle_triangle_rectangle(opp, hyp):
    angle = round((hyp**2 - opp**2)**(1/2), 2)
    return angle


print(convertir_en_radian(58))
print(convertir_en_degres(1))
print(calculer_sin(2.54))
print(angle_triangle_rectangle(5, 10))