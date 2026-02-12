#Cargar una lista con 5 elementos enteros. 
# Ordenarla de menor a mayor y mostrarla por pantalla, 
# luego ordenar de mayor a menor e imprimir nuevamente.

# Creamos una lista vacía donde guardaremos los valores ingresados
lista = []

# Pedimos 5 valores al usuario y los agregamos a la lista
for x in range(5):
    valor = int(input("Ingrese valor:"))
    lista.append(valor)

# -------------------------------
# ORDENAR DE MENOR A MAYOR
# -------------------------------

# Primer bucle: controla cuántas pasadas se hacen
for k in range(4):
    # Segundo bucle: recorre los elementos comparando pares consecutivos
    # Cada pasada deja el mayor al final, por eso restamos k
    for x in range(4 - k):
        # Si el elemento actual es mayor que el siguiente, los intercambiamos
        if lista[x] > lista[x + 1]:
            aux = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = aux

# Mostramos la lista ya ordenada ascendentemente
print("Lista ordenada de menor a mayor")
print(lista)

# -------------------------------
# ORDENAR DE MAYOR A MENOR
# -------------------------------

# Invertimos la comparación
for k in range(4):
    for x in range(4 - k):
        # Ahora intercambiamos si el actual es MENOR que el siguiente
        if lista[x] < lista[x + 1]:
            aux = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = aux

# Mostramos la lista ya ordenada descendentemente
print("Lista ordenada de mayor a menor")
print(lista)
