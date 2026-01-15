# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
# Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
# Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

def carga_lista():
    lista = []
    for n in range(5):
        num = int(input(f"Introduce el número {n+1}: "))
        lista.append(num)
    return lista

def mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    print(f"El mayor de los elementos de la lista es: {mayor}")
    print(f"El menor de los elementos de la lista es: {menor}")
    
# Bloque principal lista
lista = carga_lista()
mayor_menor(lista) 

