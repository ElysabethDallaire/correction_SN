"""
Elysabeth Dallaire
Optionnel #7 - Division
"""

def division(n, p):
    q = int(n // p)
    r = n % p
    return q, r


#Test de la fonction
q, r = division(17, 5)
print(f"q = {q}")
print(f"r = {r}")