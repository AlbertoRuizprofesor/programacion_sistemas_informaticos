# Funciones


def sumar(v1, v2, *lista):
    suma = v1 + v2
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma


# Bloque Principal

print("\nLa suma de 1+2", end=" = ")
print(sumar(1, 2))
print("\nLa suma de 1+2+3+4", end=" = ")
print(sumar(1, 2, 3, 4))
print("\nLa suma de 1+2+3+4+5+6+7+8+9+10", end=" = ")
print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
