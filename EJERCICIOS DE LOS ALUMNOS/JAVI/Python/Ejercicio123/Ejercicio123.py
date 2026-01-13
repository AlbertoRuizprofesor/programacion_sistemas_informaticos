"""
Elaborar una función que reciba tres enteros
y nos retorne el valor promedio de los mismos.
"""

def calcular_media(v1, v2, v3):
    promedio = (v1+v2+v3)//3
    return promedio

num1=int(input("Introduce un número: "))
num2=int(input("Introduce un número: "))
num3=int(input("Introduce un número: "))
resultado = calcular_media(num1, num2, num3)
print("El valor promedio es: " , resultado)

