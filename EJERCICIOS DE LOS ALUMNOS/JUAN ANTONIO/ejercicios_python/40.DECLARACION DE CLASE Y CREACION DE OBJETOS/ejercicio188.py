"""
Confeccionar una clase que permita carga el nombre y la edad de una persona.
 Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:

    # Método que inicializa los atributos del objeto.
    # Recibe un nombre y una edad, y los guarda dentro de la instancia.
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método que imprime los datos almacenados en el objeto.
    def imprimir(self):
        print("Nombre", self.nombre)
        print("Edad", self.edad)

    # Método que determina si la persona es mayor de edad.
    # Si la edad es 18 o más, imprime "Es mayor de edad".
    # Si no, imprime "No es mayor de edad".
    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")


# Bloque principal del programa

# Se crea un objeto de la clase Persona.
persona1 = Persona()

# Se inicializa el objeto con nombre "diego" y edad 40.
persona1.inicializar("diego", 40)

# Se muestran los datos almacenados.
persona1.imprimir()

# Se verifica si la persona es mayor de edad.
persona1.mayor_edad()
