# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def area():
    lado = int(input("Ingrese el valor del lado de un cuadrado: "))
    area = lado*lado
    return area

print(f"El área es: {area()}")
