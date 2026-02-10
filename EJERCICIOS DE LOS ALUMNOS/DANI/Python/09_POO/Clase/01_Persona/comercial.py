from empleado import Empleado

class Comercial(Empleado):
    def __init__(self, nombre, edad, sueldo, comision):
        super().__init__(nombre, edad, sueldo)
        self.comision = comision

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Comisión: {self.comision}")
