#""" EJERCICICIO 183: Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.
#Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math de la biblioteca estándar de Python.

from math import sqrt, pow

valor=int(input("Ingrese un numero: "))
r1=sqrt(valor)             #calcular la raiz cuadrada
r2=pow(valor,3)             #calcula la potencia, calcula el cubo del número.
print("La raíz cuadrada es",r1)
print("El cubo es",r2)