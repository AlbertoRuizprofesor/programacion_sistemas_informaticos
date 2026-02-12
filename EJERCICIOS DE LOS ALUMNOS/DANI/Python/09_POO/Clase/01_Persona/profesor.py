from empleado import Empleado

class Profesor(Empleado):
    def __init__(self, nombre, edad, sueldo, asignatura):
        super().__init__(nombre, edad, sueldo)
        self.asignatura = asignatura

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Asignatura: {self.asignatura}")
