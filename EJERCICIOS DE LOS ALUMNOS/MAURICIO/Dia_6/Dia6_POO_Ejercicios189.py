# Desarrollar un programa que cargue los lados de un triángulo e
# implemente los siguientes métodos: inicializar los atributos,
# imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
# El nombre de la clase llamarla Triangulo.


class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        ladoMayor = 0
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            ladoMayor = self.lado1
        elif self.lado2 > self.lado3:
            ladoMayor = self.lado2
        else:
            ladoMayor = self.lado3

        print(f"El lado mayor es el de: {ladoMayor}")


# Bloke

triangulo = Triangulo(12, 18, 13)
triangulo.lado_mayor()
