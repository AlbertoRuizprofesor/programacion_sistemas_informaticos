"""
- Se tiene la siguiente lista:
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".Volver a imprimir la lista.
    
    lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
    
"""
# Definimos una lista que contiene 4 sublistas.
# Cada sublista tiene varios números enteros.
lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

# Imprimimos la lista completa tal como está al inicio
print(lista)

# Recorremos SOLO la primera sublista: lista[0]
# len(lista[0]) devuelve la cantidad de elementos en esa sublista (4 elementos)
for x in range(len(lista[0])):
    # Si el elemento actual es mayor que 50...
    if lista[0][x] > 50:
        # ...lo reemplazamos por 0
        lista[0][x] = 0

# Imprimimos la lista nuevamente para ver los cambios realizados
print(lista)
