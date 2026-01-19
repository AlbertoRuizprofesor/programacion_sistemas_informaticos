"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
inicializar los atributos,
imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
El nombre de la clase llamarla Triangulo.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"Lado mayor: {mayor}")

    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es equilátero")
        else:
            print("No es equilátero")


#Main
triangulo1 = Triangulo(5, 5, 5)
mensaje("Triángulo 1")
triangulo1.lado_mayor()
triangulo1.es_equilatero()

triangulo2 = Triangulo(3, 4, 5)
mensaje("Triángulo 2")
triangulo2.lado_mayor()
triangulo2.es_equilatero()

mensaje("Fin del programa")
