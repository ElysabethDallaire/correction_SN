"""
Elysabeth Dallaire
Optionnel #2 : Divisible
"""

for nombre in range(1, 50):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FIZZBUZZ")
    elif nombre % 3 == 0:
        print("FIZZ")
    elif nombre % 5 == 0:
        print("BUZZ")
    else:
        print("Le nombre est " + str(nombre))