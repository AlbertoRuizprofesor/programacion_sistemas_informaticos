"""
Confeccionar una función que cargue por teclado una lista
de 5 enteros y la retorne. Una segunda función debe recibir
una lista y mostrar todos los valores mayores a 10.
Desde el bloque principal del programa llamar a ambas funciones.
"""

def cargar_lista():
    lista = []
    for x in range(5):
        num = int(input("Introduce un numero: "))
        lista.append(num)
    
    return lista

def mayor_10(lista):
    print("Elementos mayores a 10: ")
    for x in range (len(lista)):
        if lista[x] > 10:
            print(lista[x])

lista = cargar_lista()
mayor_10(lista)


