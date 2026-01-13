# Desarrollar un programa con dos funciones. 
# La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
def cuadrado():
    num = int(input("Dame el número para calcular su cuadrado: "))
    print(f"El cuadrado de {num} es {num**2}\n")

# La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
def producto():
    num1 = int(input("Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    print(f"El producto de {num1} y {num2} es {num1%num2}")

# LLamar desde el bloque del programa principal a ambas funciones.
cuadrado()
producto()