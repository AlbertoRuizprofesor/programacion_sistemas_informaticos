"""
Confeccionar una clase que represente un empleado.
Definir como atributos su nombre y su sueldo. 
En el método __init__ cargar los atributos por teclado
y luego en otro método imprimir sus datos
y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
"""

class Empleado:
    def __init__(self):
        for x in range(5):
            self.nombre = input(f"Ingrese el nombre del empleado {x+1}: ")
            self.sueldo = int(input(f"Ingrese el sueldo del empleado: "))
            print("---------------------------------------------------------")


    def imprimir(self):
            print(f"Nombre: {self.nombre}")
            print(f"Sueldo: {self.sueldo}")
            if self.sueldo > 3000:
                print("Debe pagar impuestos")
            print("------------------------")
        
empleado1 = Empleado()
empleado1.imprimir()