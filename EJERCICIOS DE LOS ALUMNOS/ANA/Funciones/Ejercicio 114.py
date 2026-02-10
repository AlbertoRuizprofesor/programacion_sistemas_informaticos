#Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero 
#y muestre el cuadrado de dicho valor.
#La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
#LLamar desde el bloque del programa principal a ambas funciones.
def calcular_cuadrado():
    valor=int(input("muestra el entero" , ))
    cuadrado= valor*valor 
    print("El cuadrado es" , cuadrado)

def calcular_producto():
    valor1=int(input("ingrese el primer valor:"))
    valor2=int(input("ingrese el segundo valor"))
    producto=valor1*valor2 
    print("El producto de los valores es", producto)

#El bloque principal 
calcular_cuadrado() 
calcular_producto()


    