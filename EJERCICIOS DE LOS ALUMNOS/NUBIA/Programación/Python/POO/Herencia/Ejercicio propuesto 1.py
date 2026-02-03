
class Persona:
    def __init__(self, tipo, nombre, edad):
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
        
    def imprimir(self):
        print(self.tipo)
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        

class Empleado(Persona):
    def __init__(self, tipo, nombre, edad, sueldo):
        super().__init__(tipo, nombre, edad) 
        self.sueldo = sueldo
    
    def imprimir(self):
        super().imprimir()
        print(f"Sueldo: {self.sueldo}")
        

class Comercial(Empleado):
    def __init__(self, tipo, nombre, edad, sueldo, comision):
        super().__init__(tipo, nombre, edad, sueldo)
        self.comision = comision

    def imprimir(self):
        super().imprimir()
        print(f"Comisión: {self.comision}")
        
        
class Alumno(Persona):
    def __init__(self, tipo, nombre, edad, asignatura):
        super().__init__(tipo, nombre, edad)
        self.asignatura = asignatura
        
    def imprimir(self):
        super().imprimir()
        print(f"Asignatura: {self.asignatura}")
        
class Profesor(Empleado):
    def __init__(self, tipo, nombre, edad, sueldo, asignatura):
        super().__init__(tipo, nombre, edad, sueldo)
        self.asignatura = asignatura
        
    def imprimir(self):
        super().imprimir()
        print(f"Asignatura: {self.asignatura}")
        

# Bloque principal
persona1 = Persona("PERSONA", "Darío", 16)
persona1.imprimir()
print("-"*50)

empleado1 = Empleado("EMPLEADO", "Mónica", 47, 1200)
empleado1.imprimir()
print("-"*50)

alumno1 = Alumno("ALUMNO", "Nubia", 20, "Programación")
alumno1.imprimir()
print("-"*50)

profesor1 = Profesor("PROFESOR", "Jorge", 58, 2000, "Audiovisaules")
profesor1.imprimir()
print("-"*50)

comercial1 = Comercial("EMPLEADO COMERCIAL", "Eva", 45, 1200, 0.2)
comercial1.imprimir()
print("-"*50)
