"""
Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

"""


#Pedimos un valor entre 1 y 10 y lo convertimos a entero
valor=int(input("Ingrese un valor entre 1 y 10:"))

#Recorremos los números del 1 al 12 para generar la tabla
for x in range(1,13):
    tabla = valor*x     #Calculamos el resultado de multiplicar el valor por x
    print(tabla, end = " ") #Imprimimos cada resultado en la misma línea, separado por un espacio