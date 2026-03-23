#Pide un número entero y muestra su tabla de multiplicar del 1 al 10 usando un bucle.
#Idea clave: Amplía el ejercicio para que el usuario pueda pedir varias tablas hasta escribir "salir".

n = int(input("Numero: "))

for i in range (1,11):
    print("f {n} x {i} = {n * i}")
