#Confeccionar un programa que solicite la carga de 10 valores reales por teclado. 
# Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa, 
# el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.

#Programa: Carga 10 Números y los suma
#Programador: Juan Antonio Conejo Cantos
#Fecha de última modificación: 13/01/2026

#Iniciación de la variable suma
suma = 0.0

#El bucle for permite ingresar 10 números y sumarlos
for x in range(10):
    numero = float(input("Ingrese un número: "))
    suma = suma + numero

#Muestra la suma de los números
print(f"La suma de los números es: {suma}")
