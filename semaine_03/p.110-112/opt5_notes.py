"""
    Elysabeth Dallaire
    Optionnel 5 Notes
"""

#a - Creation des variables
prenoms = ["Robert", "Rosanna", "Serge", "Nicole", "Roger", "Marcel", "Plume", "Colette"]
notes = [82, 54, 78, 97, 37, 86, 76, 90]

#b - Nombre d'etudiants
print(f"Nombre d'etudiants : {len(prenoms)}")

#c - Informations 4ieme personne
print(f"La note de {prenoms[3]} est {notes[3]}")

#d - Changer une note
notes[prenoms.index("Roger")] = 39

#e - Ajout nouvelle étudiante
prenoms.append("Ginette")
notes.append(73)

#f - Effacement d'un etudiant
notes.pop(prenoms.index("Plume"))
prenoms.remove("Plume")

#g - Derniere personne
print(f"La derniere personne ({prenoms[len(prenoms)-1]}) à une note de {notes[len(notes)- 1]}")

#h - Avant-derniere personne
print(f"L'avant-derniere personne ({prenoms[len(prenoms)-2]}) à une note de {notes[len(notes)- 2]}")