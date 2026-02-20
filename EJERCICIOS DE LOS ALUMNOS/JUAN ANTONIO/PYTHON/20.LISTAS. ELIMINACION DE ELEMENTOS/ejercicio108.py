#Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.

# Definimos una lista con cinco valores enteros
lista = [10, 20, 30, 40, 50]

# Imprimimos la lista original
print(lista)

# Eliminamos elementos usando pop()
# pop(0) elimina el elemento en la posición 0 → elimina el 10
lista.pop(0)

# OJO: después de eliminar el 10, la lista queda así:
# [20, 30, 40, 50]
# Ahora el índice 1 corresponde al valor 30
lista.pop(1)   # elimina el 30

# Después de eliminar el 30, la lista queda así:
# [20, 40, 50]
# Ahora el índice 2 corresponde al valor 50
lista.pop(2)   # elimina el 50

# Imprimimos la lista final después de las eliminaciones
print(lista)
