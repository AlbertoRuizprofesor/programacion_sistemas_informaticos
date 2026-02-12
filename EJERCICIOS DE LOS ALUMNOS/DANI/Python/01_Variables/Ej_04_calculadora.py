# Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.

num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
num3 = int(input("Dame el tercer numero: "))
num4 = int(input("Dame el cuarto numero: "))

suma = num1 + num2 + num3 + num4
promedio = suma / 4

print(f"\nSUMA --> {num1} + {num2} + {num3} + {num4} = {suma}")
print(f"PROMEDIO --> {suma} / 4 = {promedio}\n")