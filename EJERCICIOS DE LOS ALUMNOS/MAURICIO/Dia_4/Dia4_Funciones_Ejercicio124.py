# Definicion Funciones
def retornar_perimetro(lado):
    perimetro = lado * 4
    return perimetro


# Bloque Principal

lado = int(input("Lado del cuadrado: "))
print(f"El perimetro es: {retornar_perimetro(lado)}")
