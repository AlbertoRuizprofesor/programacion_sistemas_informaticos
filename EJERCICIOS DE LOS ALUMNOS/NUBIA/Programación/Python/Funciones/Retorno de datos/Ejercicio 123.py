# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

def numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    return num1, num2, num3


num1, num2, num3 = numeros()
prom = promedio(num1, num2, num3)
print("El promedio es:", prom)

# Me he complicado la vida yo sola. Puedo sustituir la función de los números por 3 inputs y luego:
# print("Valor promedio de los tres numeros", retornar_promedio(valor1,valor2,valor3))

