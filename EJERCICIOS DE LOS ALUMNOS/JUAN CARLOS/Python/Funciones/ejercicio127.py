def sumarizar(lista):
    suma=0
    #for x in range(len(lista)): #Recorrer la lista con la longitud de la lista
    for x in lista: #Recorrer la lista con for/each
        suma=suma+x
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men


# bloque principal del programa

listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumarizar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))
