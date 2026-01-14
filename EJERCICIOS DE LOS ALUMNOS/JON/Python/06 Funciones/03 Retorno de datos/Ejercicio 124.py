print("Ejercicio 124")
print("")
print("")

# Elaborar una función que nos retorne el perímetro de un cuadrado 
# pasando como parámetros el valor de un lado.

def perimetro(lado):
    perimetro = lado * 4
    return perimetro

lado = int(input("Ingrese el valor del lado del cuadrado: "))
print("El perímetro del cuadrado es:", perimetro(lado))

print("Fin del programa")
