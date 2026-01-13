"""
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
"""

def num_mayor(n1 ,n2):
    if n1>n2:
        mayor = n1
    else:
        mayor = n2
    return mayor


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

resultado = num_mayor(num1, num2)
print("El mayor es: " , resultado)

