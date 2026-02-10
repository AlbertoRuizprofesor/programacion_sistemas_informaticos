# Desarrollar un programa que permita ingresar el lado de un cuadrado.
# Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

# Definición de Funciones


def mostrar_perimetro(lado):
    p = lado * 4
    print(f"\nEl perimetro es: {p}\n")


def mostrar_superficie(lado):
    s = lado * lado
    print(f"\nLa superficie es: {s}\n")


def cargar_dato():
    l = int(input("\nIngrese el valor del lado de un cuadrado: "))
    respuesta = input(
        "Quiere calcular el perimetro o la superficie [ingresar texto: perimetro/superficie]? "
    ).lower()
    if respuesta == "perimetro" or respuesta == "p":
        mostrar_perimetro(l)
    if respuesta == "superficie" or respuesta == "s":
        mostrar_superficie(l)


# Bloque Principal

cargar_dato()
