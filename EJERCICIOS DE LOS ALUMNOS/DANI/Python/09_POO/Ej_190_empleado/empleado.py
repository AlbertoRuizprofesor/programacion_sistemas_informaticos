# Confeccionar una clase que represente un empleado. 
class Empleado:
    # Definir como atributos su nombre y su sueldo. 
    # En el método __init__ cargar los atributos por teclado
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.nombre = self.nombre.capitalize()
        self.sueldo = float(input("Sueldo: "))
        self.impresion()
        self.impuestos()
#  y luego en otro método imprimir sus datos 
    def impresion(self):
        print(f"{self.nombre} gana {self.sueldo}€")
# y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
    def impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} debe pagar impuestos")