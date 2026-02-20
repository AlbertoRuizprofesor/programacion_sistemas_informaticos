#Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
# La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el 
# bloque del programa principal a ambas funciones.

#Función para calcular el cuadrado
def calcular_cuadrado():
    numero = int(input("Ingrese un número entero:"))
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")

#Función para calcular el producto de dos números
def calcular_producto():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    producto = numero1 * numero2
    print(f"El productor de {numero1} x {numero2} es igual a: {producto}")


#Invocación de las funciones
calcular_cuadrado()
calcular_producto()

