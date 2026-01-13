# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))

def menor():
    if valor1 < valor2 < valor3:
        print(f"El menor es: {valor1}")
    elif valor2 < valor1 < valor3:
        print(f"El menor es: {valor2}")
    else:
        print(f"El menor es: {valor3}")

menor()

