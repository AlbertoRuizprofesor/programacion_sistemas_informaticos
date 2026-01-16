def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    may=lista[0]
    for x in range(1,5):
        if lista[x]>may:
            may=lista[x]
    print("Mayor de la lista",may)


def imprimir_suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("Suma de todos sus elementos",suma)

def imprimir_resta(lista):
    resta = 0
    for elemento in lista:
        resta=resta - elemento
    print("Resta de todos sus elementos",resta)

def imprimir_multiplicacion(lista):
    multi = 1
    for elemento in lista:
        multi = multi * elemento
    print("Multiplicación de todos sus elementos",multi)
