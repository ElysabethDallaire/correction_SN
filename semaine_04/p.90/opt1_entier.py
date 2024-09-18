"""
Elysabeth Dallaire
Optionnel #1 : Entier
"""

#A
print("SECTION A")
#Avec un WHILE
print("100 premiers entiers avec une boucle WHILE : ")
nombre = 1
while nombre <= 100:
    print(nombre, end = " ")
    nombre += 1

#Avec un FOR
print("\n100 premiers entiers avec une boucle FOR : ")
for nombre in range(1, 101):
    print(nombre, end = " ")

#B
print("\n\nSECTION B")
#Avec un WHILE
print("100 premiers carres avec une boucle WHILE : ")
nombre = 1
while nombre <= 100:
    print(nombre**2, end = " ")
    nombre += 1

#Avec un FOR
print("\n100 premiers carres avec une boucle FOR : ")
for nombre in range(1, 101):
    print(nombre**2, end = " ")


#C
print("\n\nSECTION C")
#Avec un WHILE
print("Nombres pairs entre 1 et 100 avec une boucle WHILE : ")
nombre = 1
while nombre <= 100:
    if nombre % 2 == 0:
        print(nombre, end = " ")
    nombre += 1

#Avec un FOR
print("\nNombres pairs entre 1 et 100 avec une boucle FOR : ")
for nombre in range(1, 101):
    if nombre % 2 == 0:
        print(nombre, end = " ")
