#Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

# Definimos una función que recibe el valor del lado de un cuadrado
# y calcula su perímetro multiplicando ese lado por 4.
def retornar_perimetro(lado):
    perimetro = lado * 4   # Fórmula del perímetro del cuadrado
    return perimetro       # Devolvemos el resultado

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos al usuario que ingrese el valor del lado del cuadrado
lado = int(input("Lado del cuadrado:"))

# Llamamos a la función y mostramos el perímetro calculado
print("El perimetro es:", retornar_perimetro(lado))
