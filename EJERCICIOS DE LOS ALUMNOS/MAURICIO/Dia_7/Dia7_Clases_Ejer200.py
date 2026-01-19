class Persona:

    def __init__(self):
        self.nombre = "Paco"
        self.edad = 38

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo = 5000

    def imprimir(self):
        super().imprimir()
        print("Sueldo: ", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


class Alumno(Persona):

    def __init__(self):
        super().__init__()
        self.asignatura = "Lengua"

    def imprimir(self):
        super().imprimir()
        print("Asignatura: ", self.asignatura)


class Profesor(Empleado):

    def __init__(self):
        super().__init__()
        self.asignatura = "python"

    def imprimir(self):
        super().imprimir()
        print("Asignatura: ", self.asignatura)


class Comercial(Empleado):

    def __init__(self):
        super().__init__()
        self.comision = 7000

    def imprimir(self):
        super().imprimir()
        print("comisiónn: ", self.comision)


# bloque principal
# print("_____________PERSONA_______________")

# persona1 = Persona()
# persona1.imprimir()

# print("____________EMPLEADO________________")
# empleado1 = Empleado()
# empleado1.imprimir()
# empleado1.paga_impuestos()

# print("____________ALUMNO________________")
# alumno1 = Alumno()
# alumno1.imprimir()

# print("_____________PROFESOR_______________")
# profesor1 = Profesor()
# profesor1.imprimir()
# profesor1.paga_impuestos()

print("______________COMERCIAL______________")
comercial1 = Comercial()
comercial1.imprimir()
comercial1.paga_impuestos()
