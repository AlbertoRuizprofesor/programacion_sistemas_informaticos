#Crear una lista por asignación. La lista tiene que tener 5 elementos. 
# Cada elemento debe ser una lista, la primera lista tiene que tener un elemento,
#la segunda dos elementos, la tercera tres elementos y así sucesivamente.
# Sumar todos los valores de las listas.

#Sumar todos los valores de las listas.

# Definimos una lista que contiene sublistas de distinto tamaño.
# Es una estructura "irregular": cada fila tiene una cantidad diferente de elementos.
lista = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

# Inicializamos una variable para acumular la suma total de todos los elementos
suma = 0

# Recorremos cada sublista usando el índice k
for k in range(len(lista)):
    # Recorremos cada elemento dentro de la sublista lista[k]
    for x in range(len(lista[k])):
        # Sumamos cada elemento encontrado
        suma = suma + lista[k][x]

# Imprimimos la suma total de todos los números contenidos en todas las sublistas
print(suma)
