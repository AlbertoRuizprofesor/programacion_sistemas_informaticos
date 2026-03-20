'''
Crea una clase base Empleado con nombre y salario base.
Después crea las subclases Programador y Diseñador. 
Cada una debe redefinir un método calcular_salario según sus complementos. 
Idea clave: Incluye un método __str__ para imprimir la información del empleado. 
'''

# str sirve para imprimir la información del objeto de forma legible.

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario Base: {self.salario_base}" 
    
class Programador(Empleado):
    def __init__(self, nombre, salario_base, comision_proyecto, lenguaje_programacion):
        super().__init__(nombre, salario_base)
        self.comision_proyecto = comision_proyecto
        self.lenguaje_programacion = lenguaje_programacion

    def calcular_salario(self):
        return self.salario_base + self.comision_proyecto

    def __str__(self):
        return f"Programador: {self.nombre}, Lenguaje: {self.lenguaje_programacion}, Salario: {self.calcular_salario()}"
    
class Diseñador(Empleado):
    def __init__(self, nombre, salario_base, comision):
        super().__init__(nombre, salario_base)
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + self.comision

    def __str__(self):
        return f"Diseñador: {self.nombre}, Comisión: {self.comision}, Salario: {self.calcular_salario()}"
    
# main
empleado1 = Empleado("Andrés", 2000)
print(empleado1)

programador1 = Programador("Nubia", 3000, 80, "Python")
print(programador1)

diseñador1 = Diseñador("Darío", 3000, 150)
print(diseñador1)