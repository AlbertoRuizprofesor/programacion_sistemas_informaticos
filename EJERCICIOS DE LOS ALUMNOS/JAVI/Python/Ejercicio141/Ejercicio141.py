"""
Cargar una lista de 10 enteros, luego mostrarlos por
pantalla a cada elemento separados por una coma.
"""

def cargar_numeros():
    lista = []
    for x in range(10):
        num = int(input("Introduzca un numero: "))
        lista.append(num)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")

lista=cargar_numeros()
imprimir(lista)

