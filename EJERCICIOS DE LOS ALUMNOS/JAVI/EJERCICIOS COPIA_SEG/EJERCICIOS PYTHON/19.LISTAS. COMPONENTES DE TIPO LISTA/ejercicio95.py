#Crear una lista por asignación. 
#La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
# Imprimir sus elementos accediendo de diferentes modos.

# Definimos una lista que contiene 4 listas internas
lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# Imprimimos la lista completa tal cual está definida
print(lista)
print("---------")

# Imprimimos la primera lista interna (índice 0)
print(lista[0])
print("---------")

# Imprimimos el primer elemento de la primera lista interna
# lista[0] → [1,2,3]
# lista[0][0] → 1
print(lista[0][0])
print("---------")

# Recorremos con un for la primera lista interna e imprimimos sus elementos
for x in range(len(lista[0])):   # len(lista[0]) = 3
    print(lista[0][x])
print("---------")

# Recorremos TODAS las listas internas y sus elementos uno por uno
for k in range(len(lista)):      # Recorre cada sublista
    for x in range(len(lista[k])):  # Recorre cada elemento de la sublista
        print(lista[k][x])
