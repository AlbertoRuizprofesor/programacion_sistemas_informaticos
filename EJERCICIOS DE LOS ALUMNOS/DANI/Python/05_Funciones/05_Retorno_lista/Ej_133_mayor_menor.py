# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
def crear_lista():
    lista = []
    
    for x in range(5):
        numero = int(input(f"Introduce el {x+1}º número: "))
        lista.append(numero)
    
    return lista

# Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    
    for x in range(len(lista)):
        if (lista[x]<mayor):
            mayor= lista[x]
        elif (lista[x]>menor):
            menor = lista[x]
    print(f"Número mayor: {mayor}\nNúmero menor: {menor}")

# Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.
mayor_menor(crear_lista())