"""
    Elysabeth Dallaire
    Optionnel 2 Nombres
"""

nombres = [14, 84, 25, 64, 5, 74, 9, 21, 3, 54, 74, 32, 78, 5, 98, 25, 4, 145, 34, 87]

#Affichage en console
print(f"i.   Taille de la liste  : {len(nombres)}")
print(f"ii.  Valeur minimale     : {min(nombres)}")
print(f"iii. Valeur maximale     : {max(nombres)}")
print(f"iv.  Somme des elements  : {sum(nombres)}")
nombres.sort()
print(f"v.   Ordre croissant     : {nombres}")
nombres.reverse()
print(f"vi.  Ordre decroissant   : {nombres}")
