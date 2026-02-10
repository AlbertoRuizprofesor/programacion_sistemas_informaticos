#Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.

# -----------------------------------------
# Función: cargar_datos
# Pide al usuario 10 números, uno por uno,
# y los guarda dentro de una lista.
# Devuelve la lista completa.
# -----------------------------------------

def cargar_datos():
    numeros = []                     # Lista vacía donde guardaremos los valores

    for i in range(10):              # Se repite 10 veces
        valor = int(input("Ingrese un número: "))
        numeros.append(valor)        # Agrega el número a la lista

    return numeros                   # Devuelve la lista completa


# -----------------------------------------
# Función: mostrar_lista
# Recibe una lista y muestra sus elementos
# en una sola línea, separados por comas.
# -----------------------------------------

def mostrar_lista(numeros):
    for i in range(len(numeros)):    # Recorre la lista por índice
        print(numeros[i], end=",")   # Imprime cada número sin salto de línea


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

lista_numeros = cargar_datos()       # Llama a la función para cargar los datos
mostrar_lista(lista_numeros)         # Muestra la lista ingresada
