'''
Pide un número entero y muestra su tabla de multiplicar del 1 al 10 usando un bucle. 
Idea clave: 
Amplía el ejercicio para que el usuario pueda pedir varias tablas hasta escribir "salir". 
'''

numero = int(input("Indica el número del que quieres la tabla de multiplicar: "))

for n in range(1, 11):
    print(f"{numero} x {n} = {numero*n}")