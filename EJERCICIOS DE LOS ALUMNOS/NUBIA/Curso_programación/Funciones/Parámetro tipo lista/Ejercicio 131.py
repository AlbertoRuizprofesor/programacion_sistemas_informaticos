# Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.

lista_enteros = [1, 2, 3, 4, 5]

def producto(lista_enteros):
    producto = 1
    for x in range(len(lista_enteros)):
        producto = producto * lista_enteros
    return producto


