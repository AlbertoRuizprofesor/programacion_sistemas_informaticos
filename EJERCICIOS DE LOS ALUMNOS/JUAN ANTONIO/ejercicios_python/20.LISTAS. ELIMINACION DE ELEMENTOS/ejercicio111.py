#Crear una lista de 5 enteros y cargarlos por teclado. 
#Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

# Creamos una lista vacía donde guardaremos los valores ingresados por el usuario
lista1 = []

# Cargamos 5 valores en la lista principal
for x in range(5):
    valor = int(input("Ingrese valor:"))
    lista1.append(valor)

# Mostramos la lista original tal como fue ingresada
print("Lista original")
print(lista1)

# Creamos una segunda lista donde guardaremos los valores mayores o iguales a 10
lista2 = []

# Usamos una variable 'posicion' para recorrer lista1 manualmente
posicion = 0

# Recorremos lista1 mientras la posición sea válida
while posicion < len(lista1):
    # Si el valor actual es mayor o igual a 10...
    if lista1[posicion] >= 10:
        # Lo eliminamos de lista1 y lo agregamos a lista2
        # IMPORTANTE: al hacer pop(), los elementos se corren hacia la izquierda
        # por eso NO incrementamos 'posicion' aquí
        lista2.append(lista1.pop(posicion))
    else:
        # Si el valor es menor que 10, avanzamos a la siguiente posición
        posicion = posicion + 1

# Mostramos cómo quedó lista1 después de eliminar los valores >= 10
print("Lista despues de borrar los elementos mayores o iguales a 10")
print(lista1)

# Mostramos la lista que contiene los valores extraídos
print("Lista generada con los elementos mayores o iguales a 10")
print(lista2)
