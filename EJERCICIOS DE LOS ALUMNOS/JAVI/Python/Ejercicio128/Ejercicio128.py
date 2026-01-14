"""
Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. 
Implementar una función que imprima el mayor y el menor valor de la lista.
"""

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]

    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        elif lista[x] < menor:
            menor = lista[x]

    print("El mayor es:", mayor)
    print("El menor es:", menor)


lista = []

for x in range(5):
    num = int(input("Introduce un numero: "))
    lista.append(num)

mayor_menor(lista)



