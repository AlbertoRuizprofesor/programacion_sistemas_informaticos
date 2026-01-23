"""
Confeccionar un programa que contenga las siguientes funciones:

1) Carga de una lista y retorno al bloque principal.

2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.

3) Imprimir la lista
"""

def cargar_numeros():
    # Crea una lista vacía donde se guardarán los valores ingresados
    numeros = []
    continuar = "s"

    # Permite ingresar valores mientras el usuario responda "s"
    while continuar == "s":
        valor = int(input("Ingrese un valor: "))
        numeros.append(valor)  # Agrega el valor a la lista
        continuar = input("¿Agregar otro número? [s/n]: ")

    return numeros


def reemplazar_por_cero(lista_numeros):
    # Recorre la lista por índice para poder modificar sus elementos
    for i in range(len(lista_numeros)):
        # Si el número es menor que 10, se reemplaza por 0
        if lista_numeros[i] < 10:
            lista_numeros[i] = 0


def mostrar_lista(lista):
    # Imprime los elementos en una sola línea separados por guiones
    for elemento in lista:
        print(elemento, "-", sep="", end="")
    print("")  # Salto de línea final


# Bloque principal del programa

lista = cargar_numeros()
print("Lista antes de modificar:")
mostrar_lista(lista)

reemplazar_por_cero(lista)
print("Lista después de modificar:")
mostrar_lista(lista)
