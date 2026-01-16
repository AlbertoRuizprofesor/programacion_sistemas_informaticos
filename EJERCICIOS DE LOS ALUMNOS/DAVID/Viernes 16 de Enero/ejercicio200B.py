class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.cargo = "Comercial"
        # Sueldo de 1500 + 75 de comisión
        self.sueldo = 1500 + 75

    def imprimir(self):
        super().imprimir()
        print("Cargo:", self.cargo)
        print("Sueldo Total:", self.sueldo)


class Profesor(Empleado):
    def __init__(self):
        super().__init__()
        # El profesor añade la asignatura
        self.asignatura = "Python"

    def imprimir(self):
        super().imprimir()
        print("Asignatura dictada:", self.asignatura)


class Alumno(Profesor):
    def __init__(self):
        # Hereda nombre, edad, cargo, sueldo y asignatura
        super().__init__()
        self.nota = float(input("Ingrese la nota del alumno: "))

    def imprimir(self):
        super().imprimir()
        print("Nota del alumno:", self.nota)


# --- Bloque principal ---

print("--- Datos del Alumno (Hereda de toda la cadena) ---")
# Al crear al alumno, se activan todos los constructores superiores
alumno1 = Alumno()
print("\n--- FICHA COMPLETA DEL ALUMNO ---")
alumno1.imprimir()