"""
- Se tiene la siguiente lista:
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
Volver a imprimir la lista.
   
    lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

"""
# Definimos una lista que contiene varias sublistas.
# Cada sublista tiene una cantidad distinta de números.
lista = [[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

# Imprimimos la lista completa tal como está al inicio
print(lista)

# Recorremos cada sublista usando el índice k
for k in range(len(lista)):
    # Recorremos cada elemento dentro de la sublista lista[k]
    for x in range(len(lista[k])):
        # Si el valor actual es mayor que 10...
        if lista[k][x] > 10:
            # ...lo reemplazamos por 0
            lista[k][x] = 0

# Imprimimos la lista nuevamente para ver los cambios realizados
print(lista)
