#Ejercicio 116 : Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")


def valor_suma():
    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es: ", suma)

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
valor_suma()
mostrar_mensaje("Es una despedida, ¡ Sigue así !")
