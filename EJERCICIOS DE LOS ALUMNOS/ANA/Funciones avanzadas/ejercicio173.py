
# 1) Carga de una lista de 10 enteros.
# 2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
# 3) Imprimir una lista.

def cargar_numeros():
    
    lista = []
    print("Introduzca 10 numeros enteros: ")

    for i in range(10):
    
        valor = int(input(f"Cargar valor {i}: "))
        lista.append(valor)
    
    return lista


def retornar_mitad(lista):
    
    mitad=len(lista)//2 
    
    return lista[:mitad] 


def imprimir(lista):

    print("Contenido de la lista")
    print(lista)


# Programa

lista=cargar_numeros()
lista2=retornar_mitad(lista)
imprimir(lista)
imprimir(lista2)