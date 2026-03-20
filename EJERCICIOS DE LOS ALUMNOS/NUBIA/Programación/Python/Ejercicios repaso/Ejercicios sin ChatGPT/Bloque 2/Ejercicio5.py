'''
Dada una lista de números, crea funciones que devuelvan el mínimo, el máximo, la media y cuántos valores están por encima de la media. 

Idea clave: Evita usar min, max y sum en la primera versión. 
'''

def minimo(numeros):
    return min(numeros)

def maximo(numeros):
    return max(numeros)

def media(numeros):
    return sum(numeros) / len(numeros)

def superiores(numeros):
    calculoMedia = media(numeros)
    # Generamos un 1 por cada valor que cumple la condición y los sumamos
    return sum(1 for n in numeros if n > calculoMedia)

# Uso del programa
numeros = [7, 4, 9, 10, 6, 8]

print(f"Números: {numeros}")
print(f"Menor: {minimo(numeros)}")
print(f"Mayor: {maximo(numeros)}")
print(f"Media: {media(numeros):.2f}")
print(f"Superiores a la media: {superiores(numeros)}")