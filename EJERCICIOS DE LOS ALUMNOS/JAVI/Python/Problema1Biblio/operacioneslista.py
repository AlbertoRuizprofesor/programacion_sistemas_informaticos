def cargar():
    lista = []
    n = int(input("¿Cuántos elementos tendrá la lista? "))
    for i in range(n):
        valor = int(input(f"Ingrese el elemento {i+1}: "))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    mayor = max(lista)
    print("El mayor elemento de la lista es:", mayor)


def imprimir_suma(lista):
    suma = sum(lista)
    print("La suma de los elementos de la lista es:", suma)





