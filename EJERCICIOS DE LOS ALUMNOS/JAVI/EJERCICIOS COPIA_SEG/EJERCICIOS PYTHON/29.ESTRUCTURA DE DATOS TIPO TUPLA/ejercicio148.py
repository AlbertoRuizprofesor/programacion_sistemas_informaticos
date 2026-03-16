#Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista.
#Modificar la lista y luego convertir la lista en tupla.

# -----------------------------------------
# Declaramos una tupla con una fecha
# (día, mes, año). Las tuplas son inmutables.
# -----------------------------------------

fecha_original = (25, 12, 2016)

print("Mostramos la tupla original")
print(fecha_original)


# -----------------------------------------
# Convertimos la tupla en una lista.
# Las listas sí se pueden modificar.
# -----------------------------------------

fecha_lista = list(fecha_original)

print("Mostramos la lista creada a partir de la tupla")
print(fecha_lista)


# -----------------------------------------
# Modificamos la lista (cambiamos el día).
# Esto NO se podría hacer si siguiera siendo tupla.
# -----------------------------------------

fecha_lista[0] = 31

print("Mostramos la lista ya modificada")
print(fecha_lista)


# -----------------------------------------
# Convertimos la lista nuevamente en tupla.
# Esto crea una nueva tupla con los cambios.
# -----------------------------------------

fecha_modificada = tuple(fecha_lista)

print("Mostramos la nueva tupla generada desde la lista")
print(fecha_modificada)

