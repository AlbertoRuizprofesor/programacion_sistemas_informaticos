# Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    
    def mayor(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")