"""
Elysabeth Dallaire
Optionnel #4 : Premier
"""
import math

#A
n = int(input("Entrer un nombre n -->  "))

#B
racine_n = int(math.sqrt(n))

#C
divisible = False #De base, le nombre n'a aucun diviseur donc, faux
for entier in range(2, racine_n):
    if racine_n % entier == 0:
        print(f"{racine_n} est divisible par {entier}")
        divisible = True #Il existe un diviseur de ce nombre
    else:
        print(f"{racine_n} n'est pas divisble par {entier}")

#D
if divisible: #Si True (divisible est un boolean) directement
    print(f"Le nombre {n} n'est pas un nombre premier")
else:
    print(f"Le nombre {n} est un nombre premier")

#E - Tests...