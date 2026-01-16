# Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.
def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


# bloque principal

lado=int(input("Lado del cuadrado:"))
print("El perimetro es:",retornar_perimetro(lado))
