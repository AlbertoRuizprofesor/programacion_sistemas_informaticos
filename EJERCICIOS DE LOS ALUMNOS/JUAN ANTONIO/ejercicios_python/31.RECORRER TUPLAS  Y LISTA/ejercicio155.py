"""
Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.

Luego en otras funciones:

1) Imprimirla en forma completa.

2) Obtener y mostrar el mayor.

3) Mostrar la suma de todas sus componentes.

Utilizar la nueva sintaxis de for vista en este concepto.
"""

def cargar_numeros():
    """
    Solicita 5 números al usuario y los guarda en una lista.
    Devuelve la lista completa.
    """
    numeros = []
    for i in range(5):
        valor = int(input("Ingrese un número: "))
        numeros.append(valor)
    return numeros


def mostrar_lista(numeros):
    """
    Imprime todos los elementos de la lista recibida.
    """
    print("Contenido de la lista:")
    for elemento in numeros:
        print(elemento)


def mostrar_mayor(numeros):
    """
    Calcula el valor máximo de la lista y lo muestra.
    """
    mayor_valor = numeros[0]
    for elemento in numeros:
        if elemento > mayor_valor:
            mayor_valor = elemento
    print("El número mayor es:", mayor_valor)


def sumar_lista(numeros):
    """
    Suma todos los elementos de la lista y muestra el resultado.
    """
    suma_total = 0
    for elemento in numeros:
        suma_total += elemento
    print("La suma total de los elementos es:", suma_total)


# Bloque principal del programa

lista_numeros = cargar_numeros()
mostrar_lista(lista_numeros)
mostrar_mayor(lista_numeros)
sumar_lista(lista_numeros)
