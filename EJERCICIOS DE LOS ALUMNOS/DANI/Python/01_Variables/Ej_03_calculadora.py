# Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto.

num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
suma = num1 + num2

num3 = int(input("Dame el tercer numero: "))
num4 = int(input("Dame el cuarto numero: "))
mult = num3 * num4

print(f"{num1} + {num2} = {suma}")
print(f"{num3} x {num4} = {mult}")