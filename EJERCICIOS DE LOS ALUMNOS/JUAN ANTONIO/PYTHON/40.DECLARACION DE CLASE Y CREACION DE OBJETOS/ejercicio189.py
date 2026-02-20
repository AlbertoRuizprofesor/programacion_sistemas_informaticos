"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, 
imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.
"""

class Triangulo:

    # Método que pide al usuario ingresar los tres lados del triángulo.
    # Cada valor se convierte a entero y se guarda como atributo del objeto.
    def inicializar(self):
        self.lado1 = int(input("Ingrese primer lado:"))
        self.lado2 = int(input("Ingrese segundo lado:"))
        self.lado3 = int(input("Ingrese tercer lado:"))

    # Método que imprime los valores de los tres lados almacenados.
    def imprimir(self):
        print("Valores de los lados del triangulo")
        print("Lado 1", self.lado1)
        print("Lado 2", self.lado2)
        print("Lado 3", self.lado3)

    # Método que determina cuál de los tres lados es el mayor.
    # Compara lado por lado y muestra el valor más grande.
    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    # Método que verifica si el triángulo es equilátero.
    # Un triángulo es equilátero cuando los tres lados son iguales.
    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")


# Bloque principal del programa

# Se crea un objeto de la clase Triangulo.
triangulo1 = Triangulo()

# Se piden los tres lados al usuario.
triangulo1.inicializar()

# Se muestran los valores ingresados.
triangulo1.imprimir()

# Se muestra cuál es el lado mayor.
triangulo1.lado_mayor()

# Se indica si el triángulo es equilátero o no.
triangulo1.es_equilatero()
