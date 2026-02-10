# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

# Crear la lista y las variables.
lista = [10, 7, 3, 7, 2] # Lista por asignación con 5 elementos
suma = 0    # Acumulador
x = 0      # Contador

# Bucle while que recorre la lista
while x < len(lista):  # Mientras que x sea menor a la longitud de la lista
    suma = suma + lista[x] # En vez de añadir el número, ponemos la variable x para que haga de número gracias a sus valores.
    x = x + 1
print(f"Los elementos de la lista son:\n{lista}\nLa suma de sus elementos es {suma}.")

# FOREACH
for list in lista:
    print(list)