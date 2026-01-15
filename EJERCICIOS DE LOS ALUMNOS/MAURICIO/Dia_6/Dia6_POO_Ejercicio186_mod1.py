# Definir objetos de la clase Persona.


class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.domicilio = ""
        self.telefono = ""

    def inicializar_datos(self, nombre, apellido="", edad=0, domicilio="", telefono=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    def mostrar_datos(self):
        print(
            f"\nEl nombre es: {self.nombre} y el apellido es: {self.apellido} y tiene {self.edad} años, vive en {self.domicilio} y su teléfono es {self.telefono}"
        )


# Crear dos objetos de la clase Persona
persona1 = Persona()
persona2 = Persona()
persona3 = Persona()

# Inicializar los nombres
persona1.inicializar_datos("Juan", "Pérez", 25, "Calle A", "123456789")
persona2.inicializar_datos("María", "Gómez", 30, "Calle B", "987654321")
persona3.inicializar_datos("Luis", "Rodríguez", 35, "Calle C", "456789123")

# Mostrar los datos
persona1.mostrar_datos()
persona2.mostrar_datos()
persona3.mostrar_datos()
