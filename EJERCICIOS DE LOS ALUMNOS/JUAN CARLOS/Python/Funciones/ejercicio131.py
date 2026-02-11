"""Definir una lista de enteros por asignación en el bloque principal.
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos.
Mostrar dicho producto en el bloque principal de nuestro programa."""
#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")
def productoElementos(listaEnteros):
    producto = 1
    for cnt in listaEnteros:
        producto *= cnt
    return producto

#Main
listaEnteros = [1, 2, 3, 4, 5]
producto = productoElementos(listaEnteros)
mensaje("Resultado")
print(f"El producto es: {producto}")
mensaje("Fin del programa")
