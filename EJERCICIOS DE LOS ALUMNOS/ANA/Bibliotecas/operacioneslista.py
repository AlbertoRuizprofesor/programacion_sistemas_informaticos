# Fichero de métodos para crear y realizar operaciones sobre una lista

def cargar_numeros():

    lista = []
    
    for i in range(5):
        valor = int(input(f"Ingrese valor {i}: "))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    
    mayor = lista[0]
    
    for i in range(1,5):
    
        if lista[i]>mayor:
            mayor=lista[i]
    
    print("Elemento mayor de la lista",mayor)


def imprimir_suma(lista):
    
    suma = 0
    
    for elemento in lista:
        suma=suma+elemento
    print("Suma de todos sus elementos",suma)
