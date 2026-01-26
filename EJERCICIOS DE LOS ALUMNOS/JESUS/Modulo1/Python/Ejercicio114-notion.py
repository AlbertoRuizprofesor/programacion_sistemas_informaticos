#Ejercicio 114 notion Desarrollar un programa con dos funciones. 
# La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
# LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado():
    numero=float(input("Ingrese el valor: "))
    cal_cuadrado=numero*numero
    print(f"El cuadrado de ese numero es: {cal_cuadrado}")

def producto():
    num1=float(input("Ingrese el valor 1 : "))
    num2=float(input("Ingrese el valor 2 : "))
    cal_producto=num1*num2
    print(f"El producto de estos valores es: {cal_producto}")


cuadrado()
producto()