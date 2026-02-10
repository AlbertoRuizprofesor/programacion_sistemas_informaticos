# Funciones


def sumar(v1, v2, v3=0, v4=0, v5=0):
    s = v1 + v2 + v3 + v4 + v5
    return s


# Bloque Principal

print(f"\nLa suma de 5 + 6 es {sumar(5, 6)}")
print(f"\nLa suma de 1 + 2 + 3 es {sumar(1, 2, 3)}")
print(f"\nLa suma de 1 + 2 + 3 + 4 + 5 es {sumar(1, 2, 3, 4, 5)}")
