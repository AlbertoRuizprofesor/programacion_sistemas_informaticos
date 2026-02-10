"""
Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros
e inmediatamente muestre su suma, resta, multiplicación y división.
Hacer cada operación en otro método de la clase Operación y llamarlos desde el mismo método __init__
"""
import funcionesJC as fnJC
#Clases
class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Introduce el primer valor entero: "))
        self.valor2 = int(input("Introduce el segundo valor entero: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        resultado = self.valor1 + self.valor2
        print(f"Suma: {self.valor1} + {self.valor2} = {resultado}")

    def restar(self):
        resultado = self.valor1 - self.valor2
        print(f"Resta: {self.valor1} - {self.valor2} = {resultado}")

    def multiplicar(self):
        resultado = self.valor1 * self.valor2
        print(f"Multiplicación: {self.valor1} * {self.valor2} = {resultado}")

    def dividir(self):
        if self.valor2 != 0:
            resultado = self.valor1 / self.valor2
            print(f"División: {self.valor1} / {self.valor2} = {resultado:.2f}")
        else:
            print("Error: División por cero")


#Main
fnJC.mensaje("Carga de valores")
oper = Operaciones()
fnJC.mensaje("Fin del programa")
