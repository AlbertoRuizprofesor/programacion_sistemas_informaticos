# Funciones


def multiplicar(l, v):
    multi = []
    for x in range(len(l)):
        multi.append(l[x] * v)
    return multi


# Bloke Main

lista = [3, 7, 8, 10, 2]
print(f"Lista original: {lista}")
print("Lista multiplicando cada elemento por 3")
multiplicacion = multiplicar(lista, 3)
print(f"Resultado: {multiplicacion}")
