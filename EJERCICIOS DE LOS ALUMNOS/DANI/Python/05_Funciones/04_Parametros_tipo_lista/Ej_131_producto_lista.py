# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos.
def producto(lista):
    producto = 1
    for list in lista:
        producto *= list
    return producto
# Definir una lista de enteros por asignación en el bloque principal. 
lista=[3, 7, 8, 10, 2]

# Mostrar dicho producto en el bloque principal de nuestro programa.
print(f"Lista: {lista}\nEl producto de los valores de la lista es: {producto(lista)}")