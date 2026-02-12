print("Ejercicio 123")
print("")
print("")

# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def promedio(num1, num2, num3):
    prom= (num1 + num2 + num3) / 3
    return prom

n1=int(input("Ingrese el primer número entero: "))
n2=int(input("Ingrese el segundo número entero: "))
n3=int(input("Ingrese el tercer número entero: "))

print("El promedio es:", promedio(n1, n2, n3))

print("Fin del programa")
