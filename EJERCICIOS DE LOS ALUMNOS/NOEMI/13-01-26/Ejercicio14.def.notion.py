#Ejercicio 114: Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.


def valor_cuadrado():
    valor=int(input("Introduce un valor: "))
    cuadrado=valor**2
    print("El cuadrado del valor es: ", cuadrado)
    
def separacion():
    print("**************************")
    
def valores_producto():
    valor1=float(input("Introduce el primer valor: "))
    valor2=float(input("Introduce el segundo valor: "))
    producto=valor1*valor2
    print("El producto de los valores es: ", producto)
    
valor_cuadrado()
separacion()
valores_producto()
    