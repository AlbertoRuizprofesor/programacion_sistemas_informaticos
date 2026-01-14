"""
Crear una lista de enteros por asignación. Definir una función que reciba una 
lista de enteros y un segundo parámetro de tipo entero.
Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
"""

def multiplicar (lista, num):
    for x in range(len(lista)):
        multiplicacion = lista[x] * num
        print(multiplicacion)

lista = [4, 12, 8, 11]
print("Lista original: " , lista)
print("Lista mulplicando cada numero por 3: ")
multiplicar(lista,3)

