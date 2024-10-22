"""
Elysabeth Dallaire
Optionnel #4 - Degres
"""

def convertir_en_celsius(temperature_F):
    temperature_C = round((temperature_F - 32 )/ 1.8, 1)
    return temperature_C


def convertir_en_fahrenheit(temperature_C):
    temperature_F = round(temperature_C * 1.8 + 32, 1)
    return temperature_F

#Section b
#i
print(f"0F donne {convertir_en_celsius(0)} en C")
#ii
print(f"0C donne {convertir_en_fahrenheit(0)} en F")
