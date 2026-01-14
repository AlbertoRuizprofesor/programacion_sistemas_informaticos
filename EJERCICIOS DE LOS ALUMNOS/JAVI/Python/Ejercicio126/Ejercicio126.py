"""
Plantear una función que reciba un string en mayúsculas
o minúsculas y retorne la cantidad de letras 'a' o 'A'.
"""

def contar_letras(cadena):
    cant = 0
    for x in range(len(cadena)):
        if cadena[x] == "a" or cadena[x] == "A":
            cant = cant + 1
    
    return cant

cadena = input("Introduzca un palabra: ")
print("La palabra " , cadena , "contiene " , contar_letras(cadena), " aes ")






