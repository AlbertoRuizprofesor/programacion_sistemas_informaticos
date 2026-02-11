"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. 
Mostrar esta tercer lista.
"""

# Creamos la primera lista vacía
lista1 = []
print("Carga de la primer lista")

# Cargamos 4 valores ingresados por el usuario en lista1
for x in range(4):
    valor = int(input("Ingrese valor:"))  # Pedimos un número
    lista1.append(valor)                  # Lo agregamos a lista1

# Creamos la segunda lista vacía
lista2 = []
print("Carga de la segunda lista")

# Cargamos 4 valores ingresados por el usuario en lista2
for x in range(4):
    valor = int(input("Ingrese valor:"))  # Pedimos otro número
    lista2.append(valor)                  # Lo agregamos a lista2

# Creamos una lista para guardar las sumas
listasuma = []

# Recorremos las posiciones del 0 al 3
for x in range(4):
    suma = lista1[x] + lista2[x]  # Sumamos los valores de ambas listas en la misma posición
    listasuma.append(suma)        # Guardamos la suma en la nueva lista

# Mostramos el resultado final
print("Lista resultante:")
print(listasuma)
