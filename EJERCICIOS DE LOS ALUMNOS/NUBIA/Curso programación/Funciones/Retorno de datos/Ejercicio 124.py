def retornar_perimetro(lado):
    perimetro = lado*4
    return perimetro


# bloque principal

lado = int(input("Lado del cuadrado: "))
print(f"El perímetro del cuadrado es: {retornar_perimetro(lado)}")