# Funciones


def cargar():
    lista = []
    for x in range(10):
        valor = int(input(f"Ingrese valor {x+1}: "))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista) - 1):
        print(lista[x], end=" - ")
    print(lista[x + 1])  # Para no poner el guion al final


# Bloque Principal

lista = cargar()
imprimir(lista)
