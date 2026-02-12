#Crear una lista por asignación. La lista tiene que tener 2 elementos.
#Cada elemento debe ser una lista de 5 enteros.
#Calcular y mostrar la suma de cada lista contenida en la lista principal.

# Definimos una lista que contiene dos listas internas
lista = [[1,1,1,1,1], [2,2,2,2,2]]

# ---------------------------------------------------------
# PRIMERA FORMA DE SUMAR: SUMA MANUAL ELEMENTO POR ELEMENTO
# ---------------------------------------------------------

# Sumamos uno por uno los elementos de la primera lista interna
suma1 = lista[0][0] + lista[0][1] + lista[0][2] + lista[0][3] + lista[0][4]
print(suma1)   # Imprime la suma de la primera fila

# Sumamos uno por uno los elementos de la segunda lista interna
suma2 = lista[1][0] + lista[1][1] + lista[1][2] + lista[1][3] + lista[1][4]
print(suma2)   # Imprime la suma de la segunda fila

print("----------")

# ---------------------------------------------------------
# SEGUNDA FORMA: SUMAR USANDO UN FOR PARA CADA LISTA
# ---------------------------------------------------------

# Sumamos la primera lista interna recorriéndola con un for
suma1 = 0
for x in range(len(lista[0])):   # len(lista[0]) = 5
    suma1 = suma1 + lista[0][x]
    
# Sumamos la segunda lista interna recorriéndola con un for
suma2 = 0
for x in range(len(lista[1])):   # len(lista[1]) = 5
    suma2 = suma2 + lista[1][x]

print(suma1)
print(suma2)

print("----------")

# ---------------------------------------------------------
# TERCERA FORMA: SUMAR TODAS LAS LISTAS INTERNAS CON DOS BUCLES
# ---------------------------------------------------------

# Recorremos cada lista interna (k recorre filas)
for k in range(len(lista)):
    suma = 0
    # Recorremos cada elemento de la lista interna (x recorre columnas)
    for x in range(len(lista[k])):
        suma = suma + lista[k][x]
    print(suma)   # Imprime la suma de cada fila


