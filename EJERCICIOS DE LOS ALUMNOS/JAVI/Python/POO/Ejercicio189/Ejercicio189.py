"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
El nombre de la clase llamarla Triangulo.
"""

class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir(self):
        print("Valores de los lados del triángulo")
        print("Lado 1:", self.lado1)
        print("Lado 2:", self.lado2)
        print("Lado 3:", self.lado3)

    def lado_mayor(self):
        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
            print("El mayor lado es:", self.lado1)
        elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3:
            print("El mayor lado es:", self.lado2)
        else:
            print("El mayor lado es:", self.lado3)

    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")


# Programa principal
triangulo1 = Triangulo(2, 3, 3)
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.equilatero()





