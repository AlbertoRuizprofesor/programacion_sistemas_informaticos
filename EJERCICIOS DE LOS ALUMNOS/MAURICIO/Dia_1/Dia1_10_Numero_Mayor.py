num1=float(input("Introduce el numero 1: "))
num2=float(input("introduce el numero 2: "))
num3=float(input("introduce el numero 3: "))
if num1 > num2:
    mayor=num1
else:
    mayor=num2
    if num3 > mayor:
        mayor=num3

print(f"El mayor de los tres numeros es: {mayor}")