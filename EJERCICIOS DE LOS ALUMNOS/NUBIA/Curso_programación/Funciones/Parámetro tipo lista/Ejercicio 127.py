# Definir por asignación una lista de enteros en el bloque principal del programa. 
# Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, 
# la segunda recibe la lista y retorna el mayor valor y 
# la última recibe la lista y retorna el menor.

enteros = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def sumar(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma

def mayor(lista):
    mayor = 0
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor

def menor(lista):
    menor = 0
    for elemento in lista:
        if elemento <= menor:
            menor = elemento
    return menor

def main():
    print(f"La suma de los elementos de la lista es: {sumar(enteros)}")
    print(f"El mayor de los elementos de la lista es: {mayor(enteros)}")
    print(f"El menor de los elementos de la lista es: {menor(enteros)}")
    
main()