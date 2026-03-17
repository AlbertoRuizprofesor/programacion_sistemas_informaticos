# Implementaremos una clase llamada Persona que tendrá como atributo (variable)
# su nombre y dos métodos (funciones),
# uno de dichos métodos inicializará el atributo nombre y
# el siguiente método mostrará en la pantalla el contenido del mismo.

# Definir dos objetos de la clase Persona.


class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""

    # def inicializar_nombre(self, nombre, apellido="desconocido"):
    #     self.nombre = nombre
    #     self.apellido = apellido

    def mostrar_nombre(self):
        print(f"El nombre es: {self.nombre} y el apellido es: {self.apellido}")


# Crear dos objetos de la clase Persona
persona1 = Persona()
persona2 = Persona()
persona3 = Persona()

# Inicializar los nombres
persona1.inicializar_nombre("Juan", "Pérez")
persona2.inicializar_nombre("María")
persona3.inicializar_nombre("Luis", "Rodríguez")

# Mostrar los nombres
persona1.mostrar_nombre()
persona2.mostrar_nombre()
persona3.mostrar_nombre()
