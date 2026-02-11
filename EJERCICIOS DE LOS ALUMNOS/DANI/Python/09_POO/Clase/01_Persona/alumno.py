from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Asignatura: {self.asignatura}")
