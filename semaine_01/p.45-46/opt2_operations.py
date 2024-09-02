"""
Elysabeth Dallaire
Optionnel #2 Operations
"""

#Lecture au clavier
premier_nb = int(input("Entrez le premier nombre : "))
second_nb = int(input("Entrez le second nombre : "))

#Affichage
print(">>>")
print(str(premier_nb) + " + " + str(second_nb) + " = " + str(premier_nb + second_nb))
print(str(premier_nb) + " - " + str(second_nb) + " = " + str(premier_nb - second_nb))
print(str(premier_nb) + " * " + str(second_nb) + " = " + str(premier_nb * second_nb))
print(str(premier_nb) + " / " + str(second_nb) + " = " + str(premier_nb / second_nb))
print(str(premier_nb) + " % " + str(second_nb) + " = " + str(premier_nb % second_nb))
print(str(premier_nb) + " // " + str(second_nb) + " = " + str(premier_nb // second_nb))
print(str(premier_nb) + " ** " + str(second_nb) + " = " + str(premier_nb ** second_nb))




"""
Deuxieme version
"""

#Lecture au clavier
#Identique ...

#Calculs mathematiques
somme = premier_nb + second_nb
soustraction = premier_nb - second_nb
multiplication = premier_nb * second_nb
division = premier_nb / second_nb
modulo = premier_nb % second_nb
division_entiere = premier_nb // second_nb
exposant = premier_nb ** second_nb

#Affichage
print(">>>")
print(str(premier_nb) + " + " + str(second_nb) + " = " + str(somme))
print(str(premier_nb) + " - " + str(second_nb) + " = " + str(soustraction))
print(str(premier_nb) + " * " + str(second_nb) + " = " + str(multiplication))
print(str(premier_nb) + " / " + str(second_nb) + " = " + str(division))
print(str(premier_nb) + " % " + str(second_nb) + " = " + str(modulo))
print(str(premier_nb) + " // " + str(second_nb) + " = " + str(division_entiere))
print(str(premier_nb) + " ** " + str(second_nb) + " = " + str(exposant))

