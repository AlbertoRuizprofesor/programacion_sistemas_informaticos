"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. 
Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo 
sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)

También en el bloque principal del programa crear un objeto de la clase Empleado.
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Alumno(Persona):

    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def imprimir(self):
        super().imprimir()
        print("Asignatura:", self.asignatura)


class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
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


class Profesor(Alumno, Empleado):

    def __init__(self, nombre, edad, asignatura, sueldo):
        super().__init__(nombre, edad, asignatura)
        self.sueldo = sueldo

    def imprimir(self):
        super().imprimir()
        print("Sueldo:", self.sueldo)


# ======================
# BLOQUE PRINCIPAL
# ======================

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

print("____________________________")

persona1 = Persona(nombre, edad)
persona1.imprimir()

print("____________________________")

alumno1 = Alumno(nombre, edad, "Matemáticas")
alumno1.imprimir()

print("____________________________")

profesor1 = Profesor(nombre, edad, "Física", 3500)
profesor1.imprimir()
profesor1.paga_impuestos()

print("____________________________")

empleado1 = Empleado(nombre, edad, 2500)
empleado1.imprimir()
empleado1.paga_impuestos()



