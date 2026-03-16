
"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume.
Finalizar la carga al ingresar el valor -1.
"""

#Declaración de la variable suma
suma=0

#Introducción de datos por consola
valor=int(input("Ingrese valor (-1 finaliza):")) 

#Mientras valor sea distinto a -1 se sigue ingresando valores
#Ingreso de valores por consola y salidad de la suma
while valor!=-1:
    suma=suma+valor
    valor=int(input("Ingrese valor(-1 finaliza):"))  
print("La suma de los valores ingresados es")
print(suma)