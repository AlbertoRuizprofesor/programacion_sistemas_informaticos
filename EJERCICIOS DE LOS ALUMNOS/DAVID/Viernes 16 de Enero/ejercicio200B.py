class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo=2400):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def imprimir(self):
        super().imprimir()
        print("Sueldo:", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


class Alumno(Persona):

    def __init__(self, nombre, edad, asignatura="Python"):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def imprimir(self):
        super().imprimir()
        print("Asignatura:", self.asignatura)


class Profesor(Empleado):

    def __init__(self, nombre, edad, asignatura="Python",sueldo=2400):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
        self.sueldo = sueldo
      

    def imprimir(self):
        super().imprimir()
class Comercial(Empleado):
    def __init__(self, nombre, edad, sueldo=2400,comision=0.10):
        super().__init__(nombre, edad, sueldo)
        self.comision = comision

    def imprimir(self):
        super().imprimir()
        print("Comision:", self.comision)


# bloque principal

empleado1 = Empleado("Alberto", 20)
empleado1.imprimir()
empleado1.paga_impuestos()
print("*******************Empleado")

alumno1 = Alumno("Juan", 36)
alumno1.imprimir()
print("*******************Alumno")
profesor1 = Profesor("Pedro", 40)
profesor1.imprimir()
profesor1.paga_impuestos()
print("*******************Comercial")
comercial1 = Comercial("Ana",23)
comercial1.imprimir()
comercial1.paga_impuestos()
