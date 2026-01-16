# Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados.
# Imprimir un mensaje si es mayor de edad (edad>=18)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")


# Bloque principal
persona1 = Persona("María", 12)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()

persona2 = Persona("Juan", 16)
persona2.mostrar_datos()
persona2.es_mayor_de_edad()
