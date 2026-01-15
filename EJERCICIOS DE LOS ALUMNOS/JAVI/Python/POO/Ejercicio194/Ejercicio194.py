"""
Plantear una clase Operaciones que solicite en el método __init__ 
la carga de dos enteros e inmediatamente muestre su suma, resta, multiplicación
y división. Hacer cada operación en otro método de la clase Operación y llamarlos
desde el mismo método __init__
"""

class Operacion:

    def __init__(self):
        self.num1 = int(input("Introduce el numero 1: "))
        self.num2 = int(input("Introduce el numero 2: "))

        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    

    def sumar(self):
        suma = self.num1 + self.num2
        print("La suma es: " , suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("La resta es: " , resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("La multiplicacion es: " , multiplicacion)

    def dividir(self):
        division = self.num1 / self.num2
        print("La division es: " , division)

operacion1 = Operacion()



