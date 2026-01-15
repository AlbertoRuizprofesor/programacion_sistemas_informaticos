"""
Confeccionar una clase que permita carga el nombre y la edad de una persona.
Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:

    def __init__(self, nombre="", edad=""):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre: " , self.nombre)
        print("Edad: " , self.edad)

    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

persona1=Persona("Pablo", 20)
persona1.imprimir()
persona1.mayor_edad()





    