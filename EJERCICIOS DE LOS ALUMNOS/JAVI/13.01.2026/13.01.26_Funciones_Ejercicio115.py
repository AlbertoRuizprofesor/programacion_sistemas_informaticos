# Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

# Definición de Funciones


def menor_valor():
    v1 = int(input("Ingrese primer valor: "))
    v2 = int(input("Ingrese segundo valor: "))
    v3 = int(input("Ingrese tercer valor: "))

    if v1 < v2 and v1 < v3:
        r = v1

    elif v2 < v1 and v2 < v3:
        r = v2
    else:
        r = v3

    print()
    print(f"El menor de {v1}, {v2}, {v3}, es: {r}")
    print()


# Bloque principal

menor_valor()
menor_valor()
