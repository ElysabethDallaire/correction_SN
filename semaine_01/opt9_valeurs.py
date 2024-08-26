"""
Elysabeth Dallaire
Optionnel #9 Valeurs
"""

x = 3 + 4**2    # x = 19 
y = x - 4       # y = 15
z = y - x       # z = -4
x = y * z -3    # x = -63 (On écrase la valeur de x)
y = 3           # y = 3 (On écrase la valeur de y)
x + y + z       # Ne fait rien, le résultat n'est pas enregistré dans une variable
print(x)        # x = -63
print(y)        # y = 3
print(z)        # z = -4