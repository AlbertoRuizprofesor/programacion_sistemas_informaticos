""" 
Plantear una clase Persona que contenga dos atributos: nombre y edad.
Definir como responsabilidades la carga por teclado y su impresión.

En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y
agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)

También en el bloque principal del programa crear un objeto de la clase Empleado.
"""

class Persona:
    def __init__(self, tipo, nombre, edad):
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(f"{self.tipo}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
        
class Empleado(Persona):
    def __init__(self, tipo, nombre, edad, sueldo):
        super().__init__(tipo, nombre, edad)
        self.sueldo = sueldo
                    
    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)
        
    def paga_impuesto(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")
    
            
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

persona1 = Persona("ESTUDIANTE", "Darío", 17)
persona1.imprimir()
print("-"*50)
empleado1=Empleado("EMPLEADO", "Mónica", 40, 1800)
empleado1.imprimir()
empleado1.paga_impuesto()
print("-"*50)
alumno1 = Alumno("ALUMNO", "Nubia", 20, "Lengua")
alumno1.imprimir()
print("-"*50)
profesor1 = Profesor("PROFESOR", "Alberto", 45, 3500, "Mates")
profesor1.imprimir()
profesor1.paga_impuesto()

                    
    
        