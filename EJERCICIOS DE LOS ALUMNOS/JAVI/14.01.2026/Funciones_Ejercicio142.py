# Funciones
def tabla(valor, termino=10):
    for x in range(1, termino + 1):
        resultado = valor * x
        print(f"{valor} x {x} = {resultado}")


# Bloque Principal

termino = int(input("Ingrese el termino de la tabla: "))
numero = int(input("Ingrese el numero para calcular la tabla de multiplicar: "))
tabla(numero, termino)
