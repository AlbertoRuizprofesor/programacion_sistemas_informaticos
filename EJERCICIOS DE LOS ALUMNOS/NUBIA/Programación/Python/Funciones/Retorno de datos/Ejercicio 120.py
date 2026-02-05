# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

lado = int(input("Ingrese el valor del lado del cuadrado: "))

def retornar_area(lado):
    area = lado*lado
    return area
area = retornar_area(lado)

print(f"El área del cuadrado es: {area}")


