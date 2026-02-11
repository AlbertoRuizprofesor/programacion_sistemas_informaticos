print("Ejercicio 131")
print("")
print("")

# Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos 
# sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.

def producto_lista(lista):
    producto=1
    for n in range(len(lista)):
        producto*=lista[n]
    return producto

def crear_lista():
    lista=[]
    cantidad=int(input("Ingrese la cantidad de elementos que tendra la lista: "))
    for n in range(cantidad):
        valor=int(input(f"Ingrese el valor entero {n+1}: "))
        lista.append(valor)
    return lista

lista=crear_lista()
print("El producto de todos los elementos de la lista es:",producto_lista(lista))


print("Fin del programa")
