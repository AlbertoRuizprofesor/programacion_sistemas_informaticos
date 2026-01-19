"""
Confeccionar una clase que represente un empleado.
Definir como atributos su nombre y su sueldo.
En el método __init__ cargar los atributos por teclado y luego en otro
método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos
(si el sueldo supera a 3000)
"""
import funcionesJC as fnJC
#Funciones
class Empleado:
    def __init__(self):
        self.nombre = input("Introduce el nombre: ")
        self.sueldo = int(input(f"Introduce el sueldo para {self.nombre}: "))

    def imprimir(self):
        fnJC.mensaje("Objeto")
        print(f"El empleado: {self.nombre} tiene un sueldo de: {self.sueldo}")

    def impuestos(self):
        if self.sueldo > 3000:
            print(f"El empleado {self.nombre} debe pagar impuestos.")
#Main
empleado1 = Empleado()
empleado2 = Empleado()

empleado1.imprimir()
empleado1.impuestos()
empleado2.imprimir()
empleado2.impuestos()
