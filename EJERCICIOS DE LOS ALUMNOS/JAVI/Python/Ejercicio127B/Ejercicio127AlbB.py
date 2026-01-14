"""
Crear un programa que me pida en una lista 5 edades, 
me haga la media de edad en una función y me diga el número
de personas mayores de edad y menores de edad en otra función.
"""

def calcular_media(edades):
    return sum(edades) / len(edades)

def contar_mayores_menores(edades):
    mayores = 0
    menores = 0

    for edad in edades:
        if edad >= 18:
            mayores += 1
        else:
            menores += 1

    return mayores, menores

# Programa principal
edades = []

for i in range(5):
    edad = int(input(f"Introduce la edad {i + 1}: "))
    edades.append(edad)

media = calcular_media(edades)
mayores, menores = contar_mayores_menores(edades)

print(f"\nLa media de edad es: {media}")
print(f"Número de personas mayores de edad: {mayores}")
print(f"Número de personas menores de edad: {menores}")

