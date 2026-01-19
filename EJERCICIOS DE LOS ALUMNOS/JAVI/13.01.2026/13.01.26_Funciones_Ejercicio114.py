# Desarrollar un programa con dos funciones.
# La primera solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
# La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
# LLamar desde el bloque del programa principal a ambas funciones.

# Definicion de Funciones


def calcular_cuadrado():
    valor = int(input("Ingrese un entero aleatorio que usted elija:"))
    cuadrado = valor * valor
    print(f"El cuadrado de {valor}es", cuadrado)


def calcular_producto():
    valor1 = int(input("Ingrese primer valor:"))
    valor2 = int(input("Ingrese segundo valor:"))
    producto = valor1 * valor2
    print("El producto de los valores es:", producto)


# Bloque Principal

calcular_cuadrado()
calcular_producto()
