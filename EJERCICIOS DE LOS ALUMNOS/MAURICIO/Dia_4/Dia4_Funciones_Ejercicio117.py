# Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos.
# La carga de los valores hacerlo por teclado.

# Definición de Funciones


def mostrar_mayor(v1, v2, v3):

    if v1 > v2 and v1 > v3:
        r = v1
    elif v2 > v3:
        r = v2
    else:
        r = v3
    print(f"\nEl mayor de los tres numeros es: {r}\n")


def cargar():
    v1 = int(input("\nIngrese el primer valor: "))
    v2 = int(input("Ingrese el segundo valor: "))
    v3 = int(input("Ingrese el tercer valor: "))
    mostrar_mayor(v1, v2, v3)


# Bloque Principal

cargar()
