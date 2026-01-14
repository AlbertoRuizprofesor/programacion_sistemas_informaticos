"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.
"""

def cargar_lista():
    lista = []
    for x in range(5):
        num = int(input("Introduce un numero: "))
        lista.append(num)
    return lista

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        else:
            if lista[i] < menor:
                menor = lista [i]

    return [mayor, menor]

lista = cargar_lista()
caso = mayor_menor(lista)
print ("Mayor de la lista: " , caso[0])
print ("Menor de la lista: " , caso[1])



