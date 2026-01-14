"""
Elaborar una función que nos retorne el perímetro de 
un cuadrado pasando como parámetros el valor de un lado.
"""

def calcular_perimetro (lado):
    perimetro = lado * 4
    return perimetro

num = int(input("Introduce el valor del lado: "))
print("El perimetro es: ")
print(calcular_perimetro(num))



