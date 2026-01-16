class Persona:

    def __init__(self):
        self.nombre="Carlos"
        self.edad=56

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


class Empleado(Persona):

    def __init__(self):
        super().__init__() #Añadimos todos los parametros puestos de persona.
        self.sueldo=668

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")

class Alumnos(Persona):
    def __init__(self):
        super().__init__()
        self.asignatura = "Matemáticas"
    def imprimir(self):
        super().imprimir()
        print(f"Asignatura: {self.asignatura}")



# bloque principal

persona1=Persona()
persona1.imprimir()
print("____________________________")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
print("____________________________")
alumno1 = Alumnos()
alumno1.imprimir()

