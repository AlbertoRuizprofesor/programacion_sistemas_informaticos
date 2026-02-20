"""
Almacenar en una lista de 5 elementos tuplas 
que guarden el nombre de un pais y la cantidad de habitantes.

Definir tres funciones, en la primera cargar la lista, en la 
segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes.
"""

# -----------------------------------------
# Función: cargar_paises
# Solicita al usuario el nombre de 5 países
# y su cantidad de habitantes.
# Guarda cada país como una tupla (nombre, población)
# dentro de una lista y la devuelve.
# -----------------------------------------

def cargar_paises():
    lista_paises = []

    for i in range(5):
        nombre = input("Ingrese el nombre del país: ")
        poblacion = int(input("Ingrese la cantidad de habitantes: "))
        lista_paises.append((nombre, poblacion))   # Se guarda como tupla

    return lista_paises


# -----------------------------------------
# Función: mostrar_paises
# Recibe una lista de tuplas (nombre, población)
# e imprime cada país junto a su cantidad de habitantes.
# -----------------------------------------

def mostrar_paises(lista_paises):
    print("Países y su población:")
    for i in range(len(lista_paises)):
        print(lista_paises[i][0], lista_paises[i][1])


# -----------------------------------------
# Función: pais_con_mas_poblacion
# Recorre la lista de países y determina cuál
# tiene la mayor cantidad de habitantes.
# Imprime el nombre del país con mayor población.
# -----------------------------------------

def pais_con_mas_poblacion(lista_paises):
    indice_max = 0   # Suponemos que el primero es el mayor

    for i in range(1, len(lista_paises)):
        if lista_paises[i][1] > lista_paises[indice_max][1]:
            indice_max = i

    print("País con mayor cantidad de habitantes:", lista_paises[indice_max][0])


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

paises = cargar_paises()                 # Carga los datos
mostrar_paises(paises)                   # Muestra la lista completa
pais_con_mas_poblacion(paises)           # Muestra el país más poblado
