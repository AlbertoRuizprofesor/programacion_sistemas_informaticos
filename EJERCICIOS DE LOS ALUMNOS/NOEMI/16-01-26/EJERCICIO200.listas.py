#Ejercicio 200: HACERLO SIN INPUT:P
"""Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.

En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)

También en el bloque principal del programa crear un objeto de la clase Empleado."""

class Persona:
    def __init__(self,nombre,edad,tipo):
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        print("Tipo",self.tipo)


class Empleado(Persona):

    def __init__(self, nombre, sueldo,edad,tipo):
        super().__init__(sueldo,edad,tipo)
        self.nombre=nombre
        self.sueldo=sueldo

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

persona1=Persona("noemi",28,"cajero")
persona1.imprimir()
print("_"*50)              #Multiplica el texto
empleado1=Empleado("noemi",2000,28,"Cajero")
empleado1.imprimir()
empleado1.paga_impuestos()

        