# Desarrollar un programa con dos funciones. 
# La primera que solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
# La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
# LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado():
    x=int(input("Ingrese un número entero: "))
    print(f"El cuadrado de {x} es: {x**2}")

def producto():
    x=int(input("Ingrese un número entero: "))
    y=int(input("Ingrese un número entero: "))
    print(f"El producto es de {x} y {y} es: {x*y}")

def llamarfuncion():
    cuadrado()
    producto()
    
llamarfuncion()

