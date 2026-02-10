from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Sueldo: {self.sueldo}")
