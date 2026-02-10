"""
Confeccionar una clase que permita cargar el nombre y la edad de una persona.
Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""
import funcionesJC as fnJC
#Funciones

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")


#Main
fnJC.borrarPantalla()
persona1 = Persona("Carlos López", 25)
fnJC.mensaje("Persona 1")
persona1.mostrar()
persona1.mayor_edad()

persona2 = Persona("Ana García", 16)
fnJC.mensaje("Persona 2")
persona2.mostrar()
persona2.mayor_edad()

fnJC.mensaje("Fin del programa")
