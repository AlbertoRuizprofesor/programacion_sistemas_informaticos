#Ejercicio 124: Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def perimetro_cuadrado(valor):
    
    return valor*4

valor=int(input("Introduce un valor: "))

print("El perimetro del valor es ", perimetro_cuadrado(valor))