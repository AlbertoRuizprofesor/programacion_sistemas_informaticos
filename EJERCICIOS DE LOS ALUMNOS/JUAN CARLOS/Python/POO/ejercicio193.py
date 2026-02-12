"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__,
 calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
"""
import funcionesJC as fnJC
#Clases
class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Introduce el primer valor entero: "))
        self.valor2 = int(input("Introduce el segundo valor entero: "))

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
fnJC.mensaje("Resultados")
oper.sumar()
oper.restar()
oper.multiplicar()
oper.dividir()
fnJC.mensaje("Fin del programa")



