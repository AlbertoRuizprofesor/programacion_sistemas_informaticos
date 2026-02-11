#Confeccionar una aplicación que muestre una presentación en pantalla del programa. 
#Solicite la carga de dos valores y nos muestre la suma. 
#Mostrar finalmente un mensaje de despedida del programa.

def mostrar_mensaje(mensaje):
    print("***********************************")
    print(mensaje)
    print("************************************")

def carga_suma():
    valor1=input("ingrese el primer valor")
    valor2=input("ingrese el segundo valor")
    suma= valor1+valor2
    print("la suma de los valores es", suma)

#programa principal

mostrar_mensaje ("el programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por estar aqui y ver este mensaje")