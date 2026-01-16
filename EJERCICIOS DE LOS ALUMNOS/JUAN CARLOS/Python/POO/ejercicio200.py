class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad)  # Llamada directa, sin super()
        self.sueldo = sueldo

    def imprimir(self):
        self.nombre  # Solo imprime lo propio + llama padre si quieres
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")

class Alumnos(Persona):
    def __init__(self, nombre, edad, asignatura):
        Persona.__init__(self, nombre, edad)  # Llamada directa, sin super()
        self.asignatura = asignatura

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print(f"Asignatura: {self.asignatura}")

class Profesor(Empleado, Alumnos):
    def __init__(self, nombre, edad, sueldo, asignatura):
        Persona.__init__(self, nombre, edad)  # Inicializa base una vez
        self.sueldo = sueldo
        self.asignatura = asignatura

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)
        print(f"Asignatura: {self.asignatura}")

# bloque principal
persona1 = Persona("Carlos", 56)
persona1.imprimir()
print("____________________________")
empleado1 = Empleado("Ana", 52, 3500)
empleado1.imprimir()
empleado1.paga_impuestos()
print("____________________________")
alumno1 = Alumnos("Marco", 18, "Animación 3D")
alumno1.imprimir()
print("____________________________")
profesor1 = Profesor("Alberto", 52, 4500, "Informática")
profesor1.imprimir()
profesor1.paga_impuestos()
