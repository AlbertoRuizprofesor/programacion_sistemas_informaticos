"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.
"""

# Función que permite cargar 10 valores enteros en una lista
def cargar_datos():
    numeros = []  # Lista vacía donde se guardarán los valores

    # Se repite 10 veces para pedir valores al usuario
    for i in range(10):
        valor = int(input("Introduce un número: "))
        numeros.append(valor)  # Agregamos cada número a la lista

    return numeros


# Función que devuelve la primera mitad de la lista
def obtener_mitad(numeros):
    mitad = len(numeros) // 2  # Calculamos la mitad usando división entera
    return numeros[:mitad]     # Retornamos desde el inicio hasta la mitad


# Función para imprimir el contenido de una lista
def mostrar_lista(numeros):
    print("Contenido actual de la lista:")
    print(numeros)


# Bloque principal del programa
lista_completa = cargar_datos()
mitad_lista = obtener_mitad(lista_completa)

mostrar_lista(lista_completa)
mostrar_lista(mitad_lista)
