#Confeccionar una aplicación que muestre una presentación en pantalla del programa.
# Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.

#Función para mostrar el mensaje
def mostrar_mensaje(mensaje):
    print("********************************************")
    print(mensaje)
    print("********************************************")

#Función para hacer la suma y mostrar el resultado
def suma():
    valor1 = int(input("Ingrese el primer valor:"))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print(f"La suma de {valor1} + {valor2} = {suma}")


#Invocación de las funciones
mostrar_mensaje("Este programa calcula la suma de dos números")
suma()
mostrar_mensaje("Hasta Pronto. Gracias por usar este pequeño programa!")